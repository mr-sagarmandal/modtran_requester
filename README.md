# modtran_requester
Simple HTTP requests utilizing Modtran API to fetch data

## Requirements
* Python 3.x. Can be downloaded [here](https://www.python.org/downloads/).

Install requirements by running:

`pip install -r requirements.txt`

**Note:** It is easier to work with this repo, if one has a coding editor installed e.g. [VSCode](aka.ms/vscode).

## Running the code
1) Open [modtran_request.py](./modtran_request.py)
2) Modify parameters of the request by modifying the payLoad dictionary and range_pairs:
  * In Payload:
    * rtmode choices are: RT_SOLAR_AND_THERMAL, RT_TRANSMITTANCE
    * atmosphere_model choices are: ATM_MIDLAT_SUMMER, ATM_US_STANDARD_1976, ATM_SUBARC_WINTER, ATM_SUBARC_SUMMER, ATM_TROPICAL, ATM_MIDLAT_WINTER
    * spectral_units choices are: microns, wavenumbers
    * aerosol_model are: AER_MARITIME_NAVY, AER_RURAL, AER_DESERT, AER_URBAN
  
  * In range_pairs, specify the ranges to send separate requests for each range list. It is in the format: [`specrng_min` , `specrng_max` , `resolution` ]
    Add as many list within the outer list separated by a comma.
3) After modifying the parameter, run 

`python modtran_request.py`

**Note:** It might take a while to fetch data based on the range_pairs.
