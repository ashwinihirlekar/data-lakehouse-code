# Package Sorting Solution

A simple package sorting system that categorizes packages based on volume and mass.

## How It Works

Packages are classified into three categories:

- **STANDARD**: Regular packages
- **SPECIAL**: Bulky or heavy packages  
- **REJECTED**: Both bulky AND heavy

## Rules

A package is:
- Bulky if: volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- Heavy if: mass ≥ 20 kg

## Usage

python sort(100, 200, 100, 10)  
# Returns "STANDARD"
