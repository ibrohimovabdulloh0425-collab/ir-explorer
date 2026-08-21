"""Lokal countries.json yaratadi — tashqi API kerak emas."""
from __future__ import annotations

import json
from pathlib import Path

# name, cca2, cca3, capital, region, subregion, population, area_km2, lat, lng
RAW = r"""
Afghanistan|AF|AFG|Kabul|Asia|Southern Asia|41128771|652230|33.9391|67.71
Albania|AL|ALB|Tirana|Europe|Southeast Europe|2837743|28748|41.1533|20.1683
Algeria|DZ|DZA|Algiers|Africa|Northern Africa|44903225|2381741|28.0339|1.6596
Andorra|AD|AND|Andorra la Vella|Europe|Southern Europe|79824|468|42.5063|1.5218
Angola|AO|AGO|Luanda|Africa|Middle Africa|35588987|1246700|-11.2027|17.8739
Antigua and Barbuda|AG|ATG|Saint John's|Americas|Caribbean|93763|442|17.0608|-61.7964
Argentina|AR|ARG|Buenos Aires|Americas|South America|46234830|2780400|-38.4161|-63.6167
Armenia|AM|ARM|Yerevan|Asia|Western Asia|2780469|29743|40.0691|45.0382
Australia|AU|AUS|Canberra|Oceania|Australia and New Zealand|26177413|7692024|-25.2744|133.7751
Austria|AT|AUT|Vienna|Europe|Western Europe|9036000|83871|47.5162|14.5501
Azerbaijan|AZ|AZE|Baku|Asia|Western Asia|10353951|86600|40.1431|47.5769
Bahamas|BS|BHS|Nassau|Americas|Caribbean|409984|13943|25.0343|-77.3963
Bahrain|BH|BHR|Manama|Asia|Western Asia|1472233|765|26.0667|50.5577
Bangladesh|BD|BGD|Dhaka|Asia|Southern Asia|171186372|147570|23.685|90.3563
Barbados|BB|BRB|Bridgetown|Americas|Caribbean|281635|430|13.1939|-59.5432
Belarus|BY|BLR|Minsk|Europe|Eastern Europe|9534954|207600|53.7098|27.9534
Belgium|BE|BEL|Brussels|Europe|Western Europe|11655930|30528|50.5039|4.4699
Belize|BZ|BLZ|Belmopan|Americas|Central America|405272|22966|17.1899|-88.4976
Benin|BJ|BEN|Porto-Novo|Africa|Western Africa|13712698|112622|9.3077|2.3158
Bhutan|BT|BTN|Thimphu|Asia|Southern Asia|782455|38394|27.5142|90.4336
Bolivia|BO|BOL|Sucre|Americas|South America|12224110|1098581|-16.2902|-63.5887
Bosnia and Herzegovina|BA|BIH|Sarajevo|Europe|Southeast Europe|3233526|51209|43.9159|17.6791
Botswana|BW|BWA|Gaborone|Africa|Southern Africa|2630296|582000|-22.3285|24.6849
Brazil|BR|BRA|Brasilia|Americas|South America|215313498|8515767|-14.235|-51.9253
Brunei|BN|BRN|Bandar Seri Begawan|Asia|South-Eastern Asia|449002|5765|4.5353|114.7277
Bulgaria|BG|BGR|Sofia|Europe|Southeast Europe|6781953|110879|42.7339|25.4858
Burkina Faso|BF|BFA|Ouagadougou|Africa|Western Africa|22673762|272967|12.2383|-1.5616
Burundi|BI|BDI|Gitega|Africa|Eastern Africa|12889576|27834|-3.3731|29.9189
Cabo Verde|CV|CPV|Praia|Africa|Western Africa|593149|4033|16.5388|-23.0418
Cambodia|KH|KHM|Phnom Penh|Asia|South-Eastern Asia|16718965|181035|12.5657|104.991
Cameroon|CM|CMR|Yaounde|Africa|Middle Africa|27914546|475442|7.3697|12.3547
Canada|CA|CAN|Ottawa|Americas|North America|38781291|9984670|56.1304|-106.3468
Central African Republic|CF|CAF|Bangui|Africa|Middle Africa|5579144|622984|6.6111|20.9394
Chad|TD|TCD|N'Djamena|Africa|Middle Africa|17723315|1284000|15.4542|18.7322
Chile|CL|CHL|Santiago|Americas|South America|19603733|756102|-35.6751|-71.543
China|CN|CHN|Beijing|Asia|Eastern Asia|1412175000|9596961|35.8617|104.1954
Colombia|CO|COL|Bogota|Americas|South America|51874024|1141748|4.5709|-74.2973
Comoros|KM|COM|Moroni|Africa|Eastern Africa|821625|1862|-11.6455|43.3333
Congo|CG|COG|Brazzaville|Africa|Middle Africa|5970424|342000|-0.228|15.8277
Costa Rica|CR|CRI|San Jose|Americas|Central America|5180821|51100|9.7489|-83.7534
Croatia|HR|HRV|Zagreb|Europe|Southeast Europe|4030358|56594|45.1|15.2
Cuba|CU|CUB|Havana|Americas|Caribbean|11212191|109884|21.5218|-77.7812
Cyprus|CY|CYP|Nicosia|Europe|Southern Europe|1251488|9251|35.1264|33.4299
Czechia|CZ|CZE|Prague|Europe|Central Europe|10495295|78865|49.8175|15.473
Democratic Republic of the Congo|CD|COD|Kinshasa|Africa|Middle Africa|99010212|2344858|-4.0383|21.7587
Denmark|DK|DNK|Copenhagen|Europe|Northern Europe|5882261|43094|56.2639|9.5018
Djibouti|DJ|DJI|Djibouti|Africa|Eastern Africa|1120849|23200|11.8251|42.5903
Dominica|DM|DMA|Roseau|Americas|Caribbean|72412|751|15.415|-61.371
Dominican Republic|DO|DOM|Santo Domingo|Americas|Caribbean|11228821|48671|18.7357|-70.1627
Ecuador|EC|ECU|Quito|Americas|South America|18001000|276841|-1.8312|-78.1834
Egypt|EG|EGY|Cairo|Africa|Northern Africa|110990103|1002450|26.8206|30.8025
El Salvador|SV|SLV|San Salvador|Americas|Central America|6336392|21041|13.7942|-88.8965
Equatorial Guinea|GQ|GNQ|Malabo|Africa|Middle Africa|1674908|28051|1.6508|10.2679
Eritrea|ER|ERI|Asmara|Africa|Eastern Africa|3684032|117600|15.1794|39.7823
Estonia|EE|EST|Tallinn|Europe|Northern Europe|1326535|45227|58.5953|25.0136
Eswatini|SZ|SWZ|Mbabane|Africa|Southern Africa|1201670|17364|-26.5225|31.4659
Ethiopia|ET|ETH|Addis Ababa|Africa|Eastern Africa|123379924|1104300|9.145|40.4897
Fiji|FJ|FJI|Suva|Oceania|Melanesia|929766|18272|-17.7134|178.065
Finland|FI|FIN|Helsinki|Europe|Northern Europe|5540720|338424|61.9241|25.7482
France|FR|FRA|Paris|Europe|Western Europe|67750000|551695|46.2276|2.2137
Gabon|GA|GAB|Libreville|Africa|Middle Africa|2388992|267668|-0.8037|11.6094
Gambia|GM|GMB|Banjul|Africa|Western Africa|2705992|11295|13.4432|-15.3101
Georgia|GE|GEO|Tbilisi|Asia|Western Asia|3714000|69700|42.3154|43.3569
Germany|DE|DEU|Berlin|Europe|Western Europe|83200000|357114|51.1657|10.4515
Ghana|GH|GHA|Accra|Africa|Western Africa|33475870|238533|7.9465|-1.0232
Greece|GR|GRC|Athens|Europe|Southern Europe|10430537|131990|39.0742|21.8243
Grenada|GD|GRD|Saint George's|Americas|Caribbean|124610|344|12.1165|-61.679
Guatemala|GT|GTM|Guatemala City|Americas|Central America|17843908|108889|15.7835|-90.2308
Guinea|GN|GIN|Conakry|Africa|Western Africa|13859341|245857|9.9456|-9.6966
Guinea-Bissau|GW|GNB|Bissau|Africa|Western Africa|2105566|36125|11.8037|-15.1804
Guyana|GY|GUY|Georgetown|Americas|South America|808726|214969|4.8604|-58.9302
Haiti|HT|HTI|Port-au-Prince|Americas|Caribbean|11584996|27750|18.9712|-72.2852
Honduras|HN|HND|Tegucigalpa|Americas|Central America|10432860|112492|15.2|-86.2419
Hungary|HU|HUN|Budapest|Europe|Central Europe|9683500|93028|47.1625|19.5033
Iceland|IS|ISL|Reykjavik|Europe|Northern Europe|372520|103000|64.9631|-19.0208
India|IN|IND|New Delhi|Asia|Southern Asia|1417173173|3287590|20.5937|78.9629
Indonesia|ID|IDN|Jakarta|Asia|South-Eastern Asia|275501339|1904569|-0.7893|113.9213
Iran|IR|IRN|Tehran|Asia|Southern Asia|88550570|1648195|32.4279|53.688
Iraq|IQ|IRQ|Baghdad|Asia|Western Asia|44496122|438317|33.2232|43.6793
Ireland|IE|IRL|Dublin|Europe|Northern Europe|5086988|70273|53.1424|-7.6921
Israel|IL|ISR|Jerusalem|Asia|Western Asia|9449000|20770|31.0461|34.8516
Italy|IT|ITA|Rome|Europe|Southern Europe|59037474|301336|41.8719|12.5674
Ivory Coast|CI|CIV|Yamoussoukro|Africa|Western Africa|28160542|322463|7.54|-5.5471
Jamaica|JM|JAM|Kingston|Americas|Caribbean|2825544|10991|18.1096|-77.2975
Japan|JP|JPN|Tokyo|Asia|Eastern Asia|125124989|377975|36.2048|138.2529
Jordan|JO|JOR|Amman|Asia|Western Asia|11285885|89342|30.5852|36.2384
Kazakhstan|KZ|KAZ|Astana|Asia|Central Asia|19800000|2724900|48.0196|66.9237
Kenya|KE|KEN|Nairobi|Africa|Eastern Africa|54027487|580367|-0.0236|37.9062
Kiribati|KI|KIR|Tarawa|Oceania|Micronesia|131232|811|1.4511|-172.0364
Kuwait|KW|KWT|Kuwait City|Asia|Western Asia|4270563|17818|29.3117|47.4818
Kyrgyzstan|KG|KGZ|Bishkek|Asia|Central Asia|7000000|199951|41.2044|74.7661
Laos|LA|LAO|Vientiane|Asia|South-Eastern Asia|7529497|236800|19.8563|102.4955
Latvia|LV|LVA|Riga|Europe|Northern Europe|1883000|64559|56.8796|24.6032
Lebanon|LB|LBN|Beirut|Asia|Western Asia|5489739|10452|33.8547|35.8623
Lesotho|LS|LSO|Maseru|Africa|Southern Africa|2305825|30355|-29.61|28.2336
Liberia|LR|LBR|Monrovia|Africa|Western Africa|5305117|111369|6.4281|-9.4295
Libya|LY|LBY|Tripoli|Africa|Northern Africa|6812341|1759540|26.3351|17.2283
Liechtenstein|LI|LIE|Vaduz|Europe|Western Europe|39327|160|47.166|9.5554
Lithuania|LT|LTU|Vilnius|Europe|Northern Europe|2800839|65300|55.1694|23.8813
Luxembourg|LU|LUX|Luxembourg|Europe|Western Europe|654768|2586|49.8153|6.1296
Madagascar|MG|MDG|Antananarivo|Africa|Eastern Africa|29611714|587041|-18.7669|46.8691
Malawi|MW|MWI|Lilongwe|Africa|Eastern Africa|20405317|118484|-13.2543|34.3015
Malaysia|MY|MYS|Kuala Lumpur|Asia|South-Eastern Asia|33938221|330803|4.2105|101.9758
Maldives|MV|MDV|Male|Asia|Southern Asia|523787|300|3.2028|73.2207
Mali|ML|MLI|Bamako|Africa|Western Africa|22593590|1240192|17.5707|-3.9962
Malta|MT|MLT|Valletta|Europe|Southern Europe|518536|316|35.9375|14.3754
Marshall Islands|MH|MHL|Majuro|Oceania|Micronesia|41569|181|7.1315|171.1845
Mauritania|MR|MRT|Nouakchott|Africa|Western Africa|4736139|1030700|21.0079|-10.9408
Mauritius|MU|MUS|Port Louis|Africa|Eastern Africa|1266041|2040|-20.3484|57.5522
Mexico|MX|MEX|Mexico City|Americas|North America|127504125|1964375|23.6345|-102.5528
Micronesia|FM|FSM|Palikir|Oceania|Micronesia|114164|702|7.4256|150.5508
Moldova|MD|MDA|Chisinau|Europe|Eastern Europe|2620495|33846|47.4116|28.3699
Monaco|MC|MCO|Monaco|Europe|Western Europe|36686|2.02|43.7384|7.4246
Mongolia|MN|MNG|Ulaanbaatar|Asia|Eastern Asia|3398366|1564110|46.8625|103.8467
Montenegro|ME|MNE|Podgorica|Europe|Southeast Europe|627082|13812|42.7087|19.3744
Morocco|MA|MAR|Rabat|Africa|Northern Africa|37457971|446550|31.7917|-7.0926
Mozambique|MZ|MOZ|Maputo|Africa|Eastern Africa|32969518|801590|-18.6657|35.5296
Myanmar|MM|MMR|Naypyidaw|Asia|South-Eastern Asia|54179380|676578|21.9162|95.956
Namibia|NA|NAM|Windhoek|Africa|Southern Africa|2567012|825615|-22.9576|18.4904
Nauru|NR|NRU|Yaren|Oceania|Micronesia|12668|21|-0.5228|166.9315
Nepal|NP|NPL|Kathmandu|Asia|Southern Asia|30547580|147181|28.3949|84.124
Netherlands|NL|NLD|Amsterdam|Europe|Western Europe|17640000|41850|52.1326|5.2913
New Zealand|NZ|NZL|Wellington|Oceania|Australia and New Zealand|5129700|270467|-40.9006|174.886
Nicaragua|NI|NIC|Managua|Americas|Central America|6948392|130373|12.8654|-85.2072
Niger|NE|NER|Niamey|Africa|Western Africa|26207977|1267000|17.6078|8.0817
Nigeria|NG|NGA|Abuja|Africa|Western Africa|218541212|923768|9.082|8.6753
North Korea|KP|PRK|Pyongyang|Asia|Eastern Asia|26069416|120538|40.3393|127.5101
North Macedonia|MK|MKD|Skopje|Europe|Southeast Europe|1836713|25713|41.6086|21.7453
Norway|NO|NOR|Oslo|Europe|Northern Europe|5403021|323802|60.472|8.4689
Oman|OM|OMN|Muscat|Asia|Western Asia|4576298|309500|21.4735|55.9754
Pakistan|PK|PAK|Islamabad|Asia|Southern Asia|235824862|881912|30.3753|69.3451
Palau|PW|PLW|Ngerulmud|Oceania|Micronesia|18092|459|7.515|134.5825
Palestine|PS|PSE|Ramallah|Asia|Western Asia|5250072|6220|31.9522|35.2332
Panama|PA|PAN|Panama City|Americas|Central America|4408581|75417|8.538|-80.7821
Papua New Guinea|PG|PNG|Port Moresby|Oceania|Melanesia|10142629|462840|-6.315|143.9555
Paraguay|PY|PRY|Asuncion|Americas|South America|6780744|406752|-23.4425|-58.4438
Peru|PE|PER|Lima|Americas|South America|34049588|1285216|-9.19|-75.0152
Philippines|PH|PHL|Manila|Asia|South-Eastern Asia|115559662|300000|12.8797|121.774
Poland|PL|POL|Warsaw|Europe|Central Europe|37736508|312679|51.9194|19.1451
Portugal|PT|PRT|Lisbon|Europe|Southern Europe|10290103|92090|39.3999|-8.2245
Qatar|QA|QAT|Doha|Asia|Western Asia|2695122|11586|25.3548|51.1839
Romania|RO|ROU|Bucharest|Europe|Southeast Europe|19053201|238391|45.9432|24.9668
Russia|RU|RUS|Moscow|Europe|Eastern Europe|143400000|17098246|61.524|105.3188
Rwanda|RW|RWA|Kigali|Africa|Eastern Africa|13776698|26338|-1.9403|29.8739
Saint Kitts and Nevis|KN|KNA|Basseterre|Americas|Caribbean|47657|261|17.3578|-62.783
Saint Lucia|LC|LCA|Castries|Americas|Caribbean|179651|616|13.9094|-60.9789
Saint Vincent and the Grenadines|VC|VCT|Kingstown|Americas|Caribbean|103948|389|12.9843|-61.2872
Samoa|WS|WSM|Apia|Oceania|Polynesia|222382|2842|-13.759|-172.1046
San Marino|SM|SMR|San Marino|Europe|Southern Europe|33745|61|43.9424|12.4578
Sao Tome and Principe|ST|STP|Sao Tome|Africa|Middle Africa|227380|964|0.1864|6.6131
Saudi Arabia|SA|SAU|Riyadh|Asia|Western Asia|36408820|2149690|23.8859|45.0792
Senegal|SN|SEN|Dakar|Africa|Western Africa|17316449|196722|14.4974|-14.4524
Serbia|RS|SRB|Belgrade|Europe|Southeast Europe|6834326|88361|44.0165|21.0059
Seychelles|SC|SYC|Victoria|Africa|Eastern Africa|107118|452|-4.6796|55.492
Sierra Leone|SL|SLE|Freetown|Africa|Western Africa|8605718|71740|8.4606|-11.7799
Singapore|SG|SGP|Singapore|Asia|South-Eastern Asia|5637022|710|1.3521|103.8198
Slovakia|SK|SVK|Bratislava|Europe|Central Europe|5447621|49037|48.669|19.699
Slovenia|SI|SVN|Ljubljana|Europe|Central Europe|2108977|20273|46.1512|14.9955
Solomon Islands|SB|SLB|Honiara|Oceania|Melanesia|724273|28896|-9.6457|160.1562
Somalia|SO|SOM|Mogadishu|Africa|Eastern Africa|17597511|637657|5.1521|46.1996
South Africa|ZA|ZAF|Pretoria|Africa|Southern Africa|59893885|1221037|-30.5595|22.9375
South Korea|KR|KOR|Seoul|Asia|Eastern Asia|51784059|100210|35.9078|127.7669
South Sudan|SS|SSD|Juba|Africa|Eastern Africa|10913164|619745|6.877|31.307
Spain|ES|ESP|Madrid|Europe|Southern Europe|47415750|505990|40.4637|-3.7492
Sri Lanka|LK|LKA|Sri Jayawardenepura Kotte|Asia|Southern Asia|22181000|65610|7.8731|80.7718
Sudan|SD|SDN|Khartoum|Africa|Northern Africa|46874204|1861484|12.8628|30.2176
Suriname|SR|SUR|Paramaribo|Americas|South America|618040|163821|3.9193|-56.0278
Sweden|SE|SWE|Stockholm|Europe|Northern Europe|10494247|450295|60.1282|18.6435
Switzerland|CH|CHE|Bern|Europe|Western Europe|8740472|41285|46.8182|8.2275
Syria|SY|SYR|Damascus|Asia|Western Asia|22125249|185180|34.8021|38.9968
Taiwan|TW|TWN|Taipei|Asia|Eastern Asia|23893394|36193|23.6978|120.9605
Tajikistan|TJ|TJK|Dushanbe|Asia|Central Asia|10000000|143100|38.861|71.2761
Tanzania|TZ|TZA|Dodoma|Africa|Eastern Africa|65497748|945087|-6.369|34.8888
Thailand|TH|THA|Bangkok|Asia|South-Eastern Asia|71697030|513120|15.87|100.9925
Timor-Leste|TL|TLS|Dili|Asia|South-Eastern Asia|1341296|14874|-8.8742|125.7275
Togo|TG|TGO|Lome|Africa|Western Africa|8848699|56785|8.6195|0.8248
Tonga|TO|TON|Nuku'alofa|Oceania|Polynesia|106858|747|-21.179|-175.1982
Trinidad and Tobago|TT|TTO|Port of Spain|Americas|Caribbean|1531044|5130|10.6918|-61.2225
Tunisia|TN|TUN|Tunis|Africa|Northern Africa|12356117|163610|33.8869|9.5375
Turkey|TR|TUR|Ankara|Asia|Western Asia|85000000|783562|38.9637|35.2433
Turkmenistan|TM|TKM|Ashgabat|Asia|Central Asia|6400000|488100|38.9697|59.5563
Tuvalu|TV|TUV|Funafuti|Oceania|Polynesia|11312|26|-7.1095|177.6493
Uganda|UG|UGA|Kampala|Africa|Eastern Africa|47249585|241550|1.3733|32.2903
Ukraine|UA|UKR|Kyiv|Europe|Eastern Europe|38000000|603500|48.3794|31.1656
United Arab Emirates|AE|ARE|Abu Dhabi|Asia|Western Asia|9441129|83600|23.4241|53.8478
United Kingdom|GB|GBR|London|Europe|Northern Europe|67000000|242495|55.3781|-3.436
United States|US|USA|Washington, D.C.|Americas|North America|331000000|9833517|37.0902|-95.7129
Uruguay|UY|URY|Montevideo|Americas|South America|3423108|176215|-32.5228|-55.7658
Uzbekistan|UZ|UZB|Tashkent|Asia|Central Asia|36000000|447400|41.3775|64.5853
Vanuatu|VU|VUT|Port Vila|Oceania|Melanesia|326740|12189|-15.3767|166.9592
Vatican City|VA|VAT|Vatican City|Europe|Southern Europe|825|0.44|41.9029|12.4534
Venezuela|VE|VEN|Caracas|Americas|South America|28301696|916445|6.4238|-66.5897
Vietnam|VN|VNM|Hanoi|Asia|South-Eastern Asia|98186856|331212|14.0583|108.2772
Yemen|YE|YEM|Sana'a|Asia|Western Asia|33696614|527968|15.5527|48.5164
Zambia|ZM|ZMB|Lusaka|Africa|Eastern Africa|20017675|752612|-13.1339|27.8493
Zimbabwe|ZW|ZWE|Harare|Africa|Eastern Africa|16320537|390757|-19.0154|29.1549
Kosovo|XK|XKX|Pristina|Europe|Southeast Europe|1786038|10887|42.6026|20.903
Hong Kong|HK|HKG|Hong Kong|Asia|Eastern Asia|7491609|1104|22.3193|114.1694
Macau|MO|MAC|Macau|Asia|Eastern Asia|686607|32.9|22.1987|113.5439
Puerto Rico|PR|PRI|San Juan|Americas|Caribbean|3252407|8870|18.2208|-66.5901
Greenland|GL|GRL|Nuuk|Americas|North America|56653|2166086|71.7069|-42.6043
Faroe Islands|FO|FRO|Torshavn|Europe|Northern Europe|53090|1393|61.8926|-6.9118
Gibraltar|GI|GIB|Gibraltar|Europe|Southern Europe|32669|6.5|36.1408|-5.3536
Bermuda|BM|BMU|Hamilton|Americas|North America|63867|54|32.3078|-64.7505
Cayman Islands|KY|CYM|George Town|Americas|Caribbean|68736|264|19.3133|-81.2546
Isle of Man|IM|IMN|Douglas|Europe|Northern Europe|84584|572|54.2361|-4.5481
Jersey|JE|JEY|Saint Helier|Europe|Northern Europe|110778|116|49.2144|-2.1312
Guernsey|GG|GGY|Saint Peter Port|Europe|Northern Europe|63726|78|49.4482|-2.5895
Aruba|AW|ABW|Oranjestad|Americas|Caribbean|106445|180|12.5211|-69.9683
Curacao|CW|CUW|Willemstad|Americas|Caribbean|191163|444|12.1696|-68.99
Sint Maarten|SX|SXM|Philipsburg|Americas|Caribbean|44198|34|18.0425|-63.0548
American Samoa|AS|ASM|Pago Pago|Oceania|Polynesia|43914|199|-14.271|-170.1322
Guam|GU|GUM|Hagatna|Oceania|Micronesia|168801|549|13.4443|144.7937
Northern Mariana Islands|MP|MNP|Saipan|Oceania|Micronesia|49551|464|15.0979|145.6739
U.S. Virgin Islands|VI|VIR|Charlotte Amalie|Americas|Caribbean|100091|347|18.3358|-64.8963
British Virgin Islands|VG|VGB|Road Town|Americas|Caribbean|31122|151|18.4207|-64.64
New Caledonia|NC|NCL|Noumea|Oceania|Melanesia|289931|18575|-20.9043|165.618
French Polynesia|PF|PYF|Papeete|Oceania|Polynesia|306279|4167|-17.6797|-149.4068
Wallis and Futuna|WF|WLF|Mata-Utu|Oceania|Polynesia|11558|142|-13.7684|-177.1561
Cook Islands|CK|COK|Avarua|Oceania|Polynesia|17044|236|-21.2367|-159.7777
Niue|NU|NIU|Alofi|Oceania|Polynesia|1937|260|-19.0544|-169.8672
Tokelau|TK|TKL|Fakaofo|Oceania|Polynesia|1871|12|-9.2002|-171.8484
Anguilla|AI|AIA|The Valley|Americas|Caribbean|15835|91|18.2206|-63.0686
Montserrat|MS|MSR|Plymouth|Americas|Caribbean|4390|102|16.7425|-62.1874
Turks and Caicos Islands|TC|TCA|Cockburn Town|Americas|Caribbean|45714|948|21.694|-71.7979
Falkland Islands|FK|FLK|Stanley|Americas|South America|3764|12173|-51.7963|-59.5236
Saint Pierre and Miquelon|PM|SPM|Saint-Pierre|Americas|North America|5888|242|46.8852|-56.3159
Saint Helena|SH|SHN|Jamestown|Africa|Western Africa|5401|394|-15.965|-5.7089
British Indian Ocean Territory|IO|IOT|Diego Garcia|Africa|Eastern Africa|3000|60|-7.3195|72.4229
Mayotte|YT|MYT|Mamoudzou|Africa|Eastern Africa|310259|374|-12.8275|45.1662
Reunion|RE|REU|Saint-Denis|Africa|Eastern Africa|908061|2511|-21.1151|55.5364
Martinique|MQ|MTQ|Fort-de-France|Americas|Caribbean|375265|1128|14.6415|-61.0242
Guadeloupe|GP|GLP|Basse-Terre|Americas|Caribbean|396051|1628|16.265|-61.551
French Guiana|GF|GUF|Cayenne|Americas|South America|301099|83534|3.9339|-53.1258
Saint Barthelemy|BL|BLM|Gustavia|Americas|Caribbean|10967|21|17.9|-62.8333
Saint Martin|MF|MAF|Marigot|Americas|Caribbean|32556|53|18.0708|-63.0501
Aland Islands|AX|ALA|Mariehamn|Europe|Northern Europe|30129|1583|60.1785|19.9156
Svalbard and Jan Mayen|SJ|SJM|Longyearbyen|Europe|Northern Europe|2939|62045|78.2186|15.6401
Western Sahara|EH|ESH|Laayoune|Africa|Northern Africa|565581|266000|24.2155|-12.8858
Antarctica|AQ|ATA||Antarctic|Antarctica|1100|14000000|-75.2509|-0.0714
Bouvet Island|BV|BVT||Antarctic|Antarctica|0|49|-54.4208|3.3464
Heard Island and McDonald Islands|HM|HMD||Antarctic|Antarctica|0|412|-53.0818|73.5042
South Georgia|GS|SGS|King Edward Point|Americas|South America|30|3903|-54.4296|-36.5879
French Southern Territories|TF|ATF|Port-aux-Francais|Antarctic|Antarctica|400|7747|-49.2804|69.3486
United States Minor Outlying Islands|UM|UMI||Oceania|Micronesia|300|34|19.2823|166.647
Christmas Island|CX|CXR|Flying Fish Cove|Oceania|Australia and New Zealand|1985|135|-10.4475|105.6904
Cocos Islands|CC|CCK|West Island|Oceania|Australia and New Zealand|596|14|-12.1642|96.871
Norfolk Island|NF|NFK|Kingston|Oceania|Australia and New Zealand|1748|36|-29.0408|167.9547
Pitcairn Islands|PN|PCN|Adamstown|Oceania|Polynesia|47|47|-24.3768|-128.3242
Caribbean Netherlands|BQ|BES|Kralendijk|Americas|Caribbean|27148|328|12.1784|-68.2385
"""

