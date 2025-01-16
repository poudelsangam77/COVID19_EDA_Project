# COVID-19 Exploratory Data Analysis (EDA) Project

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on global and country-level **COVID-19 data**. Through various visualizations and statistical techniques, this project aims to:
- Analyze COVID-19 trends globally and locally (by country).
- Understand key features of the data such as infection rates, mortality rates, and vaccination progress.
- Identify patterns, outliers, and correlations in the dataset.
- Create actionable insights using various plots and reports.

## Project Goal
The goal of this project is to provide clear insights into the **spread and impact of COVID-19** worldwide. Key questions addressed include:
- What are the most affected regions by COVID-19?
- How have case numbers and deaths evolved over time?
- What are the trends in COVID-19 vaccination?

## Technologies Used
- **Python**: For data processing and analysis.
  - Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
- **Jupyter Notebook**: For running and documenting the analysis.
- **Dash/Plotly**: For creating interactive dashboards.
- **Git**: For version control and collaboration.
- **GitHub**: For repository hosting and sharing.

## Dataset

This project utilizes **multiple datasets** from various reliable sources to perform an exploratory data analysis of COVID-19 trends globally and at the country level. The following datasets are used in this project:

### Dataset Sources:
1. **Johns Hopkins University COVID-19 Dataset**
   - **Source**: [GitHub Repository - Johns Hopkins University COVID-19](https://github.com/CSSEGISandData/COVID-19)
   - **Description**: This dataset contains daily reports of confirmed COVID-19 cases, deaths, and recoveries at a global level and by country.
   - **Data Included**: 
     - Confirmed cases
     - Deaths and recoveries
     - Geographical information (e.g., country, province)

2. **Our World in Data COVID-19 Dataset**
   - **Source**: [GitHub Repository - Our World in Data COVID-19](https://github.com/owid/covid-19-data)
   - **Description**: This dataset provides detailed COVID-19 data on confirmed cases, deaths, and vaccination information by country.
   - **Data Included**:
     - Daily reported cases and deaths
     - Vaccination data by country
     - Demographic data and health indicators

3. **COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University**
   - **Source**: [GitHub Repository - CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)
   - **Description**: Another source from Johns Hopkins University that provides global case data, including confirmed cases, deaths, and recoveries.
   - **Data Included**:
     - Global case counts
     - Country-level statistics for the spread of COVID-19

### **Key Features of the Dataset**:
- **Confirmed Cases**: The number of COVID-19 confirmed cases reported globally and at the country level.
- **Deaths and Recoveries**: Information on the number of deaths and recoveries due to COVID-19.
- **Vaccination Data**: Global and country-wise vaccination statistics to understand the progress of vaccination campaigns.
- **Time Period**: The data spans from the beginning of the COVID-19 pandemic to the present, with daily updates.


## Folder Structure


The project structure is organized as follows:

```
COVID19_EDA_Project/
├── data/
│   ├── raw/               
│   └── processed/        
├── notebooks/
│   ├── data_cleaning.ipynb   
│   ├── exploratory_analysis.ipynb  
│   └── visualizations.ipynb  
├── dashboard/               
├── reports/
│   └── visuals/            
├── .gitignore               
├── LICENSE                  
├── README.md                
└── requirements.txt    
```     


### Folder Details:
- **`data/raw/`**: Contains the raw datasets that are directly sourced and need processing.
- **`data/processed/`**: Contains cleaned and pre-processed data, ready for analysis.
- **`notebooks/`**: Jupyter notebooks for carrying out the data analysis, cleaning, and visualizations.
- **`dashboard/`**: Contains Dash application files (if you're creating a web-based dashboard for the project).
- **`reports/visuals/`**: This folder stores the saved visualizations (graphs, plots, charts) for reports.
- **`.gitignore`**: Ensures that unnecessary or temporary files are not tracked by Git (such as compiled Python files, logs, or system files).
- **`LICENSE`**: A file that outlines the licensing terms for your project.
- **`README.md`**: The file you are currently reading, which contains project information and guidelines.
- **`requirements.txt`**: Lists the Python libraries that are required to run the project (you can generate this by running `pip freeze > requirements.txt`).


## Process Involved in this Project

### Data Cleaning

The cleaning process involved the following steps for each dataset:

1. **Handling Missing Values**: Replaced missing values with `0` in numerical columns.
2. **Standardizing Column Names**: Renamed columns for consistency (e.g., "Country/Region" → "Country").
3. **Ensuring Consistent Date Formats**: Ensured all date columns follow the `YYYY-MM-DD` format.
4. **Removing Duplicates**: Checked and removed duplicate rows, if any.
5. **Dropping Irrelevant Columns**: Removed unnecessary columns that do not contribute to the analysis.

### Cleaned Datasets:
- `cleaned_confirmed_cases.csv`
- `cleaned_deaths.csv`
- `cleaned_recovered.csv`
- `cleaned_vaccinations.csv`


##  EDA and Visualizations
The following insights were drawn using data visualization techniques.

###  Global Analysis
- **Confirmed Cases Over Time**: Observed exponential growth globally with peaks during major pandemic waves.
- **Mortality Rates**: Fluctuated by region, with some areas significantly higher.
- **Vaccination Trends**: Developed countries showed rapid increases compared to developing nations.

###  Country-Level Analysis
- **Top 10 Affected Countries**: USA, India, and Brazil consistently led in confirmed cases and deaths.
- **Case Fatality Rate (CFR)**: Regions like Italy and the UK showed a higher CFR during initial waves.

###  Vaccination Insights
- **Top Vaccinated Countries**: Countries like Israel, UAE, and the USA showed high vaccination rates early.
- **Effectiveness**: Countries with higher vaccination rates showed a decline in mortality rates.

---

##  Key Findings
- **Global Trends**: COVID-19 cases and deaths followed a cyclical pattern, correlating with waves of infection.
- **Regional Variations**: Developed countries had better healthcare responses but also experienced higher initial cases due to robust testing.
- **Vaccination Impact**: Strong evidence supports that vaccination campaigns reduced mortality rates in most regions.
- **Case Fatality Rate**: Globally, the CFR ranged between 1%–3%, with significant variance across regions.



### Dashboard

An interactive dashboard has been created to visualize the COVID-19 data and provide real-time insights. The dashboard is built using **Dash/Plotly** and includes the following features:

- **Global Overview**: Displays global statistics including total confirmed cases, deaths, and recoveries.
- **Country Comparison**: Allows users to compare COVID-19 statistics between different countries.
- **Trend Analysis**: Shows trends over time for cases, deaths, and vaccinations.
- **Vaccination Progress**: Visualizes the progress of vaccination campaigns globally and by country.
- **Interactive Maps**: Provides geographical representations of COVID-19 data, highlighting affected regions.

#### How to Run the Dashboard

1. Ensure you have all the required libraries installed. You can install them using the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

2. Navigate to the `dashboard/` directory:
  ```bash
  cd dashboard
  ```

3. Run the Dash application:
  ```bash
  python app.py
  ```

4. Open your web browser and go to `http://127.0.0.1:8050/` to view the dashboard.

#### Dashboard Files

- **`app.py`**: The main file that runs the Dash application.
- **`callbacks.py`**: Contains callback functions for interactivity in the dashboard.
- **`layout.py`**: Defines the layout and structure of the dashboard.
- **`assets/`**: Contains CSS and other assets for styling the dashboard.

The dashboard provides an intuitive and interactive way to explore the COVID-19 data, making it easier to derive insights and understand trends.
6. **Saving Cleaned Data**: All cleaned datasets were saved in the `data/processed/` folder for further analysis.


## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push your changes to your forked repository (`git push origin feature-branch`).
5. Open a pull request to the `main` branch of the original repository.

Please ensure that your contributions follow the project’s coding style, and add tests/documentation if applicable.

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the data sources used for this project:
  - [Johns Hopkins University COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19)
  - [Our World in Data COVID-19 Dataset](https://github.com/owid/covid-19-data)
  - [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)

- Thanks to the open-source community for the Python libraries used in this project:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `dash`

- All contributors and collaborators who made this project possible.
