 #summary
    rt = df2
    rt = rt.astype(str)  
    
    
    totalblocks = len(rt.Block.unique())
    rt['DCCapacityKWp'] = pd.to_numeric(rt['DCCapacityKWp'], errors='coerce')
    rt1 =rt[rt.DCCapacityKWp.notnull()]
    #rt1['DCCapacityKWp'] = rt1['DCCapacityKWp'].astype(float)
    totaldcMWp = round(sum(rt1['DCCapacityKWp'])/1000,2)
