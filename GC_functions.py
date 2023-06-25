def topla(a=0,b=0):
    return a+b

def group_finder(gc_lat,gc_lon,site_list,k):
    import gc_functions as gc
    (min_site, min_dist, lat_alpha, lon_alpha) = gc.minumum_distance_finder(len(site_list), gc_lat, gc_lon, site_list)
    site_list_r1 = site_list[site_list.Sarf != min_site]
    # print(site_list_r1)
    (a1_site, a1_dist, a1_lat, a1_lon) = gc.minumum_distance_finder(len(site_list_r1), lat_alpha, lon_alpha,site_list_r1)
    site_list_r2 = site_list_r1[site_list_r1.Sarf != a1_site]
    # print(site_list_r2)
    (a2_site, a2_dist, a2_lat, a2_lon) = gc.minumum_distance_finder(len(site_list_r2), lat_alpha, lon_alpha,site_list_r2)
    site_list_r3 = site_list_r2[site_list_r2.Sarf != a2_site]
    (a3_site, a3_dist, a3_lat, a3_lon) = gc.minumum_distance_finder(len(site_list_r3), lat_alpha, lon_alpha,site_list_r3)
    site_list_r4 = site_list_r3[site_list_r3.Sarf != a3_site]

    return min_site,min_dist,a1_site,a1_dist,a2_site,a2_dist,a3_site,a3_dist,site_list_r4

def group_finder_alg_8(ave_lat,ave_lon,site_list):
    import GC_functions as gc
    import pandas as pd



    (min_site, min_dist, lat_alpha, lon_alpha) = gc.minumum_distance_finder(len(site_list), ave_lat, ave_lon, site_list)
    site_list_r1 = site_list[site_list.Sarf != min_site]
    # print(site_list_r1)
    (a1_site, a1_dist, a1_lat, a1_lon) = gc.minumum_distance_finder(len(site_list_r1), lat_alpha, lon_alpha,site_list_r1)
    site_list_r2 = site_list_r1[site_list_r1.Sarf != a1_site]
    # print(site_list_r2)
    (a2_site, a2_dist, a2_lat, a2_lon) = gc.minumum_distance_finder(len(site_list_r2), lat_alpha, lon_alpha,site_list_r2)
    site_list_r3 = site_list_r2[site_list_r2.Sarf != a2_site]
    (a3_site, a3_dist, a3_lat, a3_lon) = gc.minumum_distance_finder(len(site_list_r3), lat_alpha, lon_alpha,site_list_r3)
    site_list_r4 = site_list_r3[site_list_r3.Sarf != a3_site]
    (a4_site, a4_dist, a4_lat, a4_lon) = gc.minumum_distance_finder(len(site_list_r4), lat_alpha, lon_alpha,site_list_r4)
    site_list_r5 = site_list_r4[site_list_r4.Sarf != a4_site]
    (a5_site, a5_dist, a5_lat, a5_lon) = gc.minumum_distance_finder(len(site_list_r5), lat_alpha, lon_alpha,site_list_r5)
    site_list_r6 = site_list_r5[site_list_r5.Sarf != a5_site]
    (a6_site, a6_dist, a6_lat, a6_lon) = gc.minumum_distance_finder(len(site_list_r6), lat_alpha, lon_alpha,site_list_r6)
    site_list_r7 = site_list_r6[site_list_r6.Sarf != a6_site]
    (a7_site, a7_dist, a7_lat, a7_lon) = gc.minumum_distance_finder(len(site_list_r7), lat_alpha, lon_alpha,site_list_r7)
    site_list_r8 = site_list_r7[site_list_r7.Sarf != a7_site]

    data = {'Sarf': [min_site, a1_site, a2_site, a3_site, a4_site, a5_site, a6_site,a7_site], 'lat': [lat_alpha, a1_lat, a2_lat, a3_lat, a4_lat, a5_lat, a6_lat,a7_lat],'lon': [lon_alpha, a1_lon, a2_lon, a3_lon, a4_lon, a5_lon, a6_lon,a7_lon]}
    site8_df = pd.DataFrame(data)
    lat_ave_g8 = site8_df["lat"].mean()
    lon_ave_g8 = site8_df["lon"].mean()

    # print(site8_df)

    (min_site_g8, min_dist_g8, lat_min_g8, lon_min_g8) = gc.minumum_distance_finder(len(site8_df), lat_ave_g8, lon_ave_g8, site8_df)
    site_list_r1_g8 = site8_df[site8_df.Sarf != min_site_g8]

    (a1_site_g8, a1_dist_g8, a1_lat_g8, a1_lon_g8) = gc.minumum_distance_finder(len(site_list_r1_g8), lat_min_g8, lon_min_g8,site_list_r1_g8)
    site_list_r2_g8 = site_list_r1_g8[site_list_r1_g8.Sarf != a1_site_g8]

    (a2_site_g8, a2_dist_g8, a2_lat_g8, a2_lon_g8) = gc.minumum_distance_finder(len(site_list_r2_g8), lat_min_g8, lon_min_g8,site_list_r2_g8)
    site_list_r3_g8 = site_list_r2_g8[site_list_r2_g8.Sarf != a2_site_g8]

    (a3_site_g8, a3_dist_g8, a3_lat_g8, a3_lon_g8) = gc.minumum_distance_finder(len(site_list_r3_g8), lat_min_g8, lon_min_g8,site_list_r3_g8)
    site_list_r4_g8 = site_list_r3_g8[site_list_r3_g8.Sarf != a3_site_g8]

    selected_4 = {'Sarf': [min_site_g8, a1_site_g8, a2_site_g8, a3_site_g8], 'lat': [lat_min_g8, a1_lat_g8, a2_lat_g8, a3_lat_g8], 'lon': [lon_min_g8, a1_lon_g8, a2_lon_g8, a3_lon_g8]}
    selected_4_df = pd.DataFrame(selected_4 )

    site_list_reduced1 = site_list[site_list.Sarf != min_site_g8]
    site_list_reduced2 = site_list_reduced1[site_list_reduced1.Sarf != a1_site_g8]
    site_list_reduced3 = site_list_reduced2[site_list_reduced2.Sarf != a2_site_g8]
    site_list_reduced4 = site_list_reduced3[site_list_reduced3.Sarf != a3_site_g8]

    # print(selected_4_df)
    # print(site_list_reduced4)

    # print(len(site_list_reduced4))

    return min_site_g8,min_dist_g8,a1_site_g8,a1_dist_g8,a2_site_g8,a2_dist_g8,a3_site_g8,a3_dist_g8,site_list_reduced4

