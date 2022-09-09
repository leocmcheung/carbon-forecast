
import pandas as pd
import numpy as np
"""
README FIRST

Use load_n_preproc(year) to extract ONE year of data
Use load_n_preproc_all_avail() to get >>all years<< data
    (from 2013 as climate strategy score only available since 2013)
"""

def load_n_preproc(year):
    """
    Load all features with sector rev
    Do preproc on data
    return a cleaned database"""
    print("Reading data...")
    df = pd.read_csv("../raw_data/all_features_with_sectorrev.csv")
    df.drop(columns=["Unnamed: 0", "MI_ID", "S&P Credit Rating"], inplace=True)
    df.rename(columns={"Full Time Employees\n(actual)":"Full Time Employees (actual)", "Total Enterprise Value (CIQ)\n($M)":"Total Enterprise Value (CIQ) ($M)"}, inplace=True)
    # df.loc[:, "TCUID"] = df["TCUID"].astype(dtype="int64")
    df = rename_pe(df)
    power_pct_to_clean = ['nuclear_percentage_revenue',
    'thermal_coal_percentage_revenue',
    'ultra_deep_sea_drilling_percentage_revenue',
    'shale_oil_gas_percentage_revenue',
    'coal_percentage_revenue',
    'arctic_drilling_percentage_revenue',
    'oil_sands_percentage_revenue']
    sector_rev_to_clean  = ['Abrasive product manufacturing',
        'Accounting, tax preparation, bookkeeping, and payroll services',
        'Adhesive manufacturing',
        'Advertising and related services',
        'Air and gas compressor manufacturing',
        'Air conditioning, refrigeration, and warm air heating equipment manufacturing',
        'Air purification and ventilation equipment manufacturing',
        'Air transportation',
        'Aircraft engine and engine parts manufacturing',
        'Aircraft manufacturing',
        'Alkalies and chlorine manufacturing',
        'All other basic inorganic chemical manufacturing',
        'All other chemical product and preparation manufacturing',
        'All other converted paper product manufacturing',
        'All other crop farming',
        'All other food manufacturing',
        'All other forging, stamping, and sintering',
        'All other miscellaneous electrical equipment and component manufacturing',
        'All other miscellaneous manufacturing',
        'All other miscellaneous professional, scientific, and technical services',
        'All other miscellaneous wood product manufacturing',
        'All other paper bag and coated and treated paper manufacturing',
        'All other petroleum and coal products manufacturing',
        'All other textile product mills',
        'All other transportation equipment manufacturing',
        'Alumina refining and primary aluminum production',
        'Aluminum product manufacturing from purchased aluminum',
        'Ammunition manufacturing',
        'Amusement parks, arcades, and gambling industries',
        'Analytical laboratory instrument manufacturing',
        'Animal (except poultry) slaughtering, rendering, and processing',
        'Animal production, except cattle and poultry and eggs',
        'Apparel accessories and other apparel manufacturing',
        'Apparel knitting mills',
        'Apparel, Piece Goods, and Notions Wholesalers',
        'Architectural, engineering, and related services',
        'Arms, ordnance, and accessories manufacturing',
        'Artificial and synthetic fibers and filaments manufacturing',
        'Asphalt paving mixture and block manufacturing',
        'Asphalt shingle and coating materials manufacturing',
        'Audio and video equipment manufacturing',
        'Automatic environmental control manufacturing',
        'Automobile manufacturing',
        'Automotive equipment rental and leasing',
        'Automotive repair and maintenance, except car washes',
        'Ball and roller bearing manufacturing',
        'Bare printed circuit board manufacturing',
        'Bauxite Mining',
        'Beet sugar manufacturing',
        'Biological product (except diagnostic) manufacturing',
        'Biomass Power Generation',
        'Bituminous Coal Underground Mining',
        'Bituminous Coal and Lignite Surface Mining',
        'Blind and shade manufacturing',
        'Boat building',
        'Book publishers',
        'Bowling centers',
        'Bread and bakery product manufacturing',
        'Breakfast cereal manufacturing',
        'Breweries',
        'Brick, tile, and other structural clay product manufacturing',
        'Broadcast and wireless communications equipment',
        'Broadwoven fabric mills',
        'Broom, brush, and mop manufacturing',
        'Building Material and Garden Equipment and Supplies Dealers',
        'Business support services',
        'Cable and other subscription programming',
        'Car washes',
        'Carbon and graphite product manufacturing',
        'Carbon black manufacturing',
        'Carpet and rug mills',
        'Cattle ranching and farming',
        'Cement manufacturing',
        'Cheese manufacturing',
        'Child day care services',
        'Chocolate and confectionery manufacturing from cacao beans',
        'Clay and nonclay refractory manufacturing',
        'Clothing and Clothing Accessories Stores',
        'Coal Power Generation',
        'Coated and laminated paper, packaging paper and plastics film manufacturing',
        'Coating, engraving, heat treating and allied activities',
        'Coffee and tea manufacturing',
        'Commercial and industrial machinery and equipment rental and leasing',
        'Commercial and industrial machinery and equipment repair and maintenance',
        'Communication and energy wire and cable manufacturing',
        'Community food, housing, and other relief services, including rehabilitation services',
        'Computer storage device manufacturing',
        'Computer systems design services',
        'Computer terminals and other computer peripheral equipment manufacturing',
        'Concrete pipe, brick, and block manufacturing',
        'Confectionery manufacturing from purchased chocolate',
        'Construction machinery manufacturing',
        'Cookie, cracker, and pasta manufacturing',
        'Copper Mining',
        'Copper rolling, drawing, extruding and alloying',
        'Cotton farming',
        'Couriers and messengers',
        'Crown and closure manufacturing and metal stamping',
        'Crude Petroleum and Natural Gas Extraction',
        'Curtain and linen mills',
        'Custom architectural woodwork and millwork manufacturing',
        'Custom computer programming services',
        'Cut and sew apparel contractors',
        'Cut stone and stone product manufacturing',
        'Cutlery, utensil, pot, and pan manufacturing',
        'Cutting tool and machine tool accessory manufacturing',
        'Dairy cattle and milk production',
        'Data processing, hosting, and related services',
        'Death care services',
        'Dental equipment and supplies manufacturing',
        'Directory, mailing list, and other publishers',
        'Distilleries',
        'Dog and cat food manufacturing',
        'Doll, toy, and game manufacturing',
        'Drilling oil and gas wells',
        'Dry, condensed, and evaporated dairy product manufacturing',
        'Dry-cleaning and laundry services',
        'Electric Bulk Power Transmission and Control',
        'Electric Power Distribution',
        'Electric lamp bulb and part manufacturing',
        'Electrical and Electronic Goods Wholesalers',
        'Electricity and signal testing instruments manufacturing',
        'Electromedical and electrotherapeutic apparatus manufacturing',
        'Electron tube manufacturing',
        'Electronic and precision equipment repair and maintenance',
        'Electronic capacitor, resistor, coil, transformer, and other inductor manufacturing',
        'Electronic computer manufacturing',
        'Electronic connector manufacturing',
        'Electronics and Appliance Stores',
        'Elementary and secondary schools',
        'Employment services',
        'Engineered wood member and truss manufacturing',
        'Environmental and other technical consulting services',
        'Fabric coating mills',
        'Fabricated pipe and pipe fitting manufacturing',
        'Facilities support services',
        'Farm machinery and equipment manufacturing',
        'Fats and oils refining and blending',
        'Ferrous metal foundries',
        'Fertilizer manufacturing',
        'Fiber, yarn, and thread mills',
        'Fishing',
        'Fitness and recreational sports centers',
        'Flat glass manufacturing',
        'Flavoring syrup and concentrate manufacturing',
        'Flour milling and malt manufacturing',
        'Fluid milk and butter manufacturing',
        'Fluid power process machinery',
        'Food services and drinking places',
        'Food, Beverage, Health, and Personal Care Stores',
        'Footwear manufacturing',
        'Forest nurseries, forest products, and timber tracts',
        'Frozen food manufacturing',
        'Fruit and vegetable canning, pickling, and drying',
        'Fruit farming',
        'Funds, trusts, and other financial vehicles',
        'Furniture and Home Furnishings Stores',
        'Gasket, packing, and sealing device manufacturing',
        'Gasoline Stations',
        'General Merchandise Stores',
        'General and consumer goods rental except video tapes and discs',
        'Geothermal Power Generation',
        'Glass container manufacturing',
        'Glass product manufacturing made of purchased glass',
        'Gold Ore Mining',
        'Grain farming',
        'Grantmaking, giving, and social advocacy organizations',
        'Greenhouse, nursery, and floriculture production',
        'Grocery and Related Product Wholesalers',
        'Ground or treated mineral and earth manufacturing',
        'Guided missile and space vehicle manufacturing',
        'Handtool manufacturing',
        'Hardware manufacturing',
        'Heating equipment (except warm air furnaces) manufacturing',
        'Heavy duty truck manufacturing',
        'Home health care services',
        'Hospitals',
        'Hotels and motels, including casino hotels',
        'Household cooking appliance manufacturing',
        'Household laundry equipment manufacturing',
        'Household refrigerator and home freezer manufacturing',
        'Hydroelectric Power Generation',
        'Ice cream and frozen dessert manufacturing',
        'In-vitro diagnostic substance manufacturing',
        'Independent artists, writers, and performers',
        'Individual and family services',
        'Industrial gas manufacturing',
        'Industrial mold manufacturing',
        'Industrial process furnace and oven manufacturing',
        'Industrial process variable instruments manufacturing',
        'Institutional furniture manufacturing',
        'Insurance agencies, brokerages, and related activities',
        'Insurance carriers',
        'Internet publishing and broadcasting',
        'Internet service providers and web search portals',
        'Investigation and security services',
        'Iron and steel mills and ferroalloy manufacturing',
        'Iron ore mining',
        'Irradiation apparatus manufacturing',
        'Jewelry and silverware manufacturing',
        'Junior colleges, colleges, universities, and professional schools',
        'Knit fabric mills',
        'Laminated plastics plate, sheet (except packaging), and shape manufacturing',
        'Landfill Gas Power Generation',
        'Lawn and garden equipment manufacturing',
        'Lead Ore and Zinc Ore Mining',
        'Leather and hide tanning and finishing',
        'Legal services',
        'Lessors of nonfinancial intangible assets',
        'Light truck and utility vehicle manufacturing',
        'Lighting fixture manufacturing',
        'Lime and gypsum product manufacturing',
        'Logging',
        'Lumber and Other Construction Materials Wholesalers',
        'Magnetic and optical recording media manufacturing',
        'Management of companies and enterprises',
        'Management, scientific, and technical consulting services',
        'Manufactured home (mobile home) manufacturing',
        'Material handling equipment manufacturing',
        'Mattress manufacturing',
        'Mechanical power transmission equipment manufacturing',
        'Medical and diagnostic labs and outpatient and other ambulatory care services',
        'Medicinal and botanical manufacturing',
        "Men's and boys' cut and sew apparel manufacturing",
        'Metal and other household furniture manufacturing',
        'Metal can, box, and other metal container (light gauge) manufacturing',
        'Metal cutting and forming machine tool manufacturing',
        'Metal tank (heavy gauge) manufacturing',
        'Military armored vehicle, tank, and tank component manufacturing',
        'Mineral wool manufacturing',
        'Mining and oil and gas field machinery manufacturing',
        'Miscellaneous Durable Goods Wholesalers',
        'Miscellaneous Nondurable Goods Wholesalers',
        'Miscellaneous Store Retailers',
        'Miscellaneous nonmetallic mineral products',
        'Monetary authorities and depository credit intermediation',
        'Motion picture and video industries',
        'Motor Vehicle and Machinery, Equipment, and Supplies Wholesalers',
        'Motor Vehicle and Parts Dealers',
        'Motor and generator manufacturing',
        'Motor home manufacturing',
        'Motor vehicle body manufacturing',
        'Motor vehicle parts manufacturing',
        'Motorcycle, bicycle, and parts manufacturing',
        'Museums, historical sites, zoos, and parks',
        'Musical instrument manufacturing',
        'Narrow fabric mills and schiffli machine embroidery',
        'Natural Gas Liquid Extraction',
        'Natural Gas Power Generation',
        'Natural gas distribution',
        'Newspaper publishers',
        'Nickel Mining',
        'Nonchocolate confectionery manufacturing',
        'Nondepository credit intermediation and related activities',
        'Nonferrous metal (except copper and aluminum) rolling, drawing, extruding and alloying',
        'Nonferrous metal foundries',
        'Nonresidential commercial and health care structures',
        'Nonresidential maintenance and repair',
        'Nonresidential manufacturing structures',
        'Nonstore Retailers',
        'Nonupholstered wood household furniture manufacturing',
        'Nonwoven fabric mills',
        'Nuclear Electric Power Generation',
        'Nursing and residential care facilities',
        'Office administrative services',
        'Office furniture manufacturing',
        'Office supplies (except paper) manufacturing',
        'Offices of physicians, dentists, and other health practitioners',
        'Oilseed farming',
        'Ophthalmic goods manufacturing',
        'Optical instrument and lens manufacturing',
        'Ornamental and architectural metal products manufacturing',
        'Other Electric Power Generation',
        'Other Metal Ore Mining',
        'Other accommodations',
        'Other aircraft parts and auxiliary equipment manufacturing',
        'Other amusement and recreation industries',
        'Other animal food manufacturing',
        'Other basic organic chemical manufacturing',
        'Other commercial and service industry machinery manufacturing',
        'Other communications equipment manufacturing',
        'Other computer related services, including facilities management',
        'Other concrete product manufacturing',
        'Other cut and sew apparel manufacturing',
        'Other educational services',
        'Other electronic component manufacturing',
        'Other engine equipment manufacturing',
        'Other fabricated metal manufacturing',
        'Other general purpose machinery manufacturing',
        'Other industrial machinery manufacturing',
        'Other information services',
        'Other leather and allied product manufacturing',
        'Other major household appliance manufacturing',
        'Other nonmetallic mineral mining and quarrying',
        'Other nonresidential structures',
        'Other personal services',
        'Other plastics product manufacturing',
        'Other pressed and blown glass and glassware manufacturing',
        'Other residential structures',
        'Other rubber product manufacturing',
        'Other support services',
        'Packaging machinery manufacturing',
        'Paint and coating manufacturing',
        'Paper mills',
        'Paperboard Mills',
        'Paperboard container manufacturing',
        'Performing arts companies',
        'Periodical publishers',
        'Personal and household goods repair and maintenance',
        'Personal care services',
        'Pesticide and other agricultural chemical manufacturing',
        'Petrochemical manufacturing',
        'Petroleum Power Generation',
        'Petroleum lubricating oil and grease manufacturing',
        'Petroleum refineries',
        'Petroleum, Chemical, and Allied Products Wholesalers',
        'Pharmaceutical preparation manufacturing',
        'Photographic and photocopying equipment manufacturing',
        'Photographic services',
        'Pipeline transportation',
        'Plastics and rubber industry machinery manufacturing',
        'Plastics bottle manufacturing',
        'Plastics material and resin manufacturing',
        'Plastics packaging materials and unlaminated film and sheet manufacturing',
        'Plastics pipe and pipe fitting manufacturing',
        'Plate work and fabricated structural product manufacturing',
        'Plumbing fixture fitting and trim manufacturing',
        'Polystyrene foam product manufacturing',
        'Postal service',
        'Pottery, ceramics, and plumbing fixture manufacturing',
        'Poultry and egg production',
        'Poultry processing',
        'Power boiler and heat exchanger manufacturing',
        'Power, distribution, and specialty transformer manufacturing',
        'Power-driven handtool manufacturing',
        'Prefabricated wood building manufacturing',
        'Primary battery manufacturing',
        'Primary smelting and refining of copper',
        'Primary smelting and refining of nonferrous metal (except copper and aluminum)',
        'Printed circuit assembly (electronic assembly) manufacturing',
        'Printing',
        'Printing ink manufacturing',
        'Promoters of performing arts and sports and agents for public figures',
        'Propulsion units and parts for space vehicles and guided missiles',
        'Pulp mills',
        'Pump and pumping equipment manufacturing',
        'Radio and television broadcasting',
        'Rail transportation (Diesel)',
        'Rail transportation (Electric)',
        'Railroad rolling stock manufacturing',
        'Ready-mix concrete manufacturing',
        'Real estate',
        'Reconstituted wood product manufacturing',
        'Relay and industrial control manufacturing',
        'Residential maintenance and repair',
        'Residential permanent site single- and multi-family structures',
        'Rolling mill and other metalworking machinery manufacturing',
        'Rubber and plastics hoses and belting manufacturing',
        'Sand, gravel, clay, and ceramic and refractory minerals mining and quarrying',
        'Sanitary paper product manufacturing',
        'Sawmills and wood preservation',
        'Scientific research and development services',
        'Seafood product preparation and packaging',
        'Search, detection, and navigation instruments manufacturing',
        'Seasoning and dressing manufacturing',
        'Secondary smelting and alloying of aluminum',
        'Securities, commodity contracts, investments, and related activities',
        'Semiconductor and related device manufacturing',
        'Semiconductor machinery manufacturing',
        'Services to buildings and dwellings',
        'Ship building and repairing',
        'Showcase, partition, shelving, and locker manufacturing',
        'Sign manufacturing',
        'Small electrical appliance manufacturing',
        'Snack food manufacturing',
        'Soap and cleaning compound manufacturing',
        'Soft drink and ice manufacturing',
        'Software publishers',
        'Software, audio, and video media reproducing',
        'Solar Power Generation',
        'Sound recording industries',
        'Soybean and other oilseed processing',
        'Special tool, die, jig, and fixture manufacturing',
        'Specialized design services',
        'Spectator sports',
        'Speed changer, industrial high-speed drive, and gear manufacturing',
        'Sporting and athletic goods manufacturing',
        'Spring and wire product manufacturing',
        'Stationery product manufacturing',
        'Steel product manufacturing from purchased steel',
        'Stone mining and quarrying',
        'Storage battery manufacturing',
        'Sugar cane mills and refining',
        'Sugarcane and sugar beet farming',
        'Support activities for agriculture and forestry',
        'Support activities for oil and gas operations',
        'Support activities for other mining',
        'Support activities for printing',
        'Support activities for transportation',
        'Surgical and medical instrument manufacturing',
        'Surgical appliance and supplies manufacturing',
        'Switchgear and switchboard apparatus manufacturing',
        'Synthetic dye and pigment manufacturing',
        'Synthetic rubber manufacturing',
        'Tar Sands Extraction',
        'Telecommunications',
        'Telephone apparatus manufacturing',
        'Textile and fabric finishing mills',
        'Textile bag and canvas mills',
        'Tire manufacturing',
        'Tobacco product manufacturing',
        'Toilet preparation manufacturing',
        'Totalizing fluid meters and counting devices manufacturing',
        'Transit and ground passenger transportation',
        'Travel arrangement and reservation services',
        'Travel trailer and camper manufacturing',
        'Tree nut farming',
        'Truck trailer manufacturing',
        'Truck transportation',
        'Turbine and turbine generator set units manufacturing',
        'Turned product and screw, nut, and bolt manufacturing',
        'Unlaminated plastics profile shape manufacturing',
        'Upholstered household furniture manufacturing',
        'Uranium-Radium-Vanadium Ore Mining',
        'Urethane and other foam product (except polystyrene) manufacturing',
        'Valve and fittings other than plumbing',
        'Vegetable and melon farming',
        'Vending, commercial, industrial, and office machinery manufacturing',
        'Veneer and plywood manufacturing',
        'Veterinary services',
        'Warehousing and storage',
        'Waste management and remediation services',
        'Watch, clock, and other measuring and controlling device manufacturing',
        'Water transportation',
        'Water, sewage and other systems',
        'Wave & Tidal Power Generation',
        'Wet corn milling',
        'Wind Power Generation',
        'Wineries',
        'Wiring device manufacturing',
        "Women's and girls' cut and sew apparel manufacturing",
        'Wood container and pallet manufacturing',
        'Wood kitchen cabinet and countertop manufacturing',
        'Wood windows and doors and millwork']

    print("Preproc on power % revenue")
    df = power_pct_cleaning(df, power_pct_to_clean)
    print("Preproc on Sector Revenue")
    df = sector_rev_cleaning(df, sector_rev_to_clean)
    # print("Calculating Employees / revenue...")
    # df = employee(df)
    # print("Cleaning P/E Ratio...")
    # df = pe_cleaning(df)
    print(f"Selecting the year {year} required...")
    year_col = sorted(df.columns[df.columns.str.endswith(f"{year}")])


    print("Dropping rows that are showing NaN on...")
    print(f"-> intensity_scope1CY{year}")
    df.dropna(subset=f"intensity_scope1_CY{year}", inplace=True)
    print(f"-> intensity_scope2CY{year}")
    df.dropna(subset=f"intensity_scope2CY{year}", inplace=True)
    print(f"-> intensity_scope3CY{year}")
    df.dropna(subset=f"intensity_scope3CY{year}", inplace=True)
    print(f"-> Revenue{year}")
    df.dropna(subset=f"revenueCY{year}", inplace=True)


    print("Filling employee numbers with mean value... (subject to change later)")
    df = employee_fill(df)
    print("Filling EV with mean value... (subject to change later)")
    df = ev_fill(df)

    print("Calculating Employees & EV per Revenue...")
    df = employee_rev(df, year=year)
    df = ev_rev(df, year=year)

    print("Filling null Climate Strategy Score with 0...")
    df = c_score_fill(df, year=year)
    print("Cleaning P/E Ratio...")
    df = pe_cleaning(df, year=year)
    df["year"] = year
    col_to_keep =  ["company_name", "TCUID", "year", "Sector", "Employees / Revenue", "EV / Revenue"] + year_col + power_pct_to_clean + sector_rev_to_clean
    df = df[col_to_keep]
    print("Adding Scope 1 and Scope 2 data together...")
    df = scope_1_2_add(df,year)
    print("Doing some column renaming...")
    df = rename_year_col(df,year=year)
    reshuffle_list = df.columns.tolist()[:8] + [df.columns.tolist()[-1]] + df.columns.tolist()[8:-1]
    df = df.reindex(columns=reshuffle_list)
    print(f"Dataset preproc-ed for the year {year}!👍")

    return df

