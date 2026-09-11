#!/usr/bin/env python3
"""Regenerates tools/map_fragment.html (the Clients page map) from tools/us-states.json.
Edit PLACES below to add or move clients, then run: python3 tools/build_map.py && python3 tools/build_pages.py"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'us-states.json')))

# Albers equal-area conic (contiguous US)
p1, p2, l0, lam0 = map(math.radians, (29.5, 45.5, 23.0, -96.0))
n = (math.sin(p1) + math.sin(p2)) / 2; C = math.cos(p1) ** 2 + 2 * n * math.sin(p1); rho0 = math.sqrt(C - 2 * n * math.sin(l0)) / n
def proj(lon, lat):
    lam, phi = math.radians(lon), math.radians(lat); rho = math.sqrt(C - 2 * n * math.sin(phi)) / n; th = n * (lam - lam0)
    return rho * math.sin(th), rho0 - rho * math.cos(th)
SKIP = {'Alaska', 'Hawaii', 'Puerto Rico'}
feats = []; pts = []
for f in d['features']:
    name = f['properties']['name']
    if name in SKIP: continue
    g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    rings = [[proj(x, y) for x, y in ring] for poly in polys for ring in poly]
    feats.append((name, rings)); pts += [p for r in rings for p in r]
minx = min(p[0] for p in pts); maxx = max(p[0] for p in pts); miny = min(p[1] for p in pts); maxy = max(p[1] for p in pts)
W = 1400; s = W / (maxx - minx); H = (maxy - miny) * s
def T(p): return ((p[0] - minx) * s, (maxy - p[1]) * s)
def P(lon, lat): return T(proj(lon, lat))
states = ''.join('<path class="st" d="%s"><title>%s</title></path>' % (''.join('M' + ' L'.join('%.0f,%.0f' % T(p) for p in r) + 'Z' for r in rings), name) for name, rings in feats)

# ---- pins: (id, label, lon, lat, count, label placement, is_home)
PLACES = [
    ("home", "Home base &middot; Colorado", -104.99, 39.739, None, ("start", 46, 7), True),
    ("fayetteville", "Fayetteville, AR", -94.171, 36.082, 2, ("middle", 0, -44), False),
    ("nms", "North Mississippi", -89.10, 34.44, 3, ("middle", 0, 58), False),
    ("charlotte", "Charlotte, NC", -80.843, 35.227, 1, ("middle", 0, 58), False),
]
# When zoomed in past SPLIT_ZOOM the North Mississippi pin splits into its towns.
SPLIT = {"nms": [("Oxford, MS", -89.519, 34.366, 2), ("Baldwyn, MS", -88.635, 34.509, 1)]}
SPLIT_ZOOM = 7
MAPBOX_TOKEN = ""  # no longer used: map runs on MapLibre + OpenFreeMap (no key, no billing)
CARDS = {
    "home": None,
    "fayetteville": ("Fayetteville, AR", [
        ("Ella&rsquo;s Table at the Inn at Carnall Hall", "Social media management", "https://www.innatcarnallhall.com/restaurants-fayetteville-ar", "innatcarnallhall.com"),
        ("Lambeth Lounge at the Inn at Carnall Hall", "Social media management", "https://www.innatcarnallhall.com/restaurants-fayetteville-ar/lambeth-lounge-coffee-bar", "innatcarnallhall.com")]),
    "nms": ("North Mississippi", [
        ("Kristy Bridgers, Sober and Social <small>Oxford</small>", "Social media management, on-site shooting, paid ads, brand partnerships", "https://instagram.com/kbridgers1", "@kbridgers1"),
        ("Window Joe <small>Oxford</small>", "Social media management", "https://www.windowjoeoxford.com/", "windowjoeoxford.com"),
        ("JM Services <small>Baldwyn</small>", "Marketing management, CRM setup, print collateral", "https://jmservices.biz/", "jmservices.biz")]),
    "charlotte": ("Charlotte, NC", [
        ("Marelle Mahjong", "Instagram, content strategy, email marketing", "https://www.marellemahjong.com/", "marellemahjong.com")]),
}
STAR = "/assets/img/star-teal.png"
pins = ''; xs = []; ys = []
for pid, label, lon, lat, cnt, (anchor, lx, ly), home in PLACES:
    x, y = P(lon, lat); xs.append(x); ys.append(y)
    badge = '' if cnt is None else '<circle class="cnt" cx="22" cy="-22" r="13"/><text class="cntt" x="22" y="-17">%d</text>' % cnt
    pins += '''<g class="pin%s" data-place="%s" transform="translate(%.0f,%.0f)" tabindex="0" role="button" aria-label="%s">
      <circle class="halo" r="38"/>
      <image href="%s" x="-27" y="-30" width="54" height="60"/>%s
      <text class="pinl" style="text-anchor:%s" x="%d" y="%d">%s</text>
    </g>''' % (' home' if home else '', pid, x, y, label.replace('&middot;', '-'), STAR, badge, anchor, lx, ly, label)
zx0 = min(xs) - 120; zy0 = min(ys) - 110; zw = max(xs) - min(xs) + 240 + 160; zh = max(ys) - min(ys) + 220
if zh / zw < 0.66: zh = zw * 0.66
zoom = '%.0f %.0f %.0f %.0f' % (zx0, zy0, zw, zh)

cards = '<section class="place home" id="place-home" data-place="home"><h3><img src="%s" alt="" width="18" height="20">Home base &middot; Colorado</h3><p class="homep">Where the tour is booked from. Every stop on this map, and the ones not on it yet, gets the same hospitality-forward treatment from here.</p></section>' % STAR
for pid, label, lon, lat, cnt, _, home in PLACES:
    if home: continue
    title, items = CARDS[pid]
    lis = ''.join('<li><a href="%s" target="_blank" rel="noopener"><strong>%s</strong><span>%s</span><em>%s &#8594;</em></a></li>' % (u, nme, svc, lnk) for nme, svc, u, lnk in items)
    cards += '<section class="place" id="place-%s" data-place="%s"><h3><img src="%s" alt="" width="18" height="20">%s</h3><p class="bill">On the bill</p><ul>%s</ul></section>' % (pid, pid, STAR, title, lis)

import json as _json
GL_PLACES = [{"id": pid, "label": label.replace("&middot;", "\u00b7"), "lon": lon, "lat": lat, "count": cnt, "home": home,
              "split": [{"label": l, "lon": x, "lat": y, "count": c} for l, x, y, c in SPLIT.get(pid, [])]}
             for pid, label, lon, lat, cnt, _, home in PLACES]
GL_JSON = _json.dumps(GL_PLACES)
frag = '''<!-- CLIENT MAP (generated by tools/build_map.py) -->
<section class="clientmap" id="map">
  <p class="kicker">Tour stops</p>
  <h2>Where the tour has played</h2>
  <p class="packages-intro">Click a star for the venues at each stop, and click a name to visit them.</p>
  <ul class="pillars industries">
    <li>Salons &amp; spas</li>
    <li>Restaurants &amp; bars</li>
    <li>Home services</li>
    <li>Retail &amp; e-commerce</li>
    <li>B2B distribution</li>
    <li>Personal brands</li>
  </ul>
  <div class="mapbox">
    <svg class="map" viewBox="0 0 %d %d" data-full="0 0 %d %d" data-zoom="%s" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Map of the United States with Studio Jam client locations"><g>%s</g><g id="pins">%s</g></svg>
    <div id="sj-gl" class="gl-map" aria-hidden="true"></div>
    <span class="note">3 stops &middot; 6 venues &middot; 1 home base</span>
    <img class="mascot" src="/assets/img/mascot-chat.png" alt="" width="466" height="891" loading="lazy" decoding="async">
  </div>
  <div class="list">%s</div>
</section>
<script>
(function () {
  var pins = document.querySelectorAll('.clientmap .pin'), places = document.querySelectorAll('.clientmap .place');
  function set(id) {
    pins.forEach(function (p) { p.classList.toggle('on', p.dataset.place === id); });
    places.forEach(function (c) { c.classList.toggle('on', c.dataset.place === id); });
    var el = document.getElementById('place-' + id);
    if (el && window.innerWidth < 860) el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  pins.forEach(function (p) {
    p.addEventListener('click', function () { set(p.dataset.place); });
    p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(p.dataset.place); } });
  });
  places.forEach(function (c) { c.addEventListener('mouseenter', function () { set(c.dataset.place); }); });
  set('home');
  var svg = document.querySelector('.clientmap svg.map');
  function fit() { svg.setAttribute('viewBox', window.innerWidth < 700 ? svg.dataset.zoom : svg.dataset.full); }
  fit(); window.addEventListener('resize', fit);

  /* ---- MapLibre GL layer on OpenFreeMap tiles (the drawn map above stays as the fallback) ---- */
  var PLACES = %s;
  var box = document.querySelector('.clientmap .mapbox');
  function startGL() {
    if (!window.maplibregl) return;
    var GL = window.maplibregl;
    var style = {
      version: 8,
      glyphs: 'https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf',
      sources: { omt: { type: 'vector', url: 'https://tiles.openfreemap.org/planet', attribution: '&copy; <a href="https://openfreemap.org">OpenFreeMap</a> &copy; <a href="https://www.openmaptiles.org/">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' } },
      layers: [
        { id: 'bg', type: 'background', paint: { 'background-color': '#F6F7F7' } },
        { id: 'park', type: 'fill', source: 'omt', 'source-layer': 'park', minzoom: 9, paint: { 'fill-color': '#0B4F61', 'fill-opacity': 0.06 } },
        { id: 'water', type: 'fill', source: 'omt', 'source-layer': 'water', filter: ['!=', ['get', 'brunnel'], 'tunnel'], paint: { 'fill-color': '#0B4F61', 'fill-opacity': 0.16 } },
        { id: 'waterway', type: 'line', source: 'omt', 'source-layer': 'waterway', minzoom: 8, paint: { 'line-color': '#0B4F61', 'line-opacity': 0.25, 'line-width': 1 } },
        { id: 'roads-minor', type: 'line', source: 'omt', 'source-layer': 'transportation', minzoom: 12, filter: ['in', ['get', 'class'], ['literal', ['minor', 'tertiary', 'service']]], paint: { 'line-color': '#0B4F61', 'line-opacity': 0.14, 'line-width': ['interpolate', ['linear'], ['zoom'], 12, 0.6, 16, 2] } },
        { id: 'roads-major', type: 'line', source: 'omt', 'source-layer': 'transportation', minzoom: 8, filter: ['in', ['get', 'class'], ['literal', ['motorway', 'trunk', 'primary', 'secondary']]], paint: { 'line-color': '#0B4F61', 'line-opacity': 0.3, 'line-width': ['interpolate', ['linear'], ['zoom'], 8, 0.6, 14, 3] } },
        { id: 'admin-4', type: 'line', source: 'omt', 'source-layer': 'boundary', filter: ['all', ['==', ['get', 'admin_level'], 4], ['!=', ['get', 'maritime'], 1]], paint: { 'line-color': '#0B4F61', 'line-width': ['interpolate', ['linear'], ['zoom'], 3, 0.8, 8, 1.4], 'line-opacity': 0.7 } },
        { id: 'admin-2', type: 'line', source: 'omt', 'source-layer': 'boundary', filter: ['all', ['==', ['get', 'admin_level'], 2], ['!=', ['get', 'maritime'], 1]], paint: { 'line-color': '#0B4F61', 'line-width': 1.6 } },
        { id: 'state-labels', type: 'symbol', source: 'omt', 'source-layer': 'place', minzoom: 3.5, maxzoom: 7, filter: ['==', ['get', 'class'], 'state'], layout: { 'text-field': ['get', 'name:en'], 'text-font': ['Noto Sans Regular'], 'text-size': 12, 'text-letter-spacing': 0.2, 'text-transform': 'uppercase' }, paint: { 'text-color': '#849D9B' } },
        { id: 'city-labels', type: 'symbol', source: 'omt', 'source-layer': 'place', minzoom: 6, filter: ['all', ['in', ['get', 'class'], ['literal', ['city', 'town']]], ['<=', ['coalesce', ['get', 'rank'], 15], 12]], layout: { 'text-field': ['coalesce', ['get', 'name:en'], ['get', 'name']], 'text-font': ['Noto Sans Regular'], 'text-size': ['interpolate', ['linear'], ['zoom'], 6, 11, 12, 15], 'text-transform': 'uppercase', 'text-letter-spacing': 0.12 }, paint: { 'text-color': '#0B4F61', 'text-halo-color': '#F6F7F7', 'text-halo-width': 1.4 } }
      ]
    };
    var map = new GL.Map({ container: 'sj-gl', style: style, center: [-92, 36.5], zoom: 3.6, minZoom: 2.5, maxZoom: 15, cooperativeGestures: true, attributionControl: { compact: true }, dragRotate: false, pitchWithRotate: false, touchPitch: false });
    map.addControl(new GL.NavigationControl({ showCompass: false }), 'top-right');
    window.__sjMap = map; window.__sjErrors = []; map.on('error', function (e) { window.__sjErrors.push(String(e && e.error && e.error.message || e)); });
    var markers = {}; var splitMarkers = [];
    function makeEl(label, count, home, id) {
      var el = document.createElement('div'); el.className = 'gl-pin' + (home ? ' home' : ''); el.setAttribute('role', 'button'); el.tabIndex = 0; el.setAttribute('aria-label', label);
      el.innerHTML = '<span class="gl-halo"></span><img src="/assets/img/star-teal.png" alt="" width="44" height="49">' + (count ? '<b>' + count + '</b>' : '') + '<i>' + label + '</i>';
      if (id) { el.addEventListener('click', function (e) { e.stopPropagation(); set(id); }); el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(id); } }); }
      return el;
    }
    var b = new GL.LngLatBounds();
    PLACES.forEach(function (p) {
      var el = makeEl(p.label, p.count, p.home, p.id);
      markers[p.id] = new GL.Marker({ element: el, anchor: 'center' }).setLngLat([p.lon, p.lat]).addTo(map);
      b.extend([p.lon, p.lat]);
      p.split.forEach(function (c) {
        var m = new GL.Marker({ element: makeEl(c.label, c.count, false, p.id), anchor: 'center' }).setLngLat([c.lon, c.lat]);
        splitMarkers.push({ parent: p.id, marker: m });
      });
    });
    function applySplit() {
      var z = map.getZoom();
      splitMarkers.forEach(function (sm) {
        var parent = markers[sm.parent];
        if (z >= %d) { sm.marker.addTo(map); parent.getElement().classList.add('is-split'); }
        else { sm.marker.remove(); parent.getElement().classList.remove('is-split'); }
      });
    }
    map.on('zoom', applySplit);
    map.on('load', function () {
      box.classList.add('gl-ready');
      var pad = window.innerWidth < 700 ? 34 : 90; map.fitBounds(b, { padding: { top: pad + 20, right: pad, bottom: pad, left: pad }, maxZoom: 5.2, duration: 0 });
      applySplit();
    });
    map.on('error', function (e) { if (!box.classList.contains('gl-ready')) box.classList.add('gl-failed'); });
    window.__sjFly = function (id) {
      var p = PLACES.filter(function (x) { return x.id === id; })[0]; if (!p) return;
      Object.keys(markers).forEach(function (k) { markers[k].getElement().classList.toggle('on', k === id); });
      map.flyTo({ center: [p.lon, p.lat], zoom: p.split.length ? 7.4 : 6.2, speed: 0.9, curve: 1.3, essential: true });
    };
  }
  var _set = set;
  set = function (id) { _set(id); if (window.__sjFly) window.__sjFly(id); };
  var s1 = document.createElement('link'); s1.rel = 'stylesheet'; s1.href = 'https://cdnjs.cloudflare.com/ajax/libs/maplibre-gl/5.6.0/maplibre-gl.css'; document.head.appendChild(s1);
  var s2 = document.createElement('script'); s2.src = 'https://cdnjs.cloudflare.com/ajax/libs/maplibre-gl/5.6.0/maplibre-gl.js'; s2.onload = startGL; s2.onerror = function () { box.classList.add('gl-failed'); }; document.head.appendChild(s2);
})();
</script>
''' % (W, H, W, H, zoom, states, pins, cards, GL_JSON, SPLIT_ZOOM)
open(os.path.join(HERE, 'map_fragment.html'), 'w', encoding='utf-8').write(frag)
print('map fragment written:', len(frag) // 1024, 'KB; zoom', zoom)