def distance_calculator(lat1,lon1,lat2,lon2):
    import math
    lat1 = lat1 * math.pi / 180
    lon1 = lon1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    lon2 = lon2 * math.pi / 180

    x = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)

    if (lon1 == lon2) and (lat1 == lat2) or (x == 0) or ( math.sqrt(-x * x + 1) == 0):
        dist = 0
    else:
        y = math.atan( -x/math.sqrt(-x * x + 1) ) + 2 * math.atan(1)
        dist = y * 6371.1
    return dist

def minumum_distance_finder(len,lat1,lon1,site_list):
    import GC_functions as gc
    min_dist = 100000
    min_site = "NNA1301000AAA"
    lat_min = 0
    lon_min = 0

    for i in range(0, len):
        cell = site_list.iloc[i]
        site = cell[0]
        lat = cell[1]
        lon = cell[2]
        dist = gc.distance_calculator(lat1, lon1, lat, lon)
        if (dist < min_dist):
            min_dist = dist
            min_site = site
            lat_min = lat
            lon_min = lon
    return min_site,min_dist,lat_min,lon_min

def creating_duos(site_df, max_dist_allowed):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    no_of_sites = len(site_df)
    i = 0
    Duo_table = pd.DataFrame(columns=['Site1', 'Site2', 'Duo1_lat', 'Duo1_lon'],
                               index=range(0, no_of_sites))

    while len(site_df) > 1:

        site_df = site_df.sort_values(by=['lat'], ascending=False)

        ref_site = site_df.iloc[0]
        ref_lat = site_df.iloc[0, 1]
        ref_lon = site_df.iloc[0, 2]

        site_df['ref_lat'] = site_df.iloc[0, 1]
        site_df['ref_lon'] = site_df.iloc[0, 2]
        site_df['ref_dist'] = site_df.apply(lambda row: gc.distance_calculator(row['ref_lat'], row['ref_lon'], row['lat'], row['lon']), axis=1)

        site_df = site_df.drop(site_df.index[0])

        site_df = site_df.drop(columns=["ref_lat", "ref_lon"])
        site_df = site_df.sort_values(by=['ref_dist'])
        dist = site_df.iloc[0, 4]

        if dist < max_dist_allowed:
            Duo_table.iloc[i, 0] = ref_site[0]
            Duo_table.iloc[i, 1] = site_df.iloc[0, 0]
            Duo_table.iloc[i, 2] = np.mean([ref_lat, site_df.iloc[0, 1]])
            Duo_table.iloc[i, 3] = np.mean([ref_lon, site_df.iloc[0, 2]])
            site_df = site_df.drop(site_df.index[0])
        else:
            Duo_table.iloc[i, 0] = ref_site[0]
            Duo_table.iloc[i, 1] = 'isolated'
            Duo_table.iloc[i, 2] = ref_site[1]
            Duo_table.iloc[i, 3] = ref_site[2]

        if len(site_df) == 1:
            Duo_table.iloc[i+1, 0] = site_df.iloc[0,0]
            Duo_table.iloc[i+1, 1] = 'isolated'
            Duo_table.iloc[i+1, 2] = site_df.iloc[0,1]
            Duo_table.iloc[i+1, 3] = site_df.iloc[0,2]
        i = i + 1
    a = Duo_table['Site1'].isnull()
    Duo_table = Duo_table.drop(Duo_table.index[a])

    return Duo_table

