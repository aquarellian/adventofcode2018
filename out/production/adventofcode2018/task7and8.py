

def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


start_mrk='begins shift'
asleep_mrk = 'falls asleep'
awakes_mrk = 'wakes up'
with open("task7.txt") as f:
    content = f.readlines()
    import pandas
    df  = pandas.DataFrame(columns=['timestamp', 'id', 'event'])
    i = 0
    id = None
    isasleep = False
    for line in content:
        if start_mrk in line:
            id = substr_between(line, '#', ' ')
            df.loc[i, 'id'] = int(id)
            df.loc[i, 'timestamp'] = substr_between(line, '[', ']')
            df.loc[i, 'event'] = 'L'
            i+=1
        elif asleep_mrk in line or awakes_mrk in line:
            timestamp = substr_between(line, '[', ']')

            df.loc[i, 'timestamp'] = substr_between(line, '[', ']')
            df.loc[i, 'event'] = ('S' if asleep_mrk in line else 'A')
            i+=1

    event_df = df.sort_values(['timestamp']).reset_index()

    df  = pandas.DataFrame(columns=['date', 'id', 'from', 'to', 'sleeptime'])
    i = 0
    id = None
    for index, row in event_df.iterrows():
        if row['event'] == 'L':
            id = row['id']
        elif row['event'] == 'S':
            df.loc[i, 'id'] = id
            timestamp = row['timestamp']
            date = substr_between(timestamp, None, ' ')
            minutes = int(substr_between(timestamp, ':', None))
            hrs = int(substr_between(timestamp, ' ', ':'))
            df.loc[i, 'date'] = date
            df.loc[i, 'from'] = minutes
        elif row['event'] == 'A':
            timestamp = row['timestamp']
            # date = substr_between(timestamp, None, ' ')
            minutes = int(substr_between(timestamp, ':', None))
            df.loc[i, 'to'] = minutes
            df.loc[i, 'sleeptime'] = df.loc[i, 'to'] - df.loc[i, 'from']
            i+=1

    total_sleep = df.groupby(['id']).sum()
    id = total_sleep[total_sleep['sleeptime'] == total_sleep['sleeptime'].max()].index[0]

    df_by_id = df[df['id'] == id]
    themax = 0
    minute = -1

    for i in range(0, 60):
        count = df_by_id[(df_by_id['from'] <= i) & (df_by_id['to'] > i)].count()[0]
        if count > themax:
            themax = count
            minute = i
    print("task 7")
    print ('id=' + str(id))
    print ('minute=' + str(minute))
    print (minute*id)

    ### task8


    themax = 0
    theid = -1
    minute = -1
    themap = {}
    import numpy
    sumschedule = list(map(int, numpy.zeros(60).tolist()))
    from operator import add
    for id in df['id'].unique():
        schedule = list(map(int, numpy.zeros(60).tolist()))
        df_by_id = df[df['id'] == id]
        for index, row in df_by_id.iterrows():
            for i in range(row['from'], row['to']):
                schedule[i] += 1
        sumschedule = list(map(add, sumschedule, schedule))
        themap[id] = schedule

        newmax = max(schedule)
        if newmax > themax:
            themax = newmax
            minute = schedule.index(newmax)
            theid = id
    print("task 8")
    print('id=' + str(theid))
    print('minute=' + str(minute))
    print(minute * theid)

    # themax = max(sumschedule)
    # theminute = sumschedule.index(themax)
    # print(sumschedule)
    # print(themax)
    # print(theminute)
    #
    # themax = 0
    # theid = -1
    # for id, schedule in themap.items():
    #     if schedule[theminute] > themax:
    #         themax = schedule[theminute]
    #         theid = id
    # print(theid)
    # print(theminute)
    # print(theid*theminute)
















