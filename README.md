# 🧠 Softwaredesign 2025

A clean Python monorepo for personal study, utility code, and small projects — managed with [PDM](https://pdm.fming.dev/).

## 📂 Structure
```python
Softwaredesign2025/
├─ .venv/ # Local venv (ignored)
├─ libs/
│ └─ YMDUtil/ # Local Python package (date utilities)
├─ pyproject.toml
└─ README.md
```

## 🧰 Tech
- Python 3.10+
- PDM for dependency & env management
- pytest for testing
- Jupyter for quick experiments

## 📦 YMDUtil
A small helper library for working with dates.

```python
from YMDUtil import isLeapYear, dayOfWeek, calcWeekNr

print(isLeapYear(2024))          # True
print(dayOfWeek(23, 10, 2025))   # Thursday
print(calcWeekNr(23, 10, 2025))  # 42
```
## ⚡ Setup once shared:
```bash
git clone https://github.com/SUHonzz/Softwaredesign2025.git
cd Softwaredesign2025
pdm install
pdm run python
```


## 🧪 Dev 
# Add local lib in editable mode
```bash
pdm add -d -e libs/YMDUtil
```

# Run tests
```bash
pdm run pytest
```

# Launch notebooks
```bash
pdm run jupyter lab

```
## 📝 License

MIT © 2025 Hannes Unterhuber