def creating_groups(Duo_df,max_dist_allowed):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    no_of_groups = len(Duo_df)
    i = 0

    Group_table = pd.DataFrame(columns=['Site1', 'Site2','Site3', 'Site4', 'Group_lat', 'Group_lon'],index=range(0,no_of_groups))

    while len(Duo_df) > 1:

        Duo_df = Duo_df.sort_values(by=['Duo1_lat'], ascending=False)
        ref_duo = Duo_df.iloc[0]

        if ref_duo[1] == 'isolated':
            Group_table.iloc[i, 0] = ref_duo[0]
            Group_table.iloc[i, 1] = 'isolated'
            Group_table.iloc[i, 2] = 'isolated'
            Group_table.iloc[i, 3] = 'isolated'
            Group_table.iloc[i, 4] = ref_duo[2]
            Group_table.iloc[i, 5] = ref_duo[3]
            Duo_df = Duo_df.drop(Duo_df.index[0])

        else:
            ref_lat = Duo_df.iloc[0, 2]
            ref_lon = Duo_df.iloc[0, 3]

            Duo_df['ref_lat'] = Duo_df.iloc[0, 2]
            Duo_df['ref_lon'] = Duo_df.iloc[0, 3]
            Duo_df['ref_dist'] = Duo_df.apply(lambda row: gc.distance_calculator(row['ref_lat'], row['ref_lon'], row['Duo1_lat'], row['Duo1_lon']), axis=1)
            Duo_df = Duo_df.drop(Duo_df.index[0])

            Duo_df = Duo_df.drop(columns=["ref_lat", "ref_lon"])
            Duo_df = Duo_df.sort_values(by=['ref_dist'])
            dist = Duo_df.iloc[0, 4]

            if dist < max_dist_allowed:
                Group_table.iloc[i, 0] = ref_duo[0]
                Group_table.iloc[i, 1] = ref_duo[1]
                Group_table.iloc[i, 2] = Duo_df.iloc[0,0]
                Group_table.iloc[i, 3] = Duo_df.iloc[0,1]
                Group_table.iloc[i, 4] = np.mean([ref_lat, Duo_df.iloc[0, 2]])
                Group_table.iloc[i, 5] = np.mean([ref_lon, Duo_df.iloc[0, 3]])
                Duo_df = Duo_df.drop(Duo_df.index[0])
            else:
                Group_table.iloc[i, 0] = ref_duo[0]
                Group_table.iloc[i, 1] = ref_duo[1]
                Group_table.iloc[i, 2] = 'isolated'
                Group_table.iloc[i, 3] = 'isolated'
                Group_table.iloc[i, 4] = ref_duo[2]
                Group_table.iloc[i, 5] = ref_duo[3]
        if len(Duo_df) == 1:
            Group_table.iloc[i+1, 0] = Duo_df.iloc[0,0]
            Group_table.iloc[i+1, 1] = Duo_df.iloc[0,1]
            Group_table.iloc[i+1, 2] = 'isolated'
            Group_table.iloc[i+1, 3] = 'isolated'
            Group_table.iloc[i+1, 4] = Duo_df.iloc[0,2]
            Group_table.iloc[i+1, 5] = Duo_df.iloc[0,3]

        i = i + 1

    # print(i)
    a = Group_table['Site1'].isnull()
    Group_table = Group_table.drop(Group_table.index[a])

    return Group_table

