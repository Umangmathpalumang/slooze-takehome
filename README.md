# Slooze Data Engineering Take-Home

## Part A: Crawler

1. **Install dependencies**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure categories**  
   Edit `config/categories.yaml` to update target URLs.

3. **Run crawler**  
   ```bash
   cd crawler
   python __main__.py --config ../config/categories.yaml --out ../output/processed.csv
   ```

## Part B: Exploratory Data Analysis

1. **Generate EDA visualizations**  
   ```bash
   python eda/eda.py
   ```

2. **Results**  
   Outputs saved in `output/eda/`.




1. **Clone & venv**  
   ```bash
   git clone <your-repo-url>
   cd slooze-takehome
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
Configure categories
Edit config/categories.yaml with real listing/search URLs.

Run the crawler

bash
Copy
mkdir -p output
python crawler/__main__.py \
  --config config/categories.yaml \
  --out output/processed.csv
Perform EDA

bash
Copy
python eda/eda.py output/processed.csv output/eda
Outputs charts in output/eda/.

arduino
Copy
slooze-takehome/
├── config/
│   └── categories.yaml
├── crawler/
│   ├── downloader.py
│   ├── parser.py
│   └── __main__.py
├── eda/
│   └── eda.py
├── output/      
├── requirements.txt
└── README.md


Commit raw HTML snapshots if needed.

Label your charts and include brief write-ups of your insights.
