# Plan: Sales Dashboard with Filtering

## Overview
Add a "DASHBOARD" page to the existing Zava SPA showing Sales By Category charts and a data table, loaded from sample_data.csv via a new Flask endpoint. Filtering dropdowns control all charts and table.

## Steps

### Phase 1: Flask backend
1. Add `/sales-data` GET endpoint in `app.py` — reads `sample_data.csv` with Python's `csv` module, returns JSON array of `{year, quarter, category, amount, location}` rows. Supports optional query params: `year`, `quarter`, `category`, `location` for server-side filtering.

### Phase 2: Frontend — dashboard page & nav
2. Add Chart.js CDN `<script>` tag to `<head>` in `templates/index.html`
3. Add `DASHBOARD` nav link (desktop + mobile) in the `<nav>` at lines 93–109 — positioned after SALES
4. Add `<div id="dashboardPage" class="page-section">` after contactPage (~line 455)

### Phase 3: Dashboard layout & filtering
5. Dashboard section structure:
   - Header: "Sales By Category" title
   - Filter bar: dropdowns for Year, Quarter, Category, Location (populated dynamically from data)
   - Charts row: bar chart (by category), bar chart (by quarter), pie chart (by category total)
   - Data table: Year, Quarter, Category, Amount, Location columns with teal header row matching image

### Phase 4: JavaScript
6. `loadDashboard()` function — fetches `/sales-data`, populates filter dropdowns on first load
7. `applyFilters()` function — re-fetches `/sales-data` with current filter values, updates charts and table
8. Chart rendering with Chart.js:
   - Left bar: total amount per category, multi-color bars matching image palette
   - Middle bar: total amount per quarter, single blue color
   - Right pie: total by category, matching image color palette
9. Colors to match image:
   - Automotive: #2e7d7d, Books: #4472c4, Clothing: #5b9bd5, Electronics: #70ad47, Food & Beverage: #c55a11, General: #7f7f7f, Health & Beauty: #1f3864, Home & Garden: #a5a5a5, Sports: #7030a0, Toys: #548235

## Relevant files
- `app.py` — add `/sales-data` route
- `templates/index.html` — add Chart.js CDN, nav link, dashboard page section + JS

## Verification
1. Flask server starts without error: `python app.py`
2. GET `/sales-data` returns JSON array
3. GET `/sales-data?year=2024&quarter=Q1` returns filtered subset
4. Navigate to DASHBOARD in browser — 3 charts and table render
5. Change a filter dropdown — charts and table update to reflect filtered data

## Decisions
- Server-side filtering via query params (simple, no extra dependencies)
- Chart.js from CDN (consistent with Tailwind CDN pattern already used)
- No new template files — everything in index.html
- `sample_data.csv` is read from disk on each request (small file, acceptable)
- DASHBOARD nav link placed after SALES (HOME, ABOUT, PRODUCTS, SALES, DASHBOARD, STORES, CONTACT)