def Output_format_1(Group_table,no_of_sites):
    import pandas as pd
    import GC_functions as gc
    import numpy as np
    n = len(Group_table)

    Output_table = pd.DataFrame(columns=['Sarf', 'group'],index=range(0, 4*n))
    for i in range(0,n):
        Output_table.iloc[i, 0] = Group_table.iloc[i, 0]
        Output_table.iloc[i, 1] = i+1
    for i in range(0,n):
        Output_table.iloc[i+n, 0] = Group_table.iloc[i, 1]
        Output_table.iloc[i+n, 1] = i+1
    for i in range(0, n):
        Output_table.iloc[i + 2*n, 0] = Group_table.iloc[i, 2]
        Output_table.iloc[i + 2*n, 1] = i+1
    for i in range(0, n):
        Output_table.iloc[i + 3 * n, 0] = Group_table.iloc[i, 3]
        Output_table.iloc[i + 3 * n, 1] = i+1

    Output_table = Output_table.drop(Output_table[Output_table['Sarf'] == 'isolated'].index)

    Output_table1 = Output_table
    Output_table2 = Output_table
    Output_table3 = Output_table

    Output_table1['Cell'] = Output_table1['Sarf'] + "_1"
    a = Output_table1.copy()
    Output_table2['Cell'] = Output_table2['Sarf'] + "_2"
    b = Output_table2.copy()
    Output_table3['Cell'] = Output_table3['Sarf'] + "_3"
    c = Output_table3.copy()

    a = a.append(b)
    a = a.append(c)

    return a

def Output_format(Group_table,no_of_sites):
    import pandas as pd
    import GC_functions as gc
    import numpy as np
    n = len(Group_table)
    # random_group = np.random.choice(range(n), n, replace=False)
    random_group = np.arange((n-1),-1, -1)
    # print(random_group)
    Output_table = pd.DataFrame(columns=['Sarf', 'group'],index=range(0, 4*n))
    for i in range(0,n):
        Output_table.iloc[i, 0] = Group_table.iloc[i, 0]
        Output_table.iloc[i, 1] = random_group[i] + 1
    for i in range(0,n):
        Output_table.iloc[i+n, 0] = Group_table.iloc[i, 1]
        Output_table.iloc[i+n, 1] = random_group[i] + 1
    for i in range(0, n):
        Output_table.iloc[i + 2*n, 0] = Group_table.iloc[i, 2]
        Output_table.iloc[i + 2*n, 1] = random_group[i] + 1
    for i in range(0, n):
        Output_table.iloc[i + 3 * n, 0] = Group_table.iloc[i, 3]
        Output_table.iloc[i + 3 * n, 1] = random_group[i] + 1

    Output_table = Output_table.drop(Output_table[Output_table['Sarf'] == 'isolated'].index)

    return Output_table

