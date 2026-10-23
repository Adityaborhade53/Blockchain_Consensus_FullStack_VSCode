# ConsensusLab — Comparative Security and Energy Analysis

Full-stack educational dashboard using **Python, Flask, Pandas, Matplotlib, HTML, CSS, JavaScript, and Chart.js**. It compares PoW, PoS, DPoS, and PBFT.

> Numerical time, energy, and score values are illustrative teaching assumptions—not measurements from live blockchain networks.

## Features
- Responsive frontend dashboard, summary cards, charts, searchable table.
- Security threats and mitigations.
- Flask JSON APIs: `/api/consensus` and `/api/security`.
- Generate reports button exports two CSVs and four PNG charts.
- System architecture, workflow, report, and automated tests.

## Run in VS Code on Windows

1. Extract the ZIP and open the extracted `Blockchain_Consensus_FullStack` folder in VS Code.
2. Select **Terminal → New Terminal**.
3. Check Python:

   ```powershell
   python --version
   ```

   If Python is missing, install it from https://www.python.org/downloads/windows/ and select **Add python.exe to PATH** during setup. Restart VS Code. This project uses `python`; the `py` launcher is not required.

4. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

5. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If activation is blocked, use `.\.venv\Scripts\python.exe` instead of `python` in the next commands.

6. Install packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the site:

   ```powershell
   python app.py
   ```

8. Open **http://127.0.0.1:5000** in Chrome or Edge. Keep the terminal open while the server runs. Press `Ctrl+C` to stop it.

9. Click **Generate reports** to create files in `output/`.

## Tests

```powershell
python -m unittest discover -s tests -v
```

## Troubleshooting
- **`python` not recognized:** install Python, enable PATH, restart VS Code.
- **`ModuleNotFoundError`:** run `python -m pip install -r requirements.txt` using the same interpreter that starts the app.
- **Port 5000 in use:** change `port=5000` to `port=5001` in `app.py` and open `http://127.0.0.1:5001`.
- Browser charts use Chart.js from a CDN and need internet. PNG report charts are generated locally.

## Project layout

```text
Blockchain_Consensus_FullStack/
├── app.py
├── src/consensus_analysis.py
├── templates/index.html
├── static/styles.css
├── docs/PROJECT_REPORT.md
├── docs/SYSTEM_ARCHITECTURE.md
├── docs/WORKFLOW.md
├── tests/test_consensus_analysis.py
├── output/
├── requirements.txt
└── README.md
```