def rename_pe(df):
    pe_col = df.columns[df.columns.str.startswith("pe")].tolist()
    pe_col_rename=[]
    for i in pe_col:
        pe_col_rename.append(i[:8] + i[-4:])
    for num,i in enumerate(pe_col):
        df.rename(columns={pe_col[num]:pe_col_rename[num]}, inplace=True)
    return df

def power_pct_cleaning(df, power_pct_to_clean):
    df.loc[:,power_pct_to_clean] = df[power_pct_to_clean].fillna(0)
    return df

def sector_rev_cleaning(df, sectors):
    df.loc[:,sectors] = df[sectors].fillna(0)
    return df

def employee_fill(df):
    df["Full Time Employees (actual)"].fillna(df["Full Time Employees (actual)"].mean(), inplace=True)
    return df

def ev_fill(df):
    df["Total Enterprise Value (CIQ) ($M)"].fillna(df["Total Enterprise Value (CIQ) ($M)"].mean(), inplace=True)
    return df

def employee_rev(df, year):
    df["Employees / Revenue"] = df["Full Time Employees (actual)"] / df[f"revenueCY{year}"]
    df.drop(columns="Full Time Employees (actual)", inplace=True)
    return df

def ev_rev(df,year):
    df["EV / Revenue"] = df["Total Enterprise Value (CIQ) ($M)"] / df[f"revenueCY{year}"]
    df.drop(columns="Total Enterprise Value (CIQ) ($M)", inplace=True)
    return df