def creating_duos_south(site_df, max_dist_allowed):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    no_of_sites = len(site_df)
    i = 0
    Duo_table = pd.DataFrame(columns=['Site1', 'Site2', 'Duo1_lat', 'Duo1_lon'],
                               index=range(0, no_of_sites))

    while len(site_df) > 1:

        site_df = site_df.sort_values(by=['lat'], ascending=True)

        ref_site = site_df.iloc[0]
        ref_lat = site_df.iloc[0, 1]
        ref_lon = site_df.iloc[0, 2]

        site_df['ref_lat'] = site_df.iloc[0, 1]
        site_df['ref_lon'] = site_df.iloc[0, 2]
        site_df['ref_dist'] = site_df.apply(lambda row: gc.distance_calculator(row['ref_lat'], row['ref_lon'], row['lat'], row['lon']), axis=1)

        site_df = site_df.drop(site_df.index[0])

        site_df = site_df.drop(columns=["ref_lat", "ref_lon"])
        site_df = site_df.sort_values(by=['ref_dist'])
        dist = site_df.iloc[0, 4]

        if dist < max_dist_allowed:
            Duo_table.iloc[i, 0] = ref_site[0]
            Duo_table.iloc[i, 1] = site_df.iloc[0, 0]
            Duo_table.iloc[i, 2] = np.mean([ref_lat, site_df.iloc[0, 1]])
            Duo_table.iloc[i, 3] = np.mean([ref_lon, site_df.iloc[0, 2]])
            site_df = site_df.drop(site_df.index[0])
        else:
            Duo_table.iloc[i, 0] = ref_site[0]
            Duo_table.iloc[i, 1] = 'isolated'
            Duo_table.iloc[i, 2] = ref_site[1]
            Duo_table.iloc[i, 3] = ref_site[2]

        if len(site_df) == 1:
            Duo_table.iloc[i+1, 0] = site_df.iloc[0,0]
            Duo_table.iloc[i+1, 1] = 'isolated'
            Duo_table.iloc[i+1, 2] = site_df.iloc[0,1]
            Duo_table.iloc[i+1, 3] = site_df.iloc[0,2]
        i = i + 1
    a = Duo_table['Site1'].isnull()
    Duo_table = Duo_table.drop(Duo_table.index[a])

    return Duo_table

def creating_groups_south(Duo_df,max_dist_allowed):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    no_of_groups = len(Duo_df)
    i = 0

    Group_table = pd.DataFrame(columns=['Site1', 'Site2','Site3', 'Site4', 'Group_lat', 'Group_lon'],index=range(0,no_of_groups))

    while len(Duo_df) > 1:

        Duo_df = Duo_df.sort_values(by=['Duo1_lat'], ascending=True)
        ref_duo = Duo_df.iloc[0]

        if ref_duo[1] == 'isolated':
            Group_table.iloc[i, 0] = ref_duo[0]
            Group_table.iloc[i, 1] = 'isolated'
            Group_table.iloc[i, 2] = 'isolated'
            Group_table.iloc[i, 3] = 'isolated'
            Group_table.iloc[i, 4] = ref_duo[2]
            Group_table.iloc[i, 5] = ref_duo[3]
            Duo_df = Duo_df.drop(Duo_df.index[0])

        else:
            ref_lat = Duo_df.iloc[0, 2]
            ref_lon = Duo_df.iloc[0, 3]

            Duo_df['ref_lat'] = Duo_df.iloc[0, 2]
            Duo_df['ref_lon'] = Duo_df.iloc[0, 3]
            Duo_df['ref_dist'] = Duo_df.apply(lambda row: gc.distance_calculator(row['ref_lat'], row['ref_lon'], row['Duo1_lat'], row['Duo1_lon']), axis=1)
            Duo_df = Duo_df.drop(Duo_df.index[0])

            Duo_df = Duo_df.drop(columns=["ref_lat", "ref_lon"])
            Duo_df = Duo_df.sort_values(by=['ref_dist'])
            dist = Duo_df.iloc[0, 4]

            if dist < max_dist_allowed:
                Group_table.iloc[i, 0] = ref_duo[0]
                Group_table.iloc[i, 1] = ref_duo[1]
                Group_table.iloc[i, 2] = Duo_df.iloc[0,0]
                Group_table.iloc[i, 3] = Duo_df.iloc[0,1]
                Group_table.iloc[i, 4] = np.mean([ref_lat, Duo_df.iloc[0, 2]])
                Group_table.iloc[i, 5] = np.mean([ref_lon, Duo_df.iloc[0, 3]])
                Duo_df = Duo_df.drop(Duo_df.index[0])
            else:
                Group_table.iloc[i, 0] = ref_duo[0]
                Group_table.iloc[i, 1] = ref_duo[1]
                Group_table.iloc[i, 2] = 'isolated'
                Group_table.iloc[i, 3] = 'isolated'
                Group_table.iloc[i, 4] = ref_duo[2]
                Group_table.iloc[i, 5] = ref_duo[3]
        if len(Duo_df) == 1:
            Group_table.iloc[i+1, 0] = Duo_df.iloc[0,0]
            Group_table.iloc[i+1, 1] = Duo_df.iloc[0,1]
            Group_table.iloc[i+1, 2] = 'isolated'
            Group_table.iloc[i+1, 3] = 'isolated'
            Group_table.iloc[i+1, 4] = Duo_df.iloc[0,2]
            Group_table.iloc[i+1, 5] = Duo_df.iloc[0,3]

        i = i + 1

    # print(i)
    a = Group_table['Site1'].isnull()
    Group_table = Group_table.drop(Group_table.index[a])

    return Group_table

