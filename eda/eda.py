import os
import re
import pandas as pd
import matplotlib.pyplot as plt

def clean_price(x):
    """
    Convert strings like '₹ 30,00,000/Piece' or '30,000 - 50,000' to a float.
    - Strips currency symbols, unit labels, commas.
    - If it’s a range (e.g. '10,000 - 20,000'), takes the midpoint.
    - Returns None if it can’t parse.
    """
    if pd.isna(x):
        return None
    s = str(x)
    # remove ₹, commas, and anything after a slash or non-digit
    s = re.sub(r"[₹,]", "", s)
    # replace range dash with ' - ' to split
    parts = re.split(r"\s*-\s*", s)
    nums = []
    for p in parts:
        # extract digits and decimals
        m = re.search(r"(\d+(\.\d+)?)", p)
        if m:
            nums.append(float(m.group(1)))
    if not nums:
        return None
    # if multiple numbers (range), return midpoint
    return sum(nums) / len(nums)

def run_eda(input_csv, output_dir):
    df = pd.read_csv(input_csv)

    # Clean price column
    df['price_clean'] = df['price'].apply(clean_price)

    # create output dir
    os.makedirs(output_dir, exist_ok=True)

    # 1) Price distribution
    plt.figure()
    df['price_clean'].dropna().hist(bins=50)
    plt.title("Price Distribution")
    plt.xlabel("Price (numeric)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/price_distribution.png")
    plt.close()

    # 2) Top categories
    plt.figure()
    df['category'].value_counts().head(10).plot(kind='barh')
    plt.title("Top Categories")
    plt.xlabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_categories.png")
    plt.close()

    # 3) Summary statistics
    stats = df['price_clean'].describe()
    print("Price summary statistics:")
    print(stats.to_string())

if __name__ == "__main__":
    import sys
    in_csv  = sys.argv[1] if len(sys.argv)>1 else "../output/processed.csv"
    out_dir = sys.argv[2] if len(sys.argv)>2 else "../output/eda"
    run_eda(in_csv, out_dir)
