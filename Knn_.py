from knn_func import knn,euclidean_distance,mean

def predict(query,knum):
    raw_data = []
    with open('Prostate_Cancer.csv','r') as md:
        next(md)
        for line in md.readlines():
            data_row = line.strip().split(',')
            raw_data.append(data_row)
    #print(raw_data)

    process_data = []
    for row in raw_data:
        if(row[1]=='M'):
            row[1]=1
        else:
            row[1]=0
        data_row = list(map(float,row[1:]))
        process_data.append(data_row)
    #print(process_data)
    
    res, _ = knn(
        process_data, query , knum,
        distance_fn=euclidean_distance, choice_fn=mean
    )
    #print(round(_))
    res1 = round(_)
    if(res1==1):
        print("M")
    else:
        print("B")
    print(res)
   

query1 = [22,14,78,451,0.105,0.071,0.19,0.066]
predict(query1,15)

#96,M,23,16,132,1264,0.091,0.131,0.21,0.056
#97,B,22,14,78,451,0.105,0.071,0.19,0.066
#98,B,19,27,62,295,0.102,0.053,0.135,0.069
#99,M,16,27,94,643,0.098,0.114,0.188,0.064
#100,B,21,24,74,413,0.09,0.075,0.162,0.066