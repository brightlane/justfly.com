# FlightDealsPro — JustFly Affiliate Site v2

> 20-page static affiliate site promoting JustFly.
> Live at: **https://brightlane.github.io/justfly/**
> Affiliate URL: `https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885`

---

## Quick Start

```bash
git clone https://github.com/brightlane/justfly.git
cd justfly
python3 build.py
```

Push to `main` — GitHub Actions builds and deploys automatically.

---

## Repo Structure

```
justfly/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

After running `build.py`, a `docs/` folder is generated and deployed.

---

## Pages (20)

| Page | File | Target Keywords |
|------|------|-----------------|
| Homepage | index.html | justfly cheap flights 2026 |
| Review | justfly-review.html | justfly review 2026 |
| vs Expedia | justfly-vs-expedia.html | justfly vs expedia |
| vs Kayak | justfly-vs-kayak.html | justfly vs kayak |
| vs Priceline | justfly-vs-priceline.html | justfly vs priceline |
| Cheap Flights USA | cheap-flights-usa.html | cheapest domestic flights usa |
| NYC Flights | nyc-flights.html | cheap flights from new york |
| Miami Flights | miami-flights.html | cheap flights from miami |
| LA Flights | los-angeles-flights.html | cheap flights from los angeles |
| Chicago Flights | chicago-flights.html | cheap flights from chicago |
| Vegas Flights | las-vegas-flights.html | cheap flights to las vegas |
| International | international-flights.html | cheap international flights usa |
| Bundles | flight-hotel-bundles.html | flight hotel bundles |
| 15 Booking Tips | flight-booking-tips.html | flight booking tips 2026 |
| Best Time to Book | best-time-to-book.html | best time to book flights |
| Baggage Fees | baggage-fees.html | airline baggage fees 2026 |
| Last Minute | last-minute-flights.html | last minute flights usa |
| Budget Airlines | budget-airlines.html | spirit frontier allegiant |
| Promo Codes | promo-codes.html | justfly promo codes 2026 |
| About | about.html | about flightdealspro |

---

## GitHub Pages Setup

1. Create repo `brightlane/justfly` on GitHub
2. Add `build.py` to the repo root
3. Add `.github/workflows/deploy.yml`
4. Go to **Settings → Pages → Source → GitHub Actions**
5. Push to `main` — builds and deploys automatically
6. Live at `https://brightlane.github.io/justfly/`

---

## GitHub Actions Workflow

File: `.github/workflows/deploy.yml`

- Triggers on every push to `main`
- Sets up Python 3.11
- Runs `python3 build.py` to generate `docs/`
- Deploys `docs/` to GitHub Pages automatically
- Can also be triggered manually via Actions tab

---

## Customisation

### Update affiliate URL
```python
AFF = "https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885"
```

### Update live URL
```python
BASE = "https://brightlane.github.io/justfly"
SUB  = "/justfly"
```

### Update deal prices
Each deal is a 5-tuple:
```python
("Route Name", "$Price", "Badge Text", "badge-css-class", "Short note")
```
Badge classes: `tag-hot` (red), `tag-sale` (amber), `tag-new` (green), `tag-flash` (blue)

### Add a city page
1. Write a `def page_yourcity():` function using `city_page()`
2. Add entry to `PAGES` list
3. Add to `FN_MAP`
4. Run `python3 build.py`

### Add a new page from scratch
1. Add entry to `PAGES` list with `slug`, `title`, `desc`, `content_fn`
2. Write `def page_yourpage():` returning HTML string
3. Add to `FN_MAP`
4. Run `python3 build.py`

---

## SEO Files Generated

| File | Purpose |
|------|---------|
| `robots.txt` | Allows all crawlers, points to sitemap |
| `sitemap.xml` | 20 URLs with priorities and change frequencies |
| `llms.txt` | AI crawler instructions (llmstxt.org standard) |
| `404.html` | Branded error page with CTA |

---

## What's New in v2

- New design: deep navy + electric orange, Cabinet Grotesk + Satoshi fonts
- Gradient text hero headlines with live pulse dot indicators
- Savings ticker bar at top of every page
- Savings strip below hero with today's top 3 deals
- vs Priceline page added (transparent vs blind pricing)
- Las Vegas flights page added
- 15 booking tips (was 12) — deeper and more actionable
- All testimonials show specific dollar savings amounts
- Bundles page has 8-destination savings table with real numbers
- Review based on 30-route test and 4 actual bookings
- vs Expedia has full 20-route price comparison table
- Budget airlines page explains when each airline wins
- Last minute page includes the "$200 Rule"

---

## Tech Stack

- Python 3.8+ — standard library only, zero dependencies
- Static HTML/CSS — no JavaScript frameworks
- Google Fonts — Cabinet Grotesk + Satoshi
- GitHub Pages — free hosting, auto-deploy via Actions

---

## Affiliate Disclosure

FlightDealsPro is an independent affiliate partner of JustFly.
Not operated by or affiliated with JustFly.

---

## License

MIT — free to use, modify, and deploy.
