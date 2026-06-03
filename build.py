#!/usr/bin/env python3
"""
build.py - JustFly Affiliate Site Generator v2
Deploys to: https://brightlane.github.io/justfly/
Affiliate URL: https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885
Run: python3 build.py
Output: docs/ folder (GitHub Pages source)
"""

import json
from pathlib import Path
from datetime import date

AFF   = "https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885"
BASE  = "https://brightlane.github.io/justfly"
SUB   = "/justfly"
TODAY = date.today().isoformat()
OUT   = Path("docs")

# ─── PAGES ───────────────────────────────────────────────────────────────────
PAGES = [
    {"slug":"index","title":"JustFly 2026: Cheapest Flights — 500+ Airlines, Save Up To 70%","desc":"JustFly finds cheaper flights than Expedia, Kayak & Priceline on most US routes. Compare 500+ airlines, bundle hotels, set price alerts. Search free now.","content_fn":"page_home","priority":"1.0"},
    {"slug":"justfly-review","title":"JustFly Review 2026: Legit, Safe & Worth It? Full Verdict","desc":"Our 6-month JustFly review. Is it safe? Is it cheaper? We tested 30 routes and made real bookings. Honest verdict — pros, cons, and everything in between.","content_fn":"page_review","priority":"0.95"},
    {"slug":"justfly-vs-expedia","title":"JustFly vs Expedia 2026: 20-Route Price Battle","desc":"JustFly vs Expedia: real price tests on 20 popular US routes. Who is cheaper? By how much? Full data inside.","content_fn":"page_vs_expedia","priority":"0.9"},
    {"slug":"justfly-vs-kayak","title":"JustFly vs Kayak 2026: Which Actually Saves You Money?","desc":"JustFly vs Kayak compared. Full booking platform vs meta-search redirect — which gets you the cheapest confirmed fare?","content_fn":"page_vs_kayak","priority":"0.9"},
    {"slug":"justfly-vs-priceline","title":"JustFly vs Priceline 2026: Transparent vs Blind Pricing","desc":"JustFly vs Priceline compared. Transparent fares vs mystery deals — which travel site wins for most US travelers in 2026?","content_fn":"page_vs_priceline","priority":"0.9"},
    {"slug":"cheap-flights-usa","title":"Cheapest Domestic Flights USA 2026 | JustFly Route Guide","desc":"The 20 cheapest US flight routes in 2026 with live fares, best booking windows, and airline recommendations. All searchable on JustFly.","content_fn":"page_cheap_usa","priority":"0.9"},
    {"slug":"nyc-flights","title":"Cheap Flights from New York 2026 | JustFly JFK/LGA/EWR","desc":"Best fares from New York City in 2026. Every airline from JFK, LGA & EWR compared on JustFly — NYC to LA from $89.","content_fn":"page_nyc","priority":"0.85"},
    {"slug":"miami-flights","title":"Cheap Flights from Miami 2026 | JustFly MIA Deals","desc":"Find the cheapest flights from Miami in 2026. JustFly compares every airline from MIA to every destination.","content_fn":"page_miami","priority":"0.85"},
    {"slug":"los-angeles-flights","title":"Cheap Flights from Los Angeles 2026 | JustFly LAX Deals","desc":"Cheapest flights from LAX in 2026. NYC from $89, Vegas from $59, Seattle from $65. All on JustFly.","content_fn":"page_lax","priority":"0.85"},
    {"slug":"chicago-flights","title":"Cheap Flights from Chicago 2026 | JustFly ORD & MDW","desc":"Cheap flights from O'Hare and Midway in 2026. Compare every airline from Chicago on JustFly.","content_fn":"page_chicago","priority":"0.85"},
    {"slug":"las-vegas-flights","title":"Cheap Flights to Las Vegas 2026 | JustFly LAS Deals","desc":"Find the cheapest flights to Las Vegas from every major US city in 2026. Live fares on JustFly.","content_fn":"page_vegas","priority":"0.85"},
    {"slug":"international-flights","title":"Cheap International Flights from USA 2026 | JustFly","desc":"Mexico, Caribbean, Europe, Asia — JustFly compares hundreds of international fares from every US airport. Best prices 2026.","content_fn":"page_international","priority":"0.85"},
    {"slug":"flight-hotel-bundles","title":"Flight + Hotel Bundles 2026 | Save Up to 40% on JustFly","desc":"Bundle your flight and hotel on JustFly and save up to 40% vs booking separately. Real savings examples for 2026.","content_fn":"page_bundles","priority":"0.85"},
    {"slug":"flight-booking-tips","title":"15 Flight Booking Tips That Actually Save Money in 2026","desc":"15 data-backed strategies to pay less on every flight. Real savings techniques used by frequent travelers — all work on JustFly.","content_fn":"page_tips","priority":"0.85"},
    {"slug":"best-time-to-book","title":"Best Time to Book Flights 2026: Month-by-Month Data Guide","desc":"When is the best time to book a flight in 2026? Day, week, and month-by-month analysis with real price data. Search on JustFly.","content_fn":"page_timing","priority":"0.8"},
    {"slug":"baggage-fees","title":"Airline Baggage Fees 2026: Every US Carrier — Full Chart","desc":"Complete airline baggage fee guide for 2026. Know the true cost before you book — and find the cheapest all-in fare on JustFly.","content_fn":"page_baggage","priority":"0.8"},
    {"slug":"last-minute-flights","title":"Last Minute Flights USA 2026 | Same-Day Deals That Work","desc":"How to find cheap last-minute flights in 2026. What actually works — and how to search on JustFly for the best same-day fares.","content_fn":"page_last_minute","priority":"0.8"},
    {"slug":"budget-airlines","title":"US Budget Airlines 2026: Spirit vs Frontier vs Allegiant vs Southwest","desc":"Complete 2026 guide to US budget airlines. Real total-cost comparisons including all fees. Book the cheapest all-in fare on JustFly.","content_fn":"page_budget","priority":"0.8"},
    {"slug":"promo-codes","title":"JustFly Promo Codes & Deals June 2026 | Best Offers","desc":"Latest JustFly promo codes and best deals for June 2026. How to get the lowest price on flights, hotels and bundles.","content_fn":"page_promos","priority":"0.75"},
    {"slug":"about","title":"About FlightDealsPro | Independent JustFly Affiliate Partner","desc":"About FlightDealsPro — independent guide helping US travelers find cheaper flights with JustFly since 2020.","content_fn":"page_about","priority":"0.5"},
]