def creating_duos_west(site_df, max_dist_allowed):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    no_of_sites = len(site_df)
    i = 0
    Duo_table = pd.DataFrame(columns=['Site1', 'Site2', 'Duo1_lat', 'Duo1_lon'],
                               index=range(0, no_of_sites))

    while len(site_df) > 1:

        site_df = site_df.sort_values(by=['lon'], ascending=False)

        ref_site = site_df.iloc[0]
        ref_lat = site_df.iloc[0, 1]
        ref_lon = site_df.iloc[0, 2]

        site_df['ref_lat'] = site_df.iloc[0, 1]
        site_df['ref_lon'] = site_df.iloc[0, 2]
        site_df['ref_dist'] = site_df.apply(lambda row: gc.distance_calculator(row['ref_lat'], row['ref_lon'], row['lat'], row['lon']), axis=1)

        site_df = site_df.drop(site_df.index[0])

        site_df = site_df.drop(columns=["ref_lat", "ref_lon"])
        site_df = site_df.sort_values(by=['ref_dist'])
        dist = site_df.iloc[0, 4]

        if dist < max_dist_allowed:
            Duo_table.iloc[i, 0] = ref_site[0]
            Duo_table.iloc[i, 1] = site_df.iloc[0, 0]
            Duo_table.iloc[i, 2] = np.mean([ref_lat, site_df.iloc[0, 1]])
            Duo_table.iloc[i, 3] = np.mean([ref_lon, site_df.iloc[0, 2]])
            site_df = site_df.drop(site_df.index[0])
        else:
            Duo_table.iloc[i, 0] = ref_site[0]
            Duo_table.iloc[i, 1] = 'isolated'
            Duo_table.iloc[i, 2] = ref_site[1]
            Duo_table.iloc[i, 3] = ref_site[2]

        if len(site_df) == 1:
            Duo_table.iloc[i+1, 0] = site_df.iloc[0,0]
            Duo_table.iloc[i+1, 1] = 'isolated'
            Duo_table.iloc[i+1, 2] = site_df.iloc[0,1]
            Duo_table.iloc[i+1, 3] = site_df.iloc[0,2]
        i = i + 1
    a = Duo_table['Site1'].isnull()
    Duo_table = Duo_table.drop(Duo_table.index[a])

    return Duo_table