UZBEK_NAMES = {
    "UZ": ("O'zbekiston", "Toshkent"),
    "KZ": ("Qozog'iston", "Ostona"),
    "KG": ("Qirg'iziston", "Bishkek"),
    "TJ": ("Tojikiston", "Dushanbe"),
    "TM": ("Turkmaniston", "Ashxobod"),
    "TR": ("Turkiya", "Anqara"),
    "CN": ("Xitoy", "Pekin"),
    "RU": ("Rossiya", "Moskva"),
    "US": ("AQSH", "Vashington"),
    "FR": ("Fransiya", "Parij"),
    "DE": ("Olmanya", "Berlin"),
    "GB": ("Buyuk Britaniya", "London"),
}


def build_countries() -> list[dict]:
    countries: list[dict] = []
    seen: set[str] = set()
    for line in RAW.strip().splitlines():
        parts = line.split("|")
        if len(parts) != 10:
            raise ValueError(f"Bad line: {line}")
        name, cca2, cca3, capital, region, subregion, pop, area, lat, lng = parts
        if cca2 in seen:
            raise ValueError(f"Duplicate cca2: {cca2}")
        seen.add(cca2)
        if cca2 in UZBEK_NAMES:
            name, capital = UZBEK_NAMES[cca2]
        countries.append(
            {
                "name": name,
                "cca2": cca2,
                "cca3": cca3,
                "capital": capital or None,
                "region": region,
                "subregion": subregion,
                "population": int(float(pop)),
                "area": float(area),
                "flag_png": f"https://flagcdn.com/w320/{cca2.lower()}.png",
                "lat": float(lat),
                "lng": float(lng),
            }
        )
    return countries


def main() -> None:
    countries = build_countries()
    out = Path(__file__).with_name("countries.json")
    out.write_text(json.dumps(countries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(countries)} countries to {out}")


if __name__ == "__main__":
    main()
