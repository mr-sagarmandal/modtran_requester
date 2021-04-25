import modtran_client

## rtmode choices are: RT_SOLAR_AND_THERMAL, RT_TRANSMITTANCE
## atmosphere_model choices are: ATM_MIDLAT_SUMMER, ATM_US_STANDARD_1976, ATM_SUBARC_WINTER, ATM_SUBARC_SUMMER, ATM_TROPICAL, ATM_MIDLAT_WINTER
## spectral_units choices are: microns, wavenumbers
## aerosol_model are: AER_MARITIME_NAVY, AER_RURAL, AER_DESERT, AER_URBAN
payLoad = {
    "csrfmiddlewaretoken" : "bh9S5umFxQk4EFeYJjH7qmdQS4acxNVI",
    "rtmode" : "RT_SOLAR_AND_THERMAL" , 
    "atmosphere_model" : "ATM_MIDLAT_SUMMER" ,
    "water_column" : 3635.9 ,
    "ozone_column" : 0.33176 ,
    "co2_ppmv" : 400 ,
    "co_ppmv" : 0.15 ,
    "co_ppmv_ref" : 0.15 ,
    "ch4_ppmv" : 1.8 ,
    "ch4_ppmv_ref" : 1.7 ,
    "n2o_ppmv" : 0.32 ,
    "n2o_ppmv_ref" : 0.32 ,
    "f11_ppbv" : 0.14 ,
    "f11_ppbv_ref" : 0.14 ,
    "f12_ppbv" : 0.24 ,
    "f12_ppbv_ref" : 0.24 ,
    "f22_ppbv" : 0.06 ,
    "f22_ppbv_ref" : 0.06 ,
    "f113_ppbv" : 0.019 ,
    "f113_ppbv_ref" : 0.019 ,
    "f114_ppbv" : 0.012 ,
    "f114_ppbv_ref" : 0.012 ,
    "ccl4_ppbv" : 0.13 ,
    "ccl4_ppbv_ref" : 0.13 ,
    "ground_temp_K" : 294.2 ,
    "ground_emission" : 0 ,
    "aerosol_model" : "AER_MARITIME_NAVY" ,
    "visibility_km" : 23.0 ,
    "sens_altitude_km" : 50 ,
    "sens_zenith_deg" : 180 ,
    "path_range_km" : 70 ,
    "solar_zenith_deg" : 0 ,
    "solar_azimuth_deg" : 0 ,
    "spectral_units" : "wavenumbers" ,
    "specrng_min" : 250 ,
    "specrng_max" : 500 ,
    "resolution" : 0.2,
}

range_pairs = [
    [250, 500, 0.2]
]
        
       
if __name__ == "__main__":
    modtran_client.get_data_for_ranges(range_pairs, payLoad)