def creating_groups_west(Duo_df,max_dist_allowed):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    no_of_groups = len(Duo_df)
    i = 0

    Group_table = pd.DataFrame(columns=['Site1', 'Site2','Site3', 'Site4', 'Group_lat', 'Group_lon'],index=range(0,no_of_groups))

    while len(Duo_df) > 1:

        Duo_df = Duo_df.sort_values(by=['Duo1_lon'], ascending=False)
        ref_duo = Duo_df.iloc[0]

        if ref_duo[1] == 'isolated':
            Group_table.iloc[i, 0] = ref_duo[0]
            Group_table.iloc[i, 1] = 'isolated'
            Group_table.iloc[i, 2] = 'isolated'
            Group_table.iloc[i, 3] = 'isolated'
            Group_table.iloc[i, 4] = ref_duo[2]
            Group_table.iloc[i, 5] = ref_duo[3]
            Duo_df = Duo_df.drop(Duo_df.index[0])

        else:
            ref_lat = Duo_df.iloc[0, 2]
            ref_lon = Duo_df.iloc[0, 3]

            Duo_df['ref_lat'] = Duo_df.iloc[0, 2]
            Duo_df['ref_lon'] = Duo_df.iloc[0, 3]
            Duo_df['ref_dist'] = Duo_df.apply(lambda row: gc.distance_calculator(row['ref_lat'], row['ref_lon'], row['Duo1_lat'], row['Duo1_lon']), axis=1)
            Duo_df = Duo_df.drop(Duo_df.index[0])

            Duo_df = Duo_df.drop(columns=["ref_lat", "ref_lon"])
            Duo_df = Duo_df.sort_values(by=['ref_dist'])
            dist = Duo_df.iloc[0, 4]

            if dist < max_dist_allowed:
                Group_table.iloc[i, 0] = ref_duo[0]
                Group_table.iloc[i, 1] = ref_duo[1]
                Group_table.iloc[i, 2] = Duo_df.iloc[0,0]
                Group_table.iloc[i, 3] = Duo_df.iloc[0,1]
                Group_table.iloc[i, 4] = np.mean([ref_lat, Duo_df.iloc[0, 2]])
                Group_table.iloc[i, 5] = np.mean([ref_lon, Duo_df.iloc[0, 3]])
                Duo_df = Duo_df.drop(Duo_df.index[0])
            else:
                Group_table.iloc[i, 0] = ref_duo[0]
                Group_table.iloc[i, 1] = ref_duo[1]
                Group_table.iloc[i, 2] = 'isolated'
                Group_table.iloc[i, 3] = 'isolated'
                Group_table.iloc[i, 4] = ref_duo[2]
                Group_table.iloc[i, 5] = ref_duo[3]
        if len(Duo_df) == 1:
            Group_table.iloc[i+1, 0] = Duo_df.iloc[0,0]
            Group_table.iloc[i+1, 1] = Duo_df.iloc[0,1]
            Group_table.iloc[i+1, 2] = 'isolated'
            Group_table.iloc[i+1, 3] = 'isolated'
            Group_table.iloc[i+1, 4] = Duo_df.iloc[0,2]
            Group_table.iloc[i+1, 5] = Duo_df.iloc[0,3]

        i = i + 1

    # print(i)
    a = Group_table['Site1'].isnull()
    Group_table = Group_table.drop(Group_table.index[a])

    return Group_table

