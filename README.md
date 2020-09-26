Data Package with Assessments of the Nationally Determined Contributions (NDCs) of
countries


# Data

The Excel files from the [CAIT Climate Data Explorer](http://cait.wri.org/indcs/)
and [Worldbank INDC tool](http://indc.worldbank.org/) assessments were downloaded
from [Climate Watch](https://www.climatewatchdata.org/)
and are converted into CSV files to simplify analysis.
The CSV files from the [Klimalog NDC Explorer](https://klimalog.die-gdi.de/ndc/) are provided as is.


# Preparation

Data was downloaded from the Climate Watch (https://www.climatewatchdata.org/)
portal and converted into CSV files. Klimalog data is downloaded directly from <https://klimalog.die-gdi.de/ndc/#open-data>.
Python 3, wget and Make are required to re-run the scripts:

    make


# Licenses

## CAIT Assessment

Creative-Commons Attribution (CC-BY) https://creativecommons.org/licenses/by/4.0/ 

### Citation

WRI, CAIT Climate Data Explorer. 2016. CAIT Paris Contributions Map. Washington, DC: World Resources Institute. http://cait.wri.org/indcs/

## Klimalog GDI DIE NDC Explorer Assessment

Creative-Commons Attribution (CC-BY) https://creativecommons.org/licenses/by/4.0/ 

See their [website's](https://klimalog.die-gdi.de/ndc/#NDCExplorer/) 'download data' section for updates and citation requirements:

> You are warmly invited to download and use the data of the NDC Explorer under the following conditions. The data is licenced under CC BY 4.0. If you share, copy and redistribute the material you must give appropriate credit (name creator, copyright notice, licence notice and a link to the material). If you remix, transform or build upon the material you must distribute your contributions under the same license as the original, and indicate the changes you have made.
>
> Please consider that the underlying data is updated on a regular basis, e.g. with new NDCs releases. Therefore, please state the date of your download when referring to the data.

The date of the latest update is also given inside the CSV file.

###  Citation
Pauw, W.P, Cassanmagnano, D., Mbeva, K., Hein, J., Guarin, A., Brandi, C., Dzebo, A., Canales, N., Adams, K.M., Atteridge, A., Bock, T., Helms, J., Zalewski, A., Frommé. E., Lindener, A., Muhammad, D. (2016). NDC Explorer. German Development Institute / Deutsches Institut für Entwicklungspolitik (DIE), African Centre for Technology Studies (ACTS), Stockholm Environment Institute (SEI). DOI: 10.23661/ndc_explorer_2017_2.0

## Worldbank Assesment

Creative-Commons Attribution (CC-BY)  https://creativecommons.org/licenses/by/4.0/

See also https://data.worldbank.org/summary-terms-of-use

### Citation

World Bank. 2017. INDC. Accessed October 5. http://spappssecext.worldbank.org/sites/indc/Pages/INDCHome.aspx

## Preparation scripts

The processing scripts in `scripts` are licensed as CC0.