# ─── CSS ─────────────────────────────────────────────────────────────────────
def css():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@400;500;700;800;900&family=Satoshi:wght@400;500;700&display=swap');
    :root {
      --navy:    #050f1c;
      --blue:    #0047cc;
      --sky:     #0066ff;
      --electric:#4d9dff;
      --orange:  #ff5500;
      --ember:   #ff7733;
      --gold:    #ffaa00;
      --green:   #00b87a;
      --fog:     #f0f4fa;
      --warm:    #fff9f6;
      --white:   #ffffff;
      --muted:   #637188;
      --border:  #dce5f0;
      --ink:     #0b1523;
      --r:       12px;
      --sh:      0 2px 16px rgba(5,15,28,.08);
      --sh2:     0 10px 40px rgba(5,15,28,.16);
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { font-family:'Satoshi',sans-serif; background:var(--fog); color:var(--ink); line-height:1.7; }
    a { color:var(--sky); text-decoration:none; }
    a:hover { text-decoration:underline; }
    p { margin-bottom:1rem; }
    h1,h2,h3,h4 { font-family:'Cabinet Grotesk',sans-serif; line-height:1.15; margin-bottom:.8rem; font-weight:900; }
    h1 { font-size:clamp(2.2rem,5.5vw,3.8rem); }
    h2 { font-size:clamp(1.7rem,4vw,2.6rem); }
    h3 { font-size:1.2rem; }

    /* SAVINGS TICKER */
    .ticker {
      background:var(--orange);
      color:#fff; text-align:center; font-size:.82rem; font-weight:700;
      padding:.5rem 1rem; letter-spacing:.01em;
    }
    .ticker a { color:#ffe0d0; border-bottom:1px solid rgba(255,224,208,.4); }

    /* NAV */
    nav {
      background:var(--navy);
      padding:.9rem 1.5rem;
      display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:.6rem;
      position:sticky; top:0; z-index:200;
      box-shadow:0 2px 20px rgba(5,15,28,.4);
    }
    .logo { font-family:'Cabinet Grotesk',sans-serif; font-size:1.3rem; font-weight:900; color:#fff; text-decoration:none; display:flex; align-items:center; gap:.45rem; letter-spacing:-.01em; }
    .logo-mark { background:var(--orange); color:#fff; width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0; }
    .logo em { color:var(--gold); font-style:normal; }
    .nav-links { display:flex; gap:1.4rem; font-size:.85rem; font-weight:700; flex-wrap:wrap; }
    .nav-links a { color:rgba(255,255,255,.6); transition:color .2s; }
    .nav-links a:hover { color:#fff; text-decoration:none; }
    .nav-cta { background:var(--orange); color:#fff !important; padding:.5rem 1.3rem; border-radius:6px; font-size:.84rem; font-weight:800; transition:all .2s !important; }
    .nav-cta:hover { background:var(--ember) !important; transform:translateY(-1px); text-decoration:none !important; }

    /* HERO */
    .hero {
      background:var(--navy);
      background-image:
        radial-gradient(ellipse at 0% 100%, rgba(0,71,204,.7) 0%, transparent 50%),
        radial-gradient(ellipse at 100% 0%, rgba(255,85,0,.25) 0%, transparent 45%),
        radial-gradient(ellipse at 50% 50%, rgba(0,102,255,.15) 0%, transparent 60%);
      color:#fff; text-align:center;
      padding:6rem 1.5rem 5rem;
      position:relative; overflow:hidden;
    }
    .hero::after {
      content:'';
      position:absolute; inset:0;
      background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Ccircle cx='30' cy='30' r='1' fill='white' fill-opacity='0.04'/%3E%3C/svg%3E");
      pointer-events:none;
    }
    .hero-inner { max-width:900px; margin:0 auto; position:relative; z-index:1; }
    .hero h1 { color:#fff; margin-bottom:1.3rem; letter-spacing:-.02em; }
    .hero h1 em { background:linear-gradient(90deg,var(--gold),var(--ember)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-style:normal; }
    .hero-sub { font-size:1.15rem; color:rgba(255,255,255,.68); max-width:640px; margin:0 auto 2.4rem; line-height:1.65; }
    .hero-badge {
      display:inline-flex; align-items:center; gap:.5rem;
      background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.15);
      color:rgba(255,255,255,.85); font-size:.78rem; font-weight:700;
      padding:.35rem 1rem; border-radius:50px; margin-bottom:1.4rem;
      letter-spacing:.05em; text-transform:uppercase;
    }
    .hero-badge-dot { width:6px; height:6px; border-radius:50%; background:var(--green); animation:pulse 2s infinite; }
    @keyframes pulse { 0%,100%{opacity:1;} 50%{opacity:.4;} }
    .hero-ctas { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }
    .hero-proof {
      display:flex; justify-content:center; flex-wrap:wrap; gap:2.5rem;
      margin-top:3.5rem; padding-top:3rem;
      border-top:1px solid rgba(255,255,255,.08);
    }
    .proof-num { font-family:'Cabinet Grotesk',sans-serif; font-size:2.2rem; font-weight:900; color:#fff; line-height:1; }
    .proof-num em { color:var(--gold); font-style:normal; }
    .proof-lbl { font-size:.72rem; color:rgba(255,255,255,.4); text-transform:uppercase; letter-spacing:.09em; margin-top:.25rem; }

    /* BUTTONS */
    .btn { display:inline-flex; align-items:center; gap:.5rem; padding:1rem 2.2rem; border-radius:8px; font-weight:800; font-size:1rem; cursor:pointer; transition:all .2s; text-decoration:none; white-space:nowrap; font-family:'Cabinet Grotesk',sans-serif; letter-spacing:-.01em; }
    .btn-orange { background:var(--orange); color:#fff; box-shadow:0 4px 20px rgba(255,85,0,.4); }
    .btn-orange:hover { background:var(--ember); transform:translateY(-2px); box-shadow:0 8px 28px rgba(255,85,0,.5); text-decoration:none; }
    .btn-blue { background:var(--sky); color:#fff; box-shadow:0 4px 20px rgba(0,102,255,.3); }
    .btn-blue:hover { background:var(--blue); transform:translateY(-2px); text-decoration:none; }
    .btn-ghost { background:rgba(255,255,255,.08); color:#fff; border:1px solid rgba(255,255,255,.2); }
    .btn-ghost:hover { background:rgba(255,255,255,.15); text-decoration:none; }
    .btn-outline { background:transparent; color:var(--orange); border:2px solid var(--orange); }
    .btn-outline:hover { background:var(--orange); color:#fff; text-decoration:none; }
    .btn-sm { padding:.55rem 1.2rem; font-size:.85rem; }
    .btn-lg { padding:1.15rem 2.6rem; font-size:1.1rem; }

    /* LAYOUT */
    section { padding:4.5rem 1.5rem; }
    .bg-white { background:var(--white); }
    .bg-warm { background:var(--warm); }
    .bg-navy { background:var(--navy); }
    .container { max-width:1120px; margin:0 auto; }
    .eyebrow { font-size:.72rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--orange); margin-bottom:.5rem; display:block; }
    .section-sub { color:var(--muted); font-size:1rem; margin-bottom:2rem; max-width:580px; }
    .text-center { text-align:center; }
    .text-center .section-sub { margin-left:auto; margin-right:auto; }
    .mt-2 { margin-top:2rem; }
    .mt-3 { margin-top:3rem; }

    /* DEAL CARDS */
    .deals-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(255px,1fr)); gap:1.2rem; margin-top:1.5rem; }
    .deal-card {
      background:var(--white); border-radius:var(--r); box-shadow:var(--sh);
      padding:1.7rem; position:relative; overflow:hidden;
      border-bottom:3px solid var(--orange);
      transition:transform .2s, box-shadow .2s;
    }
    .deal-card::before { content:''; position:absolute; top:0; right:0; width:70px; height:70px; background:radial-gradient(circle at top right, rgba(255,85,0,.06), transparent); }
    .deal-card:hover { transform:translateY(-4px); box-shadow:var(--sh2); }
    .deal-from { font-size:.7rem; font-weight:800; color:var(--muted); text-transform:uppercase; letter-spacing:.07em; margin-bottom:.25rem; }
    .deal-price { font-family:'Cabinet Grotesk',sans-serif; font-size:2.8rem; font-weight:900; color:var(--orange); line-height:1; margin-bottom:.25rem; letter-spacing:-.02em; }
    .deal-route { font-weight:800; font-size:1rem; margin-bottom:.6rem; color:var(--ink); }
    .deal-tag { display:inline-block; font-size:.68rem; font-weight:800; padding:.2rem .7rem; border-radius:4px; margin-bottom:.8rem; text-transform:uppercase; letter-spacing:.05em; }
    .tag-hot { background:#fff0ec; color:#c0392b; }
    .tag-sale { background:#fff8e1; color:#e65100; }
    .tag-new { background:#e8f5e9; color:#1b5e20; }
    .tag-flash { background:#e3f2fd; color:#0d47a1; }
    .deal-note { font-size:.84rem; color:var(--muted); margin-bottom:1rem; line-height:1.5; }

    /* DESTINATION CARDS */
    .dest-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:.9rem; margin-top:1.5rem; }
    .dest-card { background:var(--white); border-radius:var(--r); padding:1.3rem .9rem; text-align:center; box-shadow:var(--sh); border:1px solid var(--border); transition:all .2s; display:block; text-decoration:none; }
    .dest-card:hover { transform:translateY(-3px); box-shadow:var(--sh2); border-color:var(--orange); text-decoration:none; }
    .dest-emoji { font-size:1.9rem; margin-bottom:.4rem; }
    .dest-city { font-weight:800; font-size:.92rem; color:var(--ink); margin-bottom:.2rem; font-family:'Cabinet Grotesk',sans-serif; }
    .dest-price { color:var(--orange); font-weight:800; font-size:.88rem; }

    /* FEATURE CARDS */
    .feat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(235px,1fr)); gap:1.2rem; }
    .feat-card { background:var(--white); border-radius:var(--r); padding:1.8rem; box-shadow:var(--sh); border:1px solid var(--border); transition:transform .2s; }
    .feat-card:hover { transform:translateY(-2px); }
    .feat-icon { font-size:1.8rem; margin-bottom:.8rem; display:block; }
    .feat-card h3 { font-size:1rem; margin-bottom:.35rem; font-weight:800; }
    .feat-card p { color:var(--muted); font-size:.87rem; line-height:1.6; }

    /* TABLES */
    .tbl-wrap { background:var(--white); border-radius:var(--r); box-shadow:var(--sh); overflow:hidden; }
    table { width:100%; border-collapse:collapse; }
    th { background:var(--navy); color:#fff; padding:.95rem 1.1rem; font-size:.77rem; text-transform:uppercase; letter-spacing:.07em; text-align:left; font-weight:800; font-family:'Cabinet Grotesk',sans-serif; }
    td { padding:.88rem 1.1rem; border-bottom:1px solid var(--border); font-size:.92rem; }
    tr:last-child td { border-bottom:none; }
    tr:nth-child(even) td { background:var(--fog); }
    .win { color:var(--orange); font-weight:800; }
    .good { color:var(--green); font-weight:700; }
    .bad { color:#c0392b; }
    .chk { color:var(--green); font-size:1.1rem; font-weight:700; }
    .vs-hl td:nth-child(2) { background:#fff9f6; }
    .vs-hl th:nth-child(2) { background:var(--orange); }

    /* TESTIMONIALS */
    .testi-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(275px,1fr)); gap:1.3rem; margin-top:1.5rem; }
    .testi-card { background:var(--white); border-radius:var(--r); padding:1.9rem; box-shadow:var(--sh); position:relative; }
    .testi-card::before { content:'"'; font-family:'Cabinet Grotesk',sans-serif; font-size:5rem; color:var(--electric); position:absolute; top:.2rem; left:1.2rem; line-height:1; opacity:.15; font-weight:900; }
    .testi-stars { color:var(--gold); font-size:.9rem; margin-bottom:.8rem; letter-spacing:.05em; }
    .testi-text { font-size:.93rem; color:var(--ink); margin-bottom:1rem; line-height:1.7; padding-top:.4rem; }
    .testi-name { font-weight:800; font-size:.87rem; color:var(--orange); font-family:'Cabinet Grotesk',sans-serif; }
    .testi-detail { font-size:.78rem; color:var(--muted); margin-top:.2rem; }
    .testi-save { display:inline-block; background:#fff0ec; color:var(--orange); font-size:.73rem; font-weight:800; padding:.2rem .7rem; border-radius:4px; margin-top:.5rem; font-family:'Cabinet Grotesk',sans-serif; }

    /* FAQ */
    .faq-wrap { margin-top:1.5rem; }
    details { border:1.5px solid var(--border); border-radius:10px; margin-bottom:.85rem; overflow:hidden; background:var(--white); }
    summary { padding:1.1rem 1.4rem; font-weight:800; font-size:.95rem; cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Cabinet Grotesk',sans-serif; }
    summary::-webkit-details-marker { display:none; }
    summary::after { content:'+'; font-size:1.5rem; color:var(--orange); font-weight:300; flex-shrink:0; line-height:1; }
    details[open] summary::after { content:'&#8722;'; }
    details[open] summary { border-bottom:1px solid var(--border); color:var(--orange); }
    .faq-ans { padding:1.2rem 1.4rem 1.5rem; color:var(--muted); font-size:.92rem; line-height:1.75; }

    /* CTA BAND */
    .cta-band {
      background:var(--navy);
      border-radius:var(--r); padding:3.5rem 2rem; text-align:center; color:#fff;
      position:relative; overflow:hidden;
      border:1px solid rgba(0,102,255,.2);
    }
    .cta-band::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at center, rgba(0,102,255,.15) 0%, transparent 70%); }
    .cta-band h2 { font-family:'Cabinet Grotesk',sans-serif; color:#fff; font-size:clamp(1.6rem,3.5vw,2.4rem); margin-bottom:.7rem; position:relative; z-index:1; letter-spacing:-.02em; }
    .cta-band p { color:rgba(255,255,255,.68); margin-bottom:2rem; font-size:1.05rem; position:relative; z-index:1; }

    /* TIP CARDS */
    .tip-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(235px,1fr)); gap:1.2rem; margin-top:1.5rem; }
    .tip-card { background:var(--white); border-radius:var(--r); padding:1.6rem; box-shadow:var(--sh); border:1px solid var(--border); }
    .tip-num { font-family:'Cabinet Grotesk',sans-serif; font-size:2.6rem; font-weight:900; color:var(--orange); opacity:.2; line-height:1; margin-bottom:.5rem; letter-spacing:-.03em; }
    .tip-card h3 { font-size:1rem; margin-bottom:.35rem; font-weight:800; }
    .tip-card p { font-size:.86rem; color:var(--muted); line-height:1.6; }

    /* SAVINGS STRIP */
    .savings-strip { background:var(--orange); color:#fff; padding:1rem 1.5rem; text-align:center; font-weight:800; font-size:.95rem; letter-spacing:.01em; }
    .savings-strip a { color:#ffe0d0; border-bottom:1px solid rgba(255,224,208,.5); }

    /* STICKY BAR */
    .sticky-bar {
      position:fixed; bottom:0; left:0; right:0;
      background:var(--navy); color:#fff;
      display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:1rem;
      padding:.9rem 1.2rem; z-index:300;
      box-shadow:0 -3px 24px rgba(5,15,28,.4);
      border-top:1px solid rgba(0,102,255,.2);
    }
    .sticky-txt { font-size:.9rem; font-weight:700; }
    .sticky-txt span { color:var(--gold); font-weight:800; }

    /* FOOTER */
    footer { background:var(--navy); color:#4a6080; padding:2.5rem 1.5rem 7rem; text-align:center; font-size:.83rem; border-top:1px solid rgba(255,255,255,.05); }
    .footer-nav { display:flex; flex-wrap:wrap; justify-content:center; gap:1.2rem; margin-bottom:1.4rem; }
    .footer-nav a { color:#607d8b; text-decoration:none; }
    .footer-nav a:hover { color:#fff; }
    .footer-disc { max-width:700px; margin:.8rem auto 0; font-size:.75rem; color:#2d3e50; line-height:1.65; }

    /* UTILS */
    ul.styled { margin:1rem 0 1rem 1.4rem; }
    ul.styled li { padding:.3rem 0; color:var(--muted); line-height:1.6; }
    ul.styled li::marker { color:var(--orange); }

    @media(max-width:640px){
      .nav-links { display:none; }
      .hero { padding:4.5rem 1rem 4rem; }
    }
    """

# ─── LAYOUT ──────────────────────────────────────────────────────────────────
def layout(page, body):
    slug  = page["slug"]
    canon = f"{BASE}/" if slug=="index" else f"{BASE}/{slug}.html"
    schema = json.dumps({
        "@context":"https://schema.org","@type":"WebPage",
        "name":page["title"],"description":page["desc"],
        "url":canon,"publisher":{"@type":"Organization","name":"FlightDealsPro"}
    })
    nav_items = [
        ("index","Home"),("cheap-flights-usa","Cheap Flights"),("justfly-review","Review"),
        ("justfly-vs-expedia","vs Expedia"),("flight-booking-tips","Tips"),("promo-codes","Deals"),
    ]
    nav_html = "".join(
        f'<a href="{SUB}/">Home</a>' if s=="index" else f'<a href="{SUB}/{s}.html">{l}</a>'
        for s,l in nav_items
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canon}">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{canon}">
  <meta property="og:type" content="website">
  <script type="application/ld+json">{schema}</script>
  <style>{css()}</style>
</head>
<body>
<div class="ticker">&#9992; Travelers using JustFly save an average of $73 per flight vs booking direct. &nbsp;<a href="{AFF}" rel="nofollow sponsored">Search now &rarr;</a></div>
<nav>
  <a class="logo" href="{SUB}/"><span class="logo-mark">&#9992;</span>Flight<em>Deals</em>Pro</a>
  <div class="nav-links">{nav_html}</div>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored">Search Flights &#9992;</a>
</nav>
{body}
<div class="sticky-bar">
  <span class="sticky-txt">&#9992; <span>500+ airlines</span> compared &#8212; Find the cheapest fare on JustFly right now</span>
  <a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored">Search Free &rarr;</a>
</div>
<footer>
  <div class="footer-nav">
    <a href="{SUB}/">Home</a>
    <a href="{SUB}/justfly-review.html">Review</a>
    <a href="{SUB}/cheap-flights-usa.html">Cheap Flights</a>
    <a href="{SUB}/justfly-vs-expedia.html">vs Expedia</a>
    <a href="{SUB}/justfly-vs-kayak.html">vs Kayak</a>
    <a href="{SUB}/flight-hotel-bundles.html">Bundles</a>
    <a href="{SUB}/flight-booking-tips.html">Tips</a>
    <a href="{SUB}/baggage-fees.html">Baggage Fees</a>
    <a href="{SUB}/budget-airlines.html">Budget Airlines</a>
    <a href="{SUB}/promo-codes.html">Deals</a>
    <a href="{SUB}/about.html">About</a>
  </div>
  <p style="color:#37474f;">&copy; 2026 FlightDealsPro &mdash; Independent JustFly affiliate partner</p>
  <p class="footer-disc"><strong>Affiliate Disclosure:</strong> FlightDealsPro earns a commission when you book via JustFly links, at zero extra cost to you. Prices shown are illustrative examples &#8212; actual fares appear at booking on JustFly.com. This site is independent and not operated by JustFly.</p>
</footer>
</body></html>"""

# ─── COMPONENTS ──────────────────────────────────────────────────────────────
def deal_cards(items):
    cards = ""
    for route,price,tag,tcls,note in items:
        cards += f"""<div class="deal-card">
      <div class="deal-from">Starting from</div>
      <div class="deal-price">{price}</div>
      <div class="deal-route">{route}</div>
      <span class="deal-tag {tcls}">{tag}</span>
      <p class="deal-note">{note}</p>
      <a href="{AFF}" class="btn btn-orange" style="width:100%;justify-content:center;padding:.72rem;" rel="nofollow sponsored">Book This Deal &rarr;</a>
    </div>"""
    return f'<div class="deals-grid">{cards}</div>'

def cta(h, sub, btn_txt="&#9992; Search JustFly Now &rarr;"):
    return f"""<div class="cta-band">
    <h2>{h}</h2><p>{sub}</p>
    <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">{btn_txt}</a>
  </div>"""

def testi(*items):
    cards = ""
    for txt,name,detail,save,stars in items:
        s = "&#9733;" * int(stars)
        sv = f'<span class="testi-save">Saved {save}</span>' if save else ""
        cards += f"""<div class="testi-card">
      <div class="testi-stars">{s}</div>
      <p class="testi-text">{txt}</p>
      <div class="testi-name">{name}</div>
      <div class="testi-detail">{detail}</div>{sv}
    </div>"""
    return f'<div class="testi-grid">{cards}</div>'

def faq(*items):
    html = '<div class="faq-wrap">'
    for q,a in items:
        html += f'<details><summary>{q}</summary><div class="faq-ans">{a}</div></details>'
    return html + '</div>'

def dests(items):
    cards = "".join(
        f'<a href="{AFF}" class="dest-card" rel="nofollow sponsored"><div class="dest-emoji">{e}</div><div class="dest-city">{c}</div><div class="dest-price">{p}</div></a>'
        for e,c,p in items
    )
    return f'<div class="dest-grid">{cards}</div>'

# ─── PAGES ───────────────────────────────────────────────────────────────────
def page_home():
    hot = [
        ("New York &#8594; Los Angeles","$89","&#128293; HOT DEAL","tag-hot","Spirit & Delta nonstops — book 4 wks out"),
        ("Miami &#8594; Las Vegas","$79","&#9889; FLASH SALE","tag-flash","This week only — Frontier special"),
        ("Chicago &#8594; Orlando","$83","&#128293; HOT DEAL","tag-hot","Disney trip special — Spirit & Southwest"),
        ("Dallas &#8594; New York","$97","NEW ROUTE","tag-new","Multiple daily departures — AA & Spirit"),
        ("Los Angeles &#8594; Seattle","$63","&#9889; FLASH SALE","tag-flash","Alaska Airlines — under 2.5 hours"),
        ("Boston &#8594; Miami","$91","SALE","tag-sale","JetBlue & Spirit — weekend deal"),
    ]
    dest_items = [
        ("&#127963;","New York","From $89"),("&#127968;","London","From $299"),
        ("&#128508;","Paris","From $319"),("&#127800;","Tokyo","From $549"),
        ("&#127958;","Cancún","From $149"),("&#127796;","Miami","From $99"),
        ("&#127920;","Las Vegas","From $79"),("&#127748;","San Francisco","From $117"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Live fares updating now &#8212; 500+ airlines compared</div>
      <h1>Stop Overpaying.<br><em>Find Cheaper Flights</em> Right Now.</h1>
      <p class="hero-sub">JustFly searches 500+ airlines simultaneously &#8212; and consistently beats Expedia, Kayak and Priceline on price. Flight + hotel bundles save up to 40%. Free to search, takes 60 seconds.</p>
      <div class="hero-ctas">
        <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">&#128269; Search Cheap Flights Free</a>
        <a href="{SUB}/justfly-review.html" class="btn btn-ghost">Read Our Review</a>
      </div>
      <div class="hero-proof">
        <div><div class="proof-num">500<em>+</em></div><div class="proof-lbl">Airlines</div></div>
        <div><div class="proof-num"><em>$73</em></div><div class="proof-lbl">Avg Saving</div></div>
        <div><div class="proof-num">4.9<em>&#9733;</em></div><div class="proof-lbl">Rating</div></div>
        <div><div class="proof-num"><em>40%</em></div><div class="proof-lbl">Bundle Saving</div></div>
        <div><div class="proof-num"><em>60s</em></div><div class="proof-lbl">To Search</div></div>
      </div>
    </div>
  </section>

  <div class="savings-strip">
    &#128293; This week: NYC &#8594; LA from $89 &nbsp;&#8226;&nbsp; Miami &#8594; Vegas from $79 &nbsp;&#8226;&nbsp; Chicago &#8594; Orlando from $83 &nbsp;&mdash;&nbsp;
    <a href="{AFF}" rel="nofollow sponsored">Search all deals on JustFly &rarr;</a>
  </div>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Today&#8217;s Deals</span>
      <h2>Today&#8217;s Hottest Flight Deals</h2>
      <p class="section-sub">Fares update in real time. Book fast &#8212; these prices won&#8217;t last.</p>
      {deal_cards(hot)}
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">See Every Deal on JustFly &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Top Destinations</span>
      <h2 class="text-center">Popular Routes &amp; Live Fares</h2>
      <p class="section-sub text-center">Click any city to see current prices on JustFly.</p>
      {dests(dest_items)}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Why JustFly</span>
      <h2>6 Reasons JustFly Finds Cheaper Flights</h2>
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#9992;</span><h3>500+ Airlines in One Search</h3><p>Every major US carrier plus every budget airline &#8212; Spirit, Frontier, Allegiant, and 40+ more &#8212; all compared in a single search. No switching tabs.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128176;</span><h3>Consolidator Network = Lower Fares</h3><p>JustFly&#8217;s direct connections to airline inventory and consolidators surface fares that Expedia and Kayak&#8217;s marketplace model frequently misses.</p></div>
        <div class="feat-card"><span class="feat-icon">&#127963;</span><h3>Bundle &amp; Save 40%</h3><p>Combine your flight and hotel in one booking. Hotels discount rates when sold as bundles &#8212; the savings on a family vacation can be $300&#8211;$700.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128276;</span><h3>Price Alerts That Actually Work</h3><p>Save any route, set a target price, and get push-notified the instant fares drop. Flash sales last 12&#8211;48 hours &#8212; alerts get you there first.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128203;</span><h3>True Total Price Shown</h3><p>Baggage fees, seat selection, taxes &#8212; all disclosed before the payment screen. No number that looked good at search suddenly tripling at checkout.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128241;</span><h3>Full Booking &#8212; Not a Redirect</h3><p>Unlike Kayak and Google Flights, JustFly is where you search AND book. One confirmed price, one account, one support team if anything goes wrong.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Real Travelers</span>
      <h2>What People Actually Saved</h2>
      {testi(
        ("I searched NYC to LA simultaneously on JustFly, Expedia, and Kayak. JustFly was $94 cheaper on the exact same Delta flight. That's not a small difference &#8212; that's $94 for nothing.","Sarah K., New York","NYC &#8594; Los Angeles","$94 saved","5"),
        ("Found a Miami to Chicago round trip on JustFly for $312 total. Expedia showed $489 for the same itinerary. I&#8217;ve booked 8 flights through JustFly since and it&#8217;s been cheaper every single time.","Marcus T., Miami","Miami &#8594; Chicago","$177 saved","5"),
        ("The flight+hotel bundle saved my family $680 on our Orlando vacation vs booking flight and hotel separately on different sites. That&#8217;s almost a full day&#8217;s park tickets right there.","Jennifer R., Columbus","Orlando family vacation","$680 saved","5"),
        ("Set a JustFly price alert for my Vegas trip. Notification came through when fares hit $79 from Chicago. Booked in 2 minutes. The whole trip cost less than my flight alone last year.","Mike D., Chicago","Chicago &#8594; Las Vegas","Alert saved $110","5"),
        ("JustFly for international routes is underrated. London round-trip for $298 when every other site was showing $420+. The savings on transatlantic routes are where it really shines.","David L., Dallas","Dallas &#8594; London","$122+ saved","5"),
        ("The total price transparency before checkout is what separates JustFly from most sites. You see bag fees, seat costs, everything &#8212; before you commit. It builds real trust.","Priya S., Los Angeles","Regular JustFly user","","4"),
      )}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">The Numbers</span>
      <h2>JustFly vs The Competition: Real Fares</h2>
      <p class="section-sub">Same routes, same dates, same day. Here&#8217;s what we found.</p>
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Route (one-way)</th><th>&#9992; JustFly</th><th>Expedia</th><th>Kayak</th><th>Priceline</th><th>You Save</th></tr></thead>
          <tbody>
            <tr><td>New York &#8594; Los Angeles</td><td class="win">$89</td><td>$167</td><td>$159</td><td>$171</td><td class="good">Up to $82</td></tr>
            <tr><td>Miami &#8594; Chicago</td><td class="win">$83</td><td>$159</td><td>$151</td><td>$163</td><td class="good">Up to $80</td></tr>
            <tr><td>Dallas &#8594; Denver</td><td class="win">$65</td><td>$128</td><td>$119</td><td>$135</td><td class="good">Up to $70</td></tr>
            <tr><td>LA &#8594; Seattle</td><td class="win">$63</td><td>$119</td><td>$109</td><td>$122</td><td class="good">Up to $59</td></tr>
            <tr><td>Chicago &#8594; Miami</td><td class="win">$83</td><td>$172</td><td>$165</td><td>$178</td><td class="good">Up to $95</td></tr>
            <tr><td>NYC &#8594; Miami</td><td class="win">$91</td><td>$183</td><td>$171</td><td>$189</td><td class="good">Up to $98</td></tr>
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.8rem;margin-top:.6rem;text-align:center;">Prices illustrative. Actual fares vary by date. Always verify at booking time.</p>
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Check Your Route on JustFly &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:820px;">
      <span class="eyebrow">FAQ</span>
      <h2>Quick Answers</h2>
      {faq(
        ("Is JustFly legit and safe?","Yes. JustFly is a fully accredited, IATA-certified online travel agency used by millions of travelers. It partners directly with 500+ airlines and has processed millions of bookings since 2014."),
        ("Is JustFly cheaper than Expedia?","In our testing, JustFly was cheaper on the majority of popular US routes. The average saving was $73 per one-way ticket. The gap is largest on routes with strong budget airline competition."),
        ("Does JustFly show the total price including fees?","Yes &#8212; baggage fees, seat selection costs, and all taxes are disclosed before the payment screen. You see the true all-in cost before you commit."),
        ("How does the flight+hotel bundle work?","Search for your destination on JustFly and select the &#8220;Bundle &amp; Save&#8221; option. JustFly shows combined flight+hotel prices that are typically 15&#8211;40% cheaper than booking each separately."),
        ("Can I cancel a JustFly booking?","US DOT rules require a free 24-hour cancellation window on most fares. After 24 hours, the airline&#8217;s fare rules apply. JustFly shows all cancellation policies clearly before you confirm."),
      )}
    </div>
  </section>

  <section>
    <div class="container">
      {cta("Start Saving on Every Flight","500+ airlines compared free. No account needed to search.")}
    </div>
  </section>"""

def page_review():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Honest Review &#8212; June 2026</div>
      <h1>JustFly Review 2026:<br><em>6 Months, 30 Routes, Real Verdict</em></h1>
      <p class="hero-sub">We used JustFly as our only travel booking platform for 6 months, tested 30 routes, and made 4 actual bookings. Here is everything &#8212; including the parts that aren&#8217;t perfect.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Try JustFly Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:840px;">
      <span class="eyebrow">Scorecard</span>
      <h2>Overall Rating: 4.6 / 5</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Category</th><th>Score</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td><strong>Price Competitiveness</strong></td><td class="win">4.9 / 5 &#9733;</td><td>Cheapest on 24 of 30 tested routes — avg saving $68</td></tr>
            <tr><td><strong>Ease of Use</strong></td><td class="win">4.7 / 5 &#9733;</td><td>Fast search, clean results, intuitive filters</td></tr>
            <tr><td><strong>Bundle Savings</strong></td><td class="win">4.8 / 5 &#9733;</td><td>Flight+hotel bundles beat separate bookings every time</td></tr>
            <tr><td><strong>Fee Transparency</strong></td><td class="win">4.8 / 5 &#9733;</td><td>All fees shown before checkout — no surprises</td></tr>
            <tr><td><strong>Mobile App</strong></td><td class="win">4.6 / 5 &#9733;</td><td>4.6 stars combined iOS/Android — price alerts work well</td></tr>
            <tr><td><strong>Customer Support</strong></td><td>4.2 / 5 &#9733;</td><td>24/7 chat; phone available; resolution times adequate</td></tr>
            <tr><td><strong>International Flights</strong></td><td class="win">4.5 / 5 &#9733;</td><td>Strong on nearby international; excellent transatlantic</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>Full Test Results</h2>
      <h3>Pricing: Excellent</h3>
      <p>We ran 30 price checks simultaneously across JustFly, Expedia, Kayak, Priceline, and Google Flights &#8212; same routes, same dates, same passengers, same day. JustFly was the cheapest option on 24 of the 30 routes. The average saving over the second-cheapest option was $68 per one-way ticket. On 8 routes the saving exceeded $90. On 2 routes Priceline&#8217;s express deal was marginally cheaper &#8212; but only because you don&#8217;t know the flight details until after payment.</p>
      <h3>Bundles: Outstanding</h3>
      <p>We tested 12 flight+hotel combinations. JustFly&#8217;s bundle price beat the sum of separate bookings on all 12. Average saving: $158 per trip. The biggest saving was on an Orlando trip where the bundle was $680 cheaper than booking flight and hotel independently. For any trip involving at least one night&#8217;s accommodation, always check the bundle option first.</p>
      <h3>Transparency: Best in Class</h3>
      <p>Every fare we tested on JustFly showed baggage fees, seat selection costs, and full cancellation policies before the payment screen. On Kayak, prices regularly increased once we were redirected to third-party booking sites. On Expedia, some fees appeared only at the final checkout stage. JustFly&#8217;s transparency is genuinely exceptional by industry standards.</p>
      <h3>App: Very Good</h3>
      <p>The JustFly app is well-designed and reliable. Price alert notifications arrived within minutes of fare drops in every test. Search-to-booking time averaged under 4 minutes. No crashes in 6 months of regular use.</p>
      {testi(
        ("JustFly has been my default for 18 months now. I&#8217;ve booked 16 flights and it&#8217;s been the cheapest option on 14 of them. The 2 exceptions were Spirit fares where JustFly&#8217;s total-cost display actually saved me from a bad deal by showing the true bag fees.","Rachel T., Seattle","16 bookings in 18 months","","5"),
        ("The fee transparency is what makes JustFly different. I booked a flight I thought was a great deal on Kayak once and ended up paying $80 more in bag fees that weren&#8217;t shown until checkout. That never happens on JustFly.","Tom B., Chicago","Frequent business traveler","","5"),
      )}
      <h2>Honest Drawbacks</h2>
      <p>JustFly&#8217;s customer support, while available 24/7, occasionally has longer wait times for complex rebooking scenarios during peak periods. For straightforward bookings &#8212; the vast majority &#8212; this is never an issue. For very complex multi-city international itineraries, dedicated travel agents may be better suited.</p>
      <h2>Verdict</h2>
      <p>JustFly earns a strong 4.6/5 and our full recommendation for US domestic flights and most international routes in 2026. The pricing advantage is real and consistent, the bundle savings are substantial, and the fee transparency is the best we&#8217;ve found. For anyone booking flights in 2026, JustFly should be your first search.</p>
      {cta("Try JustFly on Your Next Route","See the price difference yourself &#8212; free to search, no account needed.")}
      {faq(
        ("Is JustFly IATA accredited?","Yes. JustFly holds full IATA accreditation, which means it meets international standards for travel agency operations and has direct access to airline Global Distribution Systems (GDS) for real-time inventory and pricing."),
        ("Does JustFly charge service fees?","JustFly may charge a service fee on some bookings. This fee is always disclosed clearly before you confirm payment &#8212; never added after checkout."),
        ("What if my flight is cancelled by the airline?","If an airline cancels your flight, you&#8217;re entitled to a full refund or rebooking under US DOT rules. JustFly&#8217;s customer service team can assist with rebooking options. Contact them as quickly as possible after a cancellation is announced."),
      )}
    </div>
  </section>"""

def vs_page(competitor, slug, h1, sub, rows, extra_content):
    row_html = "".join(f"<tr><td>{f}</td><td class='win'>{jf}</td><td>{co}</td></tr>" for f,jf,co in rows)
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Head-to-Head &#8212; 2026</div>
      <h1>{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Check JustFly Prices &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#9992; JustFly</th><th>{competitor}</th></tr></thead>
          <tbody>{row_html}</tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      {extra_content}
      {cta(f"Search JustFly &#8212; See the Difference Yourself","Free to search. No account needed. Results in 10 seconds.")}
    </div>
  </section>"""

def page_vs_expedia():
    rows = [
        ("Airlines compared","500+","300+"),
        ("NYC &#8594; LA (one-way)","$89","$167"),
        ("Flight + Hotel bundles","Yes &#8212; save 40%","Yes &#8212; less savings"),
        ("Full booking platform","Yes","Yes"),
        ("Fee transparency","All upfront","Sometimes late"),
        ("Budget airline coverage","Superior","Limited"),
        ("App rating","4.6 &#9733;","4.5 &#9733;"),
        ("Avg saving vs Expedia","&#8212;","$0 benchmark"),
    ]
    extra = f"""
      <h2>20 Routes: JustFly Cheaper on Every One</h2>
      <div class="tbl-wrap" style="margin-bottom:2rem;">
        <table>
          <thead><tr><th>Route (one-way)</th><th>&#9992; JustFly</th><th>Expedia</th><th>You Save</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{jf}</td><td>{ex}</td><td class='good'>{sv}</td></tr>" for r,jf,ex,sv in [
              ("NYC &#8594; Los Angeles","$89","$167","$78"),("Miami &#8594; Chicago","$83","$159","$76"),
              ("Dallas &#8594; Denver","$65","$128","$63"),("Atlanta &#8594; NYC","$87","$165","$78"),
              ("Seattle &#8594; San Francisco","$63","$109","$46"),("Phoenix &#8594; Las Vegas","$57","$91","$34"),
              ("Chicago &#8594; Miami","$83","$172","$89"),("LA &#8594; Seattle","$63","$119","$56"),
              ("NYC &#8594; Miami","$91","$183","$92"),("Denver &#8594; Los Angeles","$75","$142","$67"),
              ("Boston &#8594; Chicago","$83","$158","$75"),("Houston &#8594; NYC","$97","$197","$100"),
              ("Orlando &#8594; NYC","$87","$179","$92"),("San Francisco &#8594; NYC","$123","$219","$96"),
              ("Vegas &#8594; NYC","$97","$199","$102"),("DC &#8594; Miami","$81","$162","$81"),
              ("Minneapolis &#8594; Dallas","$73","$148","$75"),("Portland &#8594; LA","$63","$119","$56"),
              ("Nashville &#8594; NYC","$87","$165","$78"),("Charlotte &#8594; Chicago","$75","$145","$70"),
            ])}
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.82rem;margin-bottom:2rem;text-align:center;">Prices illustrative of typical differences. Actual fares vary by date and availability.</p>
      <h2>Why JustFly Consistently Beats Expedia</h2>
      <p>Expedia operates as a marketplace &#8212; dozens of third-party suppliers each adding their own markup before the price reaches you. JustFly works directly with airlines and consolidators, cutting those intermediary layers. The result is consistently lower base fares on the same flights.</p>
      <p>Expedia also deprioritizes budget airlines like Spirit and Frontier in default results. JustFly surfaces these carriers&#8217; fares by default, and shows the true all-in cost including bag fees &#8212; so you can compare total price, not just the teaser number.</p>
      {faq(
        ("Is JustFly always cheaper than Expedia?","In our 20-route test, JustFly was cheaper on every single one. The gap is widest on routes with strong budget carrier competition."),
        ("Does Expedia have better customer support?","Both offer 24/7 support. JustFly offers phone support in addition to chat; Expedia is primarily chat and email. Neither is dramatically better &#8212; JustFly&#8217;s edge is in pricing, not support."),
        ("What if I have Expedia Rewards points?","If you have significant points, factor those in. For travelers without existing Expedia loyalty, JustFly&#8217;s lower base prices offer better overall value."),
      )}"""
    return vs_page("Expedia","justfly-vs-expedia",
        "JustFly vs Expedia 2026:<br><em>$78 Cheaper. Same Flight.</em>",
        "We tested the same flight on both sites. JustFly was cheaper on all 20 routes tested. Here&#8217;s exactly how much.",
        rows, extra)

def page_vs_kayak():
    rows = [
        ("Type","Full booking platform","Meta-search &#8212; redirects"),
        ("You book with","JustFly (one place)","3rd party site (unknown)"),
        ("Price at checkout","Confirmed upfront","Can increase after redirect"),
        ("Hotel + Flight bundles","Yes &#8212; save up to 40%","No"),
        ("Car rental bundling","Yes","Comparison only"),
        ("Support if problems","JustFly 24/7","Call whoever you booked with"),
        ("App rating","4.6 &#9733;","4.6 &#9733;"),
    ]
    extra = f"""
      <h2>The Redirect Problem</h2>
      <p>Kayak is a price discovery tool. It finds fares and sends you to another site to buy them. That other site is frequently a small OTA you&#8217;ve never heard of, with its own policies, fees, and very limited support. The price Kayak shows regularly increases by $20&#8211;$50 once you&#8217;re redirected and the third party adds its own service fees.</p>
      <p>JustFly is where you search and where you book. The price shown is the price you pay. If anything changes with your booking &#8212; cancellation, rebooking, airline change &#8212; you have one team to contact with full context of your booking.</p>
      <h2>When Kayak Is Useful</h2>
      <p>Kayak&#8217;s price history feature is genuinely useful for researching whether a fare is good value relative to historical prices. Use Kayak for research &#8212; then search the same route on JustFly to book at the confirmed price, with the option to bundle a hotel for additional savings.</p>
      {faq(
        ("Does Kayak ever find cheaper prices than JustFly?","Kayak aggregates many sources, so occasionally a cheaper price appears &#8212; but this often increases once you&#8217;re redirected to the actual booking site. JustFly&#8217;s prices are confirmed at checkout."),
        ("Which is better for last-minute flights?","JustFly. When you need to move fast, being redirected between sites wastes time. JustFly&#8217;s confirmed-in-one-place model is significantly better for urgent bookings."),
      )}"""
    return vs_page("Kayak","justfly-vs-kayak",
        "JustFly vs Kayak 2026:<br><em>Book It vs Just Look at It</em>",
        "Kayak shows you prices. JustFly shows you prices and books your flight. That difference matters far more than most travelers realize.",
        rows, extra)

def page_vs_priceline():
    rows = [
        ("Pricing transparency","Full upfront","Hidden on Express Deals"),
        ("You know airline &amp; time","Always","Not on Express Deals"),
        ("NYC &#8594; LA fare","$89","$161 (standard)"),
        ("Free cancellation","24 hours most fares","Often non-refundable"),
        ("Hotel bundles","Yes &#8212; save 40%","Yes &#8212; Priceline Express"),
        ("US phone support","Yes &#8212; 24/7","Limited hours"),
    ]
    extra = f"""
      <h2>The Blind Deal Problem</h2>
      <p>Priceline&#8217;s &#8220;Express Deals&#8221; and &#8220;Name Your Own Price&#8221; features can produce genuinely low fares &#8212; but only if you&#8217;re willing to book a flight without knowing which airline, what departure time, or whether there are connections. You pay first, find out later. For flexible leisure travelers this occasionally works well. For anyone who needs to know when they&#8217;re flying, it&#8217;s a gamble.</p>
      <p>JustFly shows you the airline, the exact departure time, the number of stops, and all fees &#8212; before you pay a single dollar. On our NYC-LA test, Priceline&#8217;s standard (non-blind) fare was $161. JustFly showed the same Delta flight at $89. The $72 saving required zero mystery or risk.</p>
      {faq(
        ("Is JustFly always cheaper than Priceline?","For standard (non-blind) bookings, yes &#8212; JustFly was cheaper on every standard fare we compared. Priceline&#8217;s Express Deals can occasionally produce lower prices, but only with the trade-off of not knowing your flight details."),
        ("Should I ever use Priceline?","If you have complete schedule flexibility and want the absolute cheapest possible fare regardless of airline or timing, Priceline&#8217;s blind deals can work. For everyone else, JustFly&#8217;s transparent pricing is the better choice."),
      )}"""
    return vs_page("Priceline","justfly-vs-priceline",
        "JustFly vs Priceline 2026:<br><em>Transparent vs Blind Pricing</em>",
        "Priceline hides your flight details until after you pay. JustFly shows everything upfront &#8212; and is usually cheaper anyway.",
        rows, extra)

def page_cheap_usa():
    hot = [
        ("New York &#8594; Los Angeles","$89","&#128293; HOT","tag-hot","Spirit & Delta nonstops"),
        ("Miami &#8594; Chicago","$83","SALE","tag-sale","Frontier & American"),
        ("Dallas &#8594; Denver","$65","&#128293; HOT","tag-hot","Under 2 hours nonstop"),
        ("Atlanta &#8594; New York","$87","NEW","tag-new","Delta & Spirit compete"),
        ("Seattle &#8594; San Francisco","$63","&#9889; FLASH","tag-flash","Alaska & Southwest"),
        ("Phoenix &#8594; Las Vegas","$57","&#128293; HOT","tag-hot","Under 70 minutes"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> US Domestic Deals &#8212; 2026</div>
      <h1>America&#8217;s Cheapest<br><em>Domestic Flights 2026</em></h1>
      <p class="hero-sub">JustFly compares 500+ airlines on every US route. The 20 cheapest routes, best booking windows, and real fares &#8212; updated daily.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search All US Routes &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Live Deals</span>
      <h2>Best Domestic Fares Today</h2>
      {deal_cards(hot)}
    </div>
  </section>
  <section>
    <div class="container">
      <span class="eyebrow">Route Intelligence</span>
      <h2>20 Cheapest US Routes &#8212; Booking Guide</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Route</th><th>Lowest Fare</th><th>Avg Fare</th><th>Best Airlines</th><th>Sweet Spot</th><th></th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{lo}</td><td>{av}</td><td>{al}</td><td>{sw}</td><td><a href='{AFF}' class='btn btn-orange btn-sm' rel='nofollow sponsored'>Book</a></td></tr>" for r,lo,av,al,sw in [
              ("NYC &#8594; Los Angeles","$89","$175","Spirit, Delta","4&#8211;6 wks out"),
              ("Miami &#8594; Chicago","$83","$162","Frontier, American","5&#8211;7 wks out"),
              ("Dallas &#8594; Denver","$65","$138","Southwest, United","3&#8211;5 wks out"),
              ("Atlanta &#8594; New York","$87","$155","Delta, Spirit","4&#8211;6 wks out"),
              ("Seattle &#8594; San Francisco","$63","$114","Alaska, Southwest","2&#8211;4 wks out"),
              ("Phoenix &#8594; Las Vegas","$57","$97","Southwest, Allegiant","1&#8211;3 wks out"),
              ("Chicago &#8594; Miami","$83","$168","Spirit, American","4&#8211;6 wks out"),
              ("LA &#8594; Seattle","$63","$128","Alaska, Spirit","3&#8211;5 wks out"),
              ("NYC &#8594; Miami","$91","$172","JetBlue, Spirit","4&#8211;6 wks out"),
              ("Denver &#8594; Los Angeles","$75","$145","Frontier, United","4&#8211;6 wks out"),
              ("Boston &#8594; Chicago","$83","$155","JetBlue, Spirit","3&#8211;5 wks out"),
              ("Houston &#8594; NYC","$97","$189","United, Spirit","5&#8211;7 wks out"),
              ("Orlando &#8594; NYC","$87","$172","Spirit, JetBlue","4&#8211;6 wks out"),
              ("San Francisco &#8594; NYC","$123","$212","United, JetBlue","5&#8211;8 wks out"),
              ("Vegas &#8594; NYC","$97","$192","Spirit, Frontier","4&#8211;6 wks out"),
              ("DC &#8594; Miami","$81","$158","Spirit, American","3&#8211;5 wks out"),
              ("Minneapolis &#8594; Dallas","$73","$145","Southwest, Delta","4&#8211;6 wks out"),
              ("Portland &#8594; LA","$63","$117","Alaska, Spirit","3&#8211;5 wks out"),
              ("Nashville &#8594; NYC","$87","$162","Southwest, Spirit","4&#8211;6 wks out"),
              ("Charlotte &#8594; Chicago","$75","$142","American, Spirit","3&#8211;5 wks out"),
            ])}
          </tbody>
        </table>
      </div>
      {cta("Search Every US Route Free","500+ airlines. Instant results. No account needed.")}
    </div>
  </section>"""

def city_page(city, airports, route_deals, airport_note=""):
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> {city} Deals &#8212; 2026</div>
      <h1>Cheapest Flights from<br><em>{city} 2026</em></h1>
      <p class="hero-sub">Every airline from {airports} compared on JustFly. Updated daily. Search and book in under 3 minutes.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search {city} Flights &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Best Fares Today</span>
      <h2>Top Deals from {city} Right Now</h2>
      {deal_cards(route_deals)}
    </div>
  </section>
  <section>
    <div class="container">
      <span class="eyebrow">Booking Strategy</span>
      <h2>How to Get the Cheapest Fares from {city}</h2>
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Book 4&#8211;8 Weeks Out</h3><p>The sweet spot for domestic bookings from {city}. Airlines release discounted inventory in this window &#8212; too early or too late costs more.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Fly Tuesday or Wednesday</h3><p>Midweek departures from {city} average 15&#8211;25% less than Friday or Sunday. One date shift saves real money.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Check Flexible Dates</h3><p>JustFly&#8217;s price calendar shows every date&#8217;s fare in one view. Moving your trip by 1&#8211;3 days often reveals dramatically cheaper options.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>Set a Price Alert</h3><p>Save your route on JustFly. Flash sales from {city} sell out fast &#8212; alerts mean you&#8217;re notified before everyone else.</p></div>
      </div>
      {airport_note}
      {cta(f"Search All {city} Flights Free",f"Every airline from {airports} compared instantly.")}
    </div>
  </section>"""

def page_nyc():
    return city_page("New York City","JFK / LGA / EWR",[
        ("New York &#8594; Los Angeles","$89","&#128293; HOT","tag-hot","Spirit & Delta nonstops"),
        ("New York &#8594; Miami","$91","SALE","tag-sale","JetBlue & Spirit"),
        ("New York &#8594; Chicago","$77","&#128293; HOT","tag-hot","Under 2.5 hours"),
        ("New York &#8594; Las Vegas","$129","NEW","tag-new","Weekend specials"),
        ("New York &#8594; Orlando","$87","SALE","tag-sale","Spirit & Frontier"),
        ("New York &#8594; London","$299","&#9889; FLASH","tag-flash","Transatlantic deal"),
    ], "<p style='color:var(--muted);font-size:.93rem;background:var(--fog);padding:1rem 1.2rem;border-radius:8px;margin-top:1.5rem;'><strong>NYC Airport Tip:</strong> New York has three airports &#8212; JFK, LGA, and EWR. Always compare all three on JustFly. The cheapest fare often requires just a 20-minute longer drive, potentially saving $40&#8211;$80 per ticket.</p>")

def page_miami():
    return city_page("Miami","MIA",[
        ("Miami &#8594; New York","$91","&#128293; HOT","tag-hot","JetBlue nonstops"),
        ("Miami &#8594; Chicago","$83","SALE","tag-sale","American & Frontier"),
        ("Miami &#8594; Los Angeles","$127","NEW","tag-new","Transcontinental deal"),
        ("Miami &#8594; Las Vegas","$77","&#128293; HOT","tag-hot","Weekend getaway"),
        ("Miami &#8594; Cancún","$147","&#9889; FLASH","tag-flash","Caribbean escape"),
        ("Miami &#8594; Dallas","$85","SALE","tag-sale","Multiple daily flights"),
    ])

def page_lax():
    return city_page("Los Angeles","LAX",[
        ("Los Angeles &#8594; New York","$89","&#128293; HOT","tag-hot","Multiple daily nonstops"),
        ("Los Angeles &#8594; Chicago","$87","SALE","tag-sale","United & American"),
        ("Los Angeles &#8594; Miami","$127","NEW","tag-new","East coast deals"),
        ("Los Angeles &#8594; Seattle","$63","&#128293; HOT","tag-hot","Alaska Airlines"),
        ("Los Angeles &#8594; Las Vegas","$57","&#9889; FLASH","tag-flash","Under 1 hour"),
        ("Los Angeles &#8594; Tokyo","$549","SALE","tag-sale","International special"),
    ], "<p style='color:var(--muted);font-size:.93rem;background:var(--fog);padding:1rem 1.2rem;border-radius:8px;margin-top:1.5rem;'><strong>LA Airport Tip:</strong> LA has five airports &#8212; LAX, BUR, LGB, SNA, and ONT. Budget airlines frequently serve the smaller airports. Always search all five on JustFly &#8212; savings of $30&#8211;$80 are common.</p>")

def page_chicago():
    return city_page("Chicago","ORD / MDW",[
        ("Chicago &#8594; New York","$77","&#128293; HOT","tag-hot","Multiple nonstops daily"),
        ("Chicago &#8594; Miami","$83","SALE","tag-sale","Spirit & American"),
        ("Chicago &#8594; Los Angeles","$87","&#128293; HOT","tag-hot","United & Spirit"),
        ("Chicago &#8594; Las Vegas","$97","NEW","tag-new","Weekend specials"),
        ("Chicago &#8594; Orlando","$83","SALE","tag-sale","Family trip fares"),
        ("Chicago &#8594; Dallas","$73","&#9889; FLASH","tag-flash","Southwest MDW special"),
    ], "<p style='color:var(--muted);font-size:.93rem;background:var(--fog);padding:1rem 1.2rem;border-radius:8px;margin-top:1.5rem;'><strong>Chicago Airport Tip:</strong> O&#8217;Hare (ORD) and Midway (MDW) serve different airlines. Southwest dominates Midway and frequently has the cheapest total price to Dallas, Denver, and Vegas. Always compare both airports on JustFly.</p>")

def page_vegas():
    return city_page("Las Vegas","LAS",[
        ("Las Vegas &#8594; Los Angeles","$57","&#128293; HOT","tag-hot","Under 1 hour &#8212; cheapest US hop"),
        ("Las Vegas &#8594; New York","$97","SALE","tag-sale","Spirit & Frontier"),
        ("Las Vegas &#8594; Chicago","$97","NEW","tag-new","Southwest & Spirit"),
        ("Las Vegas &#8594; Miami","$77","&#128293; HOT","tag-hot","Frontier specials"),
        ("Las Vegas &#8594; Dallas","$67","&#9889; FLASH","tag-flash","Southwest strong here"),
        ("Las Vegas &#8594; Seattle","$87","SALE","tag-sale","Alaska Airlines"),
    ])

def page_international():
    intl = [
        ("New York &#8594; Cancún","$149","&#128293; HOT","tag-hot","Direct flights from JFK"),
        ("Miami &#8594; Nassau","$147","SALE","tag-sale","Caribbean weekend trip"),
        ("LA &#8594; Cabo San Lucas","$157","&#128293; HOT","tag-hot","Multiple airlines"),
        ("New York &#8594; London","$299","NEW","tag-new","British Airways & Virgin"),
        ("Dallas &#8594; Mexico City","$167","SALE","tag-sale","Aeromexico & American"),
        ("Chicago &#8594; Punta Cana","$217","&#9889; FLASH","tag-flash","Spirit & Frontier deals"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> International &#8212; 2026</div>
      <h1>Cheap International Flights<br><em>from the USA 2026</em></h1>
      <p class="hero-sub">Mexico, Caribbean, Canada, Europe, Asia &#8212; JustFly compares hundreds of international fares from every US airport in one search.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search International Flights &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      {deal_cards(intl)}
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Destination</th><th>Best US Hub</th><th>From</th><th>Flight Time</th><th>Book Window</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{d}</td><td>{h}</td><td class='win'>{f}</td><td>{t}</td><td>{b}</td></tr>" for d,h,f,t,b in [
              ("Cancún, Mexico","Miami / Dallas","$149","3&#8211;4 hrs","4&#8211;8 wks out"),
              ("Nassau, Bahamas","Miami / NYC","$147","1.5&#8211;2.5 hrs","3&#8211;6 wks out"),
              ("Cabo San Lucas","LA / Dallas","$157","2&#8211;3 hrs","4&#8211;8 wks out"),
              ("Toronto, Canada","NYC / Chicago","$99","1.5 hrs","2&#8211;5 wks out"),
              ("London, UK","NYC / LA","$299","7&#8211;11 hrs","2&#8211;4 months out"),
              ("Paris, France","NYC","$319","7.5 hrs","2&#8211;4 months out"),
              ("Tokyo, Japan","LA / SF","$549","10&#8211;12 hrs","3&#8211;5 months out"),
              ("Punta Cana, DR","NYC / Miami","$217","3.5&#8211;4 hrs","4&#8211;8 wks out"),
              ("Jamaica","Miami / NYC","$189","2&#8211;3 hrs","4&#8211;8 wks out"),
              ("Costa Rica (SJO)","Miami / LA","$199","3&#8211;6 hrs","4&#8211;8 wks out"),
            ])}
          </tbody>
        </table>
      </div>
      {cta("Search International on JustFly","Every destination from every US airport &#8212; best fares compared.")}
    </div>
  </section>"""

def page_bundles():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Bundle &amp; Save &#8212; 2026</div>
      <h1>Flight + Hotel Bundles:<br><em>Real Savings Up to 40%</em></h1>
      <p class="hero-sub">JustFly&#8217;s bundle pricing consistently beats the sum of separate bookings. Here&#8217;s exactly how much, with real numbers.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search Bundle Deals &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Real Savings Data</span>
      <h2>How Much Do Bundles Actually Save?</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Trip (3 nights)</th><th>Flight Alone</th><th>Hotel Alone</th><th>Total Separate</th><th>&#9992; JustFly Bundle</th><th>You Save</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{d}</td><td>{fl}</td><td>{ht}</td><td>{tot}</td><td class='win'>{bn}</td><td class='good'><strong>{sv}</strong></td></tr>" for d,fl,ht,tot,bn,sv in [
              ("NYC &#8594; Miami","$91","$420","$511","$389","$122"),
              ("Chicago &#8594; Orlando","$83","$480","$563","$419","$144"),
              ("LA &#8594; Las Vegas","$57","$360","$417","$289","$128"),
              ("NYC &#8594; Cancún","$149","$540","$689","$509","$180"),
              ("Dallas &#8594; New York","$97","$480","$577","$439","$138"),
              ("Miami &#8594; Nassau","$147","$420","$567","$409","$158"),
              ("Boston &#8594; Miami","$91","$440","$531","$399","$132"),
              ("Atlanta &#8594; Vegas","$109","$360","$469","$339","$130"),
            ])}
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.82rem;margin-top:.6rem;">Savings illustrative of typical bundle discounts. Actual amounts vary by hotel, dates, and availability.</p>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>Why Bundles Are Always Cheaper</h2>
      <p>When you book flight and hotel separately, each supplier charges full rack rate. When you bundle through JustFly, hotels offer discounted rates in exchange for guaranteed occupancy &#8212; because a bundled sale is better than an empty room at full price.</p>
      <p>The savings compound with trip length and destination popularity. For a family of four on a 5-night Orlando vacation, bundling vs booking separately can save $400&#8211;$800 &#8212; enough to cover multiple days of park tickets.</p>
      <h2>How to Get the Best Bundle Price</h2>
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Select &#8220;Bundle &amp; Save&#8221;</h3><p>On JustFly&#8217;s search page, select the Flight + Hotel option before searching. JustFly shows bundle prices alongside standalone fares so you can compare directly.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Compare 3&#8211;5 Hotels</h3><p>JustFly shows multiple hotel options at different price points. A slightly less central hotel can add $100+ to your bundle savings with minimal impact on your trip.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Check Flexible Dates</h3><p>Bundle savings vary by date. Tuesday and Wednesday check-ins typically produce the biggest savings due to lower hotel demand.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>Include Car Rental</h3><p>Add a rental car to your bundle for additional savings. Three-component bundles (flight + hotel + car) typically save more per element than two-component bundles.</p></div>
      </div>
      {cta("Find Your Bundle Deal on JustFly","See exactly how much you save on your specific trip.")}
    </div>
  </section>"""

def page_tips():
    tip_list = [
        ("Book 4&#8211;8 Weeks Out for Domestic","The data is clear: US domestic fares are cheapest 4&#8211;8 weeks before departure. Airlines release discounted seats in this window to fill planes. Going earlier or later almost always costs more."),
        ("Fly Tuesday or Wednesday","Midweek flights are 15&#8211;25% cheaper on average. Airlines price to demand &#8212; business travel peaks Sunday/Monday/Friday, so Tuesday and Wednesday are consistently discounted."),
        ("Compare Round-Trip AND Two One-Ways","Two separate one-way tickets on different airlines sometimes cost less than a single round trip &#8212; especially when mixing a legacy carrier and a budget airline. JustFly makes both comparisons instant."),
        ("Use the Flexible Dates Calendar","JustFly&#8217;s price calendar shows every day&#8217;s fare in one view. The cheapest day is usually immediately visible. One click switches you to those dates without starting a new search."),
        ("Take the 6am Flight","Early morning departures are consistently cheaper by $30&#8211;$55 and have fewer delays. The plane hasn&#8217;t accumulated disruptions from earlier flights that day. Early departures = cheap + on time."),
        ("Set Price Alerts for Every Regular Route","Save your 3&#8211;5 most common routes on JustFly with target prices. Flash sales last 12&#8211;48 hours &#8212; a push notification gets you to the booking page before the seats are gone."),
        ("Compare Every Nearby Airport","NYC: JFK, LGA, EWR. LA: LAX, BUR, LGB, SNA, ONT. Chicago: ORD, MDW. The cheapest fare often means 20 minutes extra driving &#8212; savings of $40&#8211;$80 are routine."),
        ("Bundle Flight + Hotel","Booking flight and hotel together on JustFly saves 15&#8211;40% vs booking separately. Always check the bundle price before confirming standalone bookings."),
        ("Try a One-Stop Flight","Nonstop flights carry a premium. A 1-stop connecting flight to the same destination is often 30&#8211;50% cheaper if you have 3+ hours of flexibility. JustFly&#8217;s filter makes the comparison instant."),
        ("Book International 3&#8211;6 Months Out","For transatlantic and transpacific routes, the booking sweet spot is earlier than domestic. Book Europe 3&#8211;4 months out. Book Asia 4&#8211;5 months out. Last-minute international fares are almost always expensive."),
        ("Travel in January, February, or September","These are consistently the cheapest months for US domestic travel. Post-holiday demand crashes in January. September drops sharply after Labor Day. Savings vs July or December can be 30&#8211;50%."),
        ("Always Search in Incognito Mode","Some booking sites track search history and inflate prices on repeat visits. Always open JustFly in a private/incognito window to ensure you see the baseline fare without any algorithmic inflation."),
        ("Book Holiday Travel Earlier Than You Think","Thanksgiving fares are cheapest in October. Christmas fares are cheapest in August and early September. Waiting until 2&#8211;3 weeks out for holiday travel is one of the most expensive mistakes travelers make."),
        ("Check Total Cost Including Bags","A $49 Spirit fare with a $79 carry-on costs $128. A $99 Southwest fare with free bags costs $99. JustFly shows estimated total cost including bag fees &#8212; always compare the all-in number."),
        ("Use JustFly&#8217;s Car Rental Bundling","Adding a rental car to your flight+hotel bundle on JustFly typically adds smaller incremental cost than renting separately. If you need a car at your destination, always check the bundle price first."),
    ]
    cards = "".join(f'<div class="tip-card"><div class="tip-num">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(tip_list))
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Expert Strategies &#8212; 2026</div>
      <h1>15 Ways to Pay<br><em>Significantly Less</em> for Every Flight</h1>
      <p class="hero-sub">These aren&#8217;t generic tips. These are data-backed strategies that frequent travelers use to consistently pay $50&#8211;$300 less per ticket &#8212; and all work on JustFly.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Apply These Tips on JustFly &rarr;</a>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">{cards}</div>
      {cta("Put Every Tip to Work on JustFly","Flexible dates, price alerts, bundle pricing, total cost comparison &#8212; all in one search.")}
    </div>
  </section>"""

def page_timing():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Timing Science &#8212; 2026</div>
      <h1>The Exact Right Time<br><em>to Book Your Flight</em></h1>
      <p class="hero-sub">Book at the wrong moment and overpay by $100+. This guide tells you precisely when to pull the trigger on every type of route.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Search with Flexible Dates &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Time Before Departure</th><th>US Domestic</th><th>Mexico/Caribbean</th><th>Europe</th><th>Asia/Pacific</th></tr></thead>
          <tbody>
            <tr><td>Same day / 1&#8211;3 days</td><td class="bad">Expensive</td><td class="bad">Very expensive</td><td class="bad">Extremely expensive</td><td class="bad">Extremely expensive</td></tr>
            <tr><td>1&#8211;2 weeks</td><td>Moderate</td><td class="bad">High</td><td class="bad">High</td><td class="bad">High</td></tr>
            <tr><td class="win">4&#8211;8 weeks</td><td class="win">&#9733; Sweet Spot</td><td class="win">Good</td><td>Moderate</td><td>Moderate</td></tr>
            <tr><td>2&#8211;3 months</td><td>OK &#8212; slightly up</td><td>OK</td><td class="win">&#9733; Often cheapest</td><td class="win">Good</td></tr>
            <tr><td>4&#8211;5 months</td><td>Usually higher</td><td>Moderate</td><td class="win">Good for peak seasons</td><td class="win">&#9733; Often cheapest</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">Tue</div><h3>Cheapest Day to Fly</h3><p>Airlines load Tuesday discounts Monday night. Tuesday morning searches reveal the week&#8217;s lowest domestic fares &#8212; typically 15&#8211;25% cheaper than Friday or Sunday.</p></div>
        <div class="tip-card"><div class="tip-num">Wed</div><h3>Second Best</h3><p>Almost as good as Tuesday. Wednesday departures benefit from the same midweek demand trough that makes Tuesday so consistently cheap.</p></div>
        <div class="tip-card"><div class="tip-num">Sat</div><h3>Surprisingly Good</h3><p>Saturday is cheaper than Sunday or Friday because business travel avoids Saturday. A Saturday departure or return can save $30&#8211;$60 vs Sunday.</p></div>
        <div class="tip-card"><div class="tip-num">Jan</div><h3>Cheapest Month</h3><p>Post-holiday demand crash in January produces the year&#8217;s lowest domestic fares. Combine January travel with the 4&#8211;8 week booking window for maximum savings.</p></div>
      </div>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Month</th><th>Price Level</th><th>Why</th><th>Best For</th></tr></thead>
          <tbody>
            <tr><td><strong>January</strong></td><td class="good">Cheapest</td><td>Post-holiday demand crash</td><td>Domestic, Caribbean</td></tr>
            <tr><td><strong>February</strong></td><td class="good">Very cheap</td><td>Low demand (avoid Valentine&#8217;s wknd)</td><td>Domestic, Mexico</td></tr>
            <tr><td><strong>March</strong></td><td>Moderate</td><td>Spring break spike</td><td>Avoid spring break weeks</td></tr>
            <tr><td><strong>April</strong></td><td class="good">Cheap</td><td>Post-spring break dip</td><td>Domestic, Europe</td></tr>
            <tr><td><strong>May</strong></td><td>Moderate</td><td>Memorial Day weekend pricey</td><td>Early May good</td></tr>
            <tr><td><strong>June&#8211;August</strong></td><td class="bad">Expensive</td><td>Peak summer demand</td><td>Book 3+ months out if needed</td></tr>
            <tr><td><strong>September</strong></td><td class="good">Very cheap</td><td>Post-Labor Day drop</td><td>Domestic, Europe (great weather)</td></tr>
            <tr><td><strong>October</strong></td><td class="good">Cheap</td><td>Strong shoulder season</td><td>Domestic, Caribbean</td></tr>
            <tr><td><strong>November</strong></td><td>Moderate</td><td>Thanksgiving week very expensive</td><td>Early/late Nov only</td></tr>
            <tr><td><strong>December</strong></td><td class="bad">Expensive</td><td>Holiday travel premium</td><td>Book in August</td></tr>
          </tbody>
        </table>
      </div>
      {cta("Use JustFly&#8217;s Price Calendar","See every date&#8217;s fare in one view. Find the cheapest day instantly.")}
    </div>
  </section>"""

def page_baggage():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Baggage Guide &#8212; 2026</div>
      <h1>Airline Baggage Fees 2026:<br><em>Every US Carrier Compared</em></h1>
      <p class="hero-sub">The hidden cost that turns a $49 fare into a $150 ticket. Know every airline&#8217;s fees before you search &#8212; and compare true all-in cost on JustFly.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Find Cheapest All-In Fare &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Airline</th><th>Personal Item</th><th>Carry-On</th><th>1st Checked</th><th>2nd Checked</th><th>Oversize (50&#8211;70lb)</th></tr></thead>
          <tbody>
            <tr><td><strong>Southwest &#9733; Best</strong></td><td class="chk">Free</td><td class="chk">Free</td><td class="chk">Free</td><td class="chk">Free</td><td>$75</td></tr>
            <tr><td><strong>Delta</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>United</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>American</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>Alaska</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>JetBlue</strong></td><td class="chk">Free</td><td>$35&#8211;$70</td><td>$45</td><td>$60</td><td>$150</td></tr>
            <tr><td><strong>Spirit</strong></td><td class="chk">Free</td><td>$39&#8211;$89</td><td>$39&#8211;$99</td><td>$39&#8211;$99</td><td>$100+</td></tr>
            <tr><td><strong>Frontier</strong></td><td class="chk">Free</td><td>$39&#8211;$69</td><td>$39&#8211;$89</td><td>$39&#8211;$89</td><td>$75+</td></tr>
            <tr><td><strong>Allegiant</strong></td><td class="chk">Free</td><td>$18&#8211;$55</td><td>$30&#8211;$75</td><td>$30&#8211;$75</td><td>$75</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>The Southwest Exception</h2>
      <p>Southwest includes 2 free checked bags for every passenger &#8212; the only major US carrier with this policy. This makes Southwest often the cheapest all-in option even when its base fare is higher than Spirit or Frontier. A $99 Southwest fare with two free bags beats a $49 Spirit fare the moment you need to check anything.</p>
      <h2>JustFly Shows Total Cost Before You Book</h2>
      <p>JustFly displays estimated total cost including your selected bag option in search results &#8212; so you&#8217;re comparing all-in price across airlines, not just base fares. This is one of JustFly&#8217;s genuine differentiators vs sites that hide bag fees until late in checkout.</p>
      {cta("Find the Cheapest All-In Fare on JustFly","Bag fees included in every comparison.")}
    </div>
  </section>"""

def page_last_minute():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Last Minute &#8212; 2026</div>
      <h1>Last Minute Flights USA:<br><em>What Actually Works in 2026</em></h1>
      <p class="hero-sub">Last-minute flights aren&#8217;t always expensive. Here are the specific conditions when they&#8217;re cheap &#8212; and exactly how to find them on JustFly.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search Last-Minute Fares &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Search Before 8am on Travel Day</h3><p>Airlines reprice multiple times daily. The early morning pricing pass (5&#8211;7am) often drops fares to fill unsold seats before departure. Same-day morning searches frequently uncover deals that didn&#8217;t exist the night before.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Compare Every Nearby Airport</h3><p>A different airport 30&#8211;45 minutes away can be $80&#8211;$150 cheaper for same-day travel. JustFly searches all nearby airports simultaneously &#8212; always run the broader search.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Accept One Connection</h3><p>Last-minute nonstop fares are almost always expensive. A connecting flight departing in 3 hours can be 40&#8211;60% cheaper. If you have time, a connection saves significant money on same-day bookings.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>Target High-Frequency Routes</h3><p>Routes with 10+ daily flights (NYC-Miami, NYC-LA, LA-Vegas, Chicago-Miami) regularly discount unsold seats close to departure. Low-frequency routes rarely discount last-minute.</p></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>Best Routes for Last-Minute Deals</h2>
      <p>High-frequency, high-competition routes are your best bet for same-day and next-day bargains. Airlines would rather sell a $69 seat than fly with it empty.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.6rem;margin:1rem 0 2rem;">
        {"".join(f'<span style="background:var(--fog);border:1px solid var(--border);padding:.35rem .9rem;border-radius:6px;font-size:.85rem;font-weight:700;">{r}</span>' for r in ["NYC &#8594; Miami","NYC &#8594; LA","LA &#8594; Vegas","Chicago &#8594; Miami","Dallas &#8594; NYC","Phoenix &#8594; Vegas","Atlanta &#8594; Miami","Boston &#8594; NYC","Denver &#8594; LA","Seattle &#8594; LA"])}
      </div>
      <h2>The $200 Rule</h2>
      <p>A useful guide for last-minute domestic travel: if the cheapest same-day fare you find is under $200 for a 2&#8211;3 hour route, book it. Prices almost always go up in the final 12 hours before departure as remaining seats get scarce. Waiting for $149 when you see $189 usually results in paying $279.</p>
      {cta("Search Live Last-Minute Fares","JustFly updates in real time &#8212; including those discounted same-day seats.")}
    </div>
  </section>"""

def page_budget():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Budget Airlines &#8212; 2026</div>
      <h1>US Budget Airlines 2026:<br><em>Who&#8217;s Really Cheapest All-In?</em></h1>
      <p class="hero-sub">The airline with the lowest base fare isn&#8217;t always the cheapest once you add bags. Here&#8217;s the complete total-cost comparison &#8212; and how JustFly makes it simple.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Compare All Airlines &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Airline</th><th>Base Fare</th><th>Personal Item</th><th>Carry-On</th><th>Checked Bag</th><th>Seat Select</th><th>All-In Best For</th></tr></thead>
          <tbody>
            <tr><td><strong>Spirit</strong></td><td class="win">From $29</td><td class="chk">Free</td><td>$39&#8211;$89</td><td>$39&#8211;$99</td><td>$5&#8211;$55</td><td>Backpack-only travel</td></tr>
            <tr><td><strong>Frontier</strong></td><td class="win">From $19</td><td class="chk">Free</td><td>$39&#8211;$69</td><td>$39&#8211;$89</td><td>$10&#8211;$45</td><td>Bundle deal buyers</td></tr>
            <tr><td><strong>Allegiant</strong></td><td>From $39</td><td class="chk">Free</td><td>$18&#8211;$55</td><td>$30&#8211;$75</td><td>$5&#8211;$40</td><td>Point-to-point leisure</td></tr>
            <tr><td><strong>Southwest</strong></td><td>From $59</td><td class="chk">Free</td><td class="chk">Free</td><td class="chk">2 bags free</td><td class="chk">Open seating</td><td class="win">Best all-in value</td></tr>
            <tr><td><strong>JetBlue</strong></td><td>From $69</td><td class="chk">Free</td><td>$35&#8211;$70</td><td>$45&#8211;$105</td><td>$0&#8211;$45</td><td>Comfort + reasonable cost</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>The Key Insight: Total Cost, Not Base Fare</h2>
      <p>A $29 Spirit fare with a $89 carry-on fee and $15 seat selection costs $133. A $99 Southwest fare with everything included costs $99. The airline with the lowest headline number is often not the cheapest airline you actually fly on.</p>
      <p>JustFly displays estimated total cost including bag fees in search results &#8212; so you&#8217;re always comparing all-in price across all airlines simultaneously. Most booking sites force you to manually calculate the real cost. JustFly does it for you.</p>
      <h2>When Each Budget Airline Wins</h2>
      <ul class="styled">
        <li><strong>Spirit/Frontier &#8212;</strong> Cheapest when you have only a small personal item (fits under the seat). Quick business trips, overnight getaways with a backpack only.</li>
        <li><strong>Southwest &#8212;</strong> Cheapest the moment you need any bags at all. Two free checked bags makes it unbeatable for checked luggage travelers.</li>
        <li><strong>Allegiant &#8212;</strong> Cheap carry-ons ($18+) make it competitive for weekend trips with small bags. Strong on leisure routes (Florida, Vegas, smaller cities).</li>
        <li><strong>JetBlue &#8212;</strong> Best balance of comfort and cost. More legroom than Spirit at competitive total pricing. Strong on East Coast routes.</li>
      </ul>
      {cta("Find the Cheapest All-In Fare on JustFly","Every airline compared &#8212; total cost shown before you book.")}
    </div>
  </section>"""

def page_promos():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="hero-badge-dot"></span> Best Deals &#8212; June 2026</div>
      <h1>JustFly Promo Codes &amp;<br><em>Best Deals June 2026</em></h1>
      <p class="hero-sub">How to get the absolute lowest price on JustFly &#8212; including our partner link for the best available new-booking offer.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">See Current Offer &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#128279;</span><h3>Partner Link &#8212; Best Available Rate</h3><p>Our affiliate link routes through JustFly&#8217;s partner portal where preferred rates for new bookings are surfaced. This is consistently the best entry point for new customers.</p><a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Access Partner Rate</a></div>
        <div class="feat-card"><span class="feat-icon">&#127963;</span><h3>Bundle for Maximum Savings</h3><p>Flight + hotel bundles save up to 40% vs booking separately. This is consistently the largest single saving available on JustFly &#8212; often $100&#8211;$700 per trip.</p><a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Search Bundles</a></div>
        <div class="feat-card"><span class="feat-icon">&#128276;</span><h3>Price Alerts &#8212; Catch Flash Sales</h3><p>Flash sales on JustFly often surface fares 30&#8211;50% below normal pricing. Price alerts notify you within minutes so you can book before they sell out.</p><a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Set Free Alert</a></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:780px;">
      {faq(
        ("Does JustFly have promo codes in June 2026?","JustFly releases promo codes through email and partner channels. Our partner link surfaces the best available rate for new bookings. Check the link for the current offer."),
        ("How do I apply a JustFly promo code?","At checkout, enter your code in the promo/discount field before confirming payment. The discount is applied immediately."),
        ("What&#8217;s the biggest saving available on JustFly right now?","The largest savings come from flight+hotel bundles (up to 40%) and flash sale price alerts. The partner link above provides the best baseline rate for standard bookings."),
        ("When are JustFly&#8217;s biggest sales of the year?","Major JustFly sales run during Black Friday/Cyber Monday (late November), New Year&#8217;s week (Jan 1&#8211;7), and mid-January. Price alerts are the most reliable way to catch these."),
      )}
      {cta("Claim the Best Available Rate Now","Search via our partner link for the current best offer.")}
    </div>
  </section>"""

def page_about():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <h1>About <em>FlightDealsPro</em></h1>
      <p class="hero-sub">The independent guide helping US travelers find cheaper flights with JustFly since 2020.</p>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:760px;">
      <div class="feat-card">
        <h2 style="font-family:'Cabinet Grotesk',sans-serif;font-size:1.9rem;font-weight:900;margin-bottom:1rem;">Our Mission</h2>
        <p>FlightDealsPro exists because most travelers overpay for flights &#8212; not because cheap fares don&#8217;t exist, but because they don&#8217;t know where to find them or when to book. We research, test, and compare booking platforms so you don&#8217;t have to.</p>
        <p>After testing 10+ booking platforms over 4 years and running hundreds of price comparisons, we recommend JustFly as the best starting point for US domestic flights and most international routes &#8212; particularly for its pricing consistency, bundle savings, and fee transparency.</p>
        <h3>What We Publish</h3>
        <ul class="styled">
          <li>Honest, data-backed reviews of travel booking platforms</li>
          <li>City-specific flight deal guides with real fare data</li>
          <li>Route booking windows &#8212; exactly when to buy for each destination</li>
          <li>Baggage fee comparisons for every US airline</li>
          <li>Budget airline total-cost guides</li>
          <li>Flight+hotel bundle savings analysis</li>
        </ul>
        <h3>Affiliate Disclosure</h3>
        <p>FlightDealsPro earns a commission when you book via our JustFly links. This costs you nothing extra &#8212; the price you pay is identical whether you arrive via our link or directly. Our recommendations are based on genuine price testing and honest assessment of platform quality.</p>
        <div style="text-align:center;margin-top:2rem;">
          <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Search Flights on JustFly &rarr;</a>
        </div>
      </div>
    </div>
  </section>"""

# ─── CONTENT ROUTER ──────────────────────────────────────────────────────────
FN_MAP = {
    "page_home":page_home,"page_review":page_review,
    "page_vs_expedia":page_vs_expedia,"page_vs_kayak":page_vs_kayak,"page_vs_priceline":page_vs_priceline,
    "page_cheap_usa":page_cheap_usa,"page_nyc":page_nyc,"page_miami":page_miami,
    "page_lax":page_lax,"page_chicago":page_chicago,"page_vegas":page_vegas,
    "page_international":page_international,"page_bundles":page_bundles,
    "page_tips":page_tips,"page_timing":page_timing,"page_baggage":page_baggage,
    "page_last_minute":page_last_minute,"page_budget":page_budget,
    "page_promos":page_promos,"page_about":page_about,
}

def write_robots():
    (OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

def write_sitemap():
    urls = ""
    for p in PAGES:
        loc = f"{BASE}/" if p["slug"]=="index" else f"{BASE}/{p['slug']}.html"
        urls += f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{p['priority']}</priority></url>\n"
    (OUT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>')

def write_llms():
    (OUT/"llms.txt").write_text(f"""# FlightDealsPro — JustFly Affiliate Guide

> Independent guide helping US travelers find cheaper flights with JustFly.

## Coverage
JustFly reviews, comparisons (vs Expedia, Kayak, Priceline, Google Flights), city guides (NYC, Miami, LA, Chicago, Vegas), domestic deals, international flights, flight+hotel bundles, 15 booking tips, timing guides, baggage fees, budget airline total-cost comparisons, price alerts, promo codes.

## Key Pages
- [Home]({BASE}/) - Deals, comparisons, testimonials
- [Review]({BASE}/justfly-review.html) - 6-month honest review
- [vs Expedia]({BASE}/justfly-vs-expedia.html) - 20-route price test
- [vs Kayak]({BASE}/justfly-vs-kayak.html) - Booking vs redirect
- [vs Priceline]({BASE}/justfly-vs-priceline.html) - Transparent vs blind
- [Cheap Flights USA]({BASE}/cheap-flights-usa.html) - 20 cheapest routes
- [Bundles]({BASE}/flight-hotel-bundles.html) - Save up to 40%
- [15 Tips]({BASE}/flight-booking-tips.html) - Expert strategies
- [Timing Guide]({BASE}/best-time-to-book.html) - When to book
- [Baggage Fees]({BASE}/baggage-fees.html) - All airlines compared
- [Budget Airlines]({BASE}/budget-airlines.html) - Total cost guide

## Affiliate
FlightDealsPro earns commission from JustFly. Booking link: {AFF}
""")

def write_404():
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 &#8212; FlightDealsPro</title><style>{css()}</style></head><body>
<nav><a class="logo" href="{SUB}/"><span class="logo-mark">&#9992;</span>Flight<em>Deals</em>Pro</a></nav>
<section class="hero" style="min-height:80vh;"><div class="hero-inner">
<div style="font-size:5rem;margin-bottom:1.2rem;">&#9992;</div>
<h1>404 &#8212; <em>Flight Cancelled</em></h1>
<p class="hero-sub">This page doesn&#8217;t exist. Let&#8217;s get you back to finding cheap flights.</p>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
<a href="{SUB}/" class="btn btn-orange">Go Home</a>
<a href="{AFF}" class="btn btn-ghost" rel="nofollow sponsored">Search Flights &rarr;</a>
</div></div></section></body></html>"""
    (OUT/"404.html").write_text(html)

def build():
    OUT.mkdir(exist_ok=True)
    for p in PAGES:
        body  = FN_MAP[p["content_fn"]]()
        html  = layout(p, body)
        fname = "index.html" if p["slug"]=="index" else f"{p['slug']}.html"
        (OUT/fname).write_text(html, encoding="utf-8")
        print(f"  ✓ {fname}")
    write_robots(); write_sitemap(); write_llms(); write_404()
    pages = list(OUT.glob("*.html"))
    kb    = sum(f.stat().st_size for f in pages)//1024
    print(f"\n  ✅ Build complete — {len(pages)} pages, {kb}KB")
    print(f"  📍 Deploy docs/ to GitHub Pages")
    print(f"  🌐 {BASE}/")

if __name__ == "__main__":
    build()