def c_score_fill(df,year):
    df[f"climate_strategy_scoreFY{year}"].fillna(0.,inplace=True)
    return df

def pe_cleaning(df, year):
    df[f"pe_ratio{year}"].fillna(0., inplace=True)
    df[f"pe_ratio{year}"].replace("NM",0., inplace=True)
    df[f"pe_ratio{year}"] = df[f"pe_ratio{year}"].astype(dtype="float64")
    return df

def rename_year_col(df,year):
    year_col = df.columns[df.columns.str.endswith(f"{year}")].tolist()
    for i in year_col:
        df.rename(columns={i:i[:-6]}, inplace=True)
    return df

def scope_1_2_add(df,year):
    df["intensity_1and2"] = df[f"intensity_scope1_CY{year}"] + df[f"intensity_scope2CY{year}"]
    df.drop(columns=[f"intensity_scope1_CY{year}", f"intensity_scope2CY{year}"], inplace=True)
    return df

def load_n_preproc_all_avail():
    years = [2013,2014,2015,2016,2017,2018,2019,2020]
    output = pd.DataFrame()
    for year in years:
        output = pd.concat([output, load_n_preproc(year)])
    return output

if __name__ == '__main__':
    year = 2020
    print("Test - 2020 data preproc")
    load_n_preproc(year)