def vrr_table(group_df):
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    n = len(group_df)
    # print(group_df)
    # print(n)
    vvrr_table = pd.DataFrame(columns=['Sarf', 'VCU', 'VDU', 'RIU'], index=range(0, n))
    vvrr_table['VCU'] = group_df['group'].values
    vdu_no = [1, 1, 2, 2]

    for i in range(0, n):
        vvrr_table.iloc[i, 2] = vdu_no[i]
        vvrr_table.iloc[i, 3] = i + 1


    if n == 4:
        dist_matrix = pd.DataFrame(columns=['Site1', 'Site2', 'Dist'], index=range(0, 6))
        dist_matrix.iloc[0, 0] = group_df.iloc[0, 0]
        dist_matrix.iloc[1, 0] = group_df.iloc[0, 0]
        dist_matrix.iloc[2, 0] = group_df.iloc[0, 0]
        dist_matrix.iloc[3, 0] = group_df.iloc[1, 0]
        dist_matrix.iloc[4, 0] = group_df.iloc[1, 0]
        dist_matrix.iloc[5, 0] = group_df.iloc[2, 0]

        dist_matrix.iloc[0, 1] = group_df.iloc[1, 0]
        dist_matrix.iloc[1, 1] = group_df.iloc[2, 0]
        dist_matrix.iloc[2, 1] = group_df.iloc[3, 0]
        dist_matrix.iloc[3, 1] = group_df.iloc[2, 0]
        dist_matrix.iloc[4, 1] = group_df.iloc[3, 0]
        dist_matrix.iloc[5, 1] = group_df.iloc[3, 0]

        dist_matrix.iloc[0, 2] = gc.distance_calculator(group_df.iloc[0, 1], group_df.iloc[0, 2], group_df.iloc[1, 1],
                                                        group_df.iloc[1, 2])
        dist_matrix.iloc[1, 2] = gc.distance_calculator(group_df.iloc[0, 1], group_df.iloc[0, 2], group_df.iloc[2, 1],
                                                        group_df.iloc[2, 2])
        dist_matrix.iloc[2, 2] = gc.distance_calculator(group_df.iloc[0, 1], group_df.iloc[0, 2], group_df.iloc[3, 1],
                                                        group_df.iloc[3, 2])
        dist_matrix.iloc[3, 2] = gc.distance_calculator(group_df.iloc[1, 1], group_df.iloc[1, 2], group_df.iloc[2, 1],
                                                        group_df.iloc[2, 2])
        dist_matrix.iloc[4, 2] = gc.distance_calculator(group_df.iloc[1, 1], group_df.iloc[1, 2], group_df.iloc[3, 1],
                                                        group_df.iloc[3, 2])
        dist_matrix.iloc[5, 2] = gc.distance_calculator(group_df.iloc[2, 1], group_df.iloc[2, 2], group_df.iloc[3, 1],
                                                        group_df.iloc[3, 2])

        dist_matrix = dist_matrix.sort_values(by=['Dist'])

        vvrr_table.iloc[0, 0] = dist_matrix.iloc[0, 0]
        vvrr_table.iloc[1, 0] = dist_matrix.iloc[0, 1]

        group_df = group_df[group_df.Sarf != vvrr_table.iloc[0, 0]]
        group_df = group_df[group_df.Sarf != vvrr_table.iloc[1, 0]]

        vvrr_table.iloc[2, 0] = group_df.iloc[0, 0]
        vvrr_table.iloc[3, 0] = group_df.iloc[1, 0]
    elif n == 3:
        dist_matrix = pd.DataFrame(columns=['Site1', 'Site2', 'Dist'], index=range(0, 3))
        dist_matrix.iloc[0, 0] = group_df.iloc[0, 0]
        dist_matrix.iloc[1, 0] = group_df.iloc[0, 0]
        dist_matrix.iloc[2, 0] = group_df.iloc[1, 0]

        dist_matrix.iloc[0, 1] = group_df.iloc[1, 0]
        dist_matrix.iloc[1, 1] = group_df.iloc[2, 0]
        dist_matrix.iloc[2, 1] = group_df.iloc[2, 0]

        dist_matrix.iloc[0, 2] = gc.distance_calculator(group_df.iloc[0, 1], group_df.iloc[0, 2], group_df.iloc[1, 1], group_df.iloc[1, 2])
        dist_matrix.iloc[1, 2] = gc.distance_calculator(group_df.iloc[0, 1], group_df.iloc[0, 2], group_df.iloc[2, 1], group_df.iloc[2, 2])
        dist_matrix.iloc[2, 2] = gc.distance_calculator(group_df.iloc[1, 1], group_df.iloc[1, 2], group_df.iloc[2, 1], group_df.iloc[2, 2])

        dist_matrix = dist_matrix.sort_values(by=['Dist'])

        vvrr_table.iloc[0, 0] = dist_matrix.iloc[0, 0]
        vvrr_table.iloc[1, 0] = dist_matrix.iloc[0, 1]

        group_df = group_df[group_df.Sarf != vvrr_table.iloc[0, 0]]
        group_df = group_df[group_df.Sarf != vvrr_table.iloc[1, 0]]

        vvrr_table.iloc[2, 0] = group_df.iloc[0, 0]

    elif n == 2:
        vvrr_table.iloc[0, 0] = group_df.iloc[0, 0]
        vvrr_table.iloc[1, 0] = group_df.iloc[1, 0]
    elif n == 1:
        vvrr_table.iloc[0, 0] = group_df.iloc[0, 0]
    # print(vvrr_table)
    return vvrr_table

def RRH_numbering(total_vvrr_df3):
    pre = 1
    k = 1
    m = len(total_vvrr_df3)

    for i in range(0, m):

        cur = total_vvrr_df3.iloc[i, 1]
        if cur != pre:
            k = 1
            total_vvrr_df3.iloc[i, 4] = k
            k = k + 1
        else:
            total_vvrr_df3.iloc[i, 4] = k
            k = k + 1

        pre = total_vvrr_df3.iloc[i , 1]

        # print(a)
    return total_vvrr_df3

def checks(vcu_plan_df):
    import pandas as pd
    number_of_sites = len(vcu_plan_df)
    n = number_of_sites // 4 + 1
    kalan = number_of_sites % 4
    if kalan == 0:
        n = n - 1
    m = len(vcu_plan_df['group'].unique())
    if n != m:
        print('error on number of groups')
    max = vcu_plan_df['group'].unique().max()
    if n != max:
        print('error on consecutive VCU number')
    site_vcu_count = pd.value_counts(vcu_plan_df['group'])
    if site_vcu_count.max() > 4:
        print('error on maximum site number in group')


