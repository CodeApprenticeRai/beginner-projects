
# coding: utf-8

# In[3]:

def read_csv(file):
    #Opens file, splits on new line, and takes out the header
    ed1_file = open(file, "r").read()
    ed2_file = ed1_file.split("\n")
    string_list = ed2_file[1:-1]
    final_list = []
    
    #Turns data in a list of list of integers
    for obj in string_list:
        int_fields = []
        string_fields = obj.split(",")
        for j in string_fields:
            x = int(j)
            int_fields.append(x)
            #int_fields.append(int(string_fields[0:-1]))
        final_list.append(int_fields)
    return(final_list)
  


# In[4]:

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


# In[3]:

f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
raw_data = f.read()
raw_data1 = raw_data.split("\n")
print(raw_data1[0:10])


# In[5]:

def month_births(arg):
    births_per_month = {}
    for obj in arg:
        month = obj[1]
        births = obj[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return(births_per_month)
    


# In[6]:

cdc_months_births = month_births(cdc_list)
cdc_months_births


# In[7]:

def dow_births(arg):
    day_of_week = {}
    for obj in arg:
        day = obj[3]
        births = obj[4]
        if day in day_of_week:
            day_of_week[day] += births
        else:
            day_of_week[day] = births
    return(day_of_week)


# In[8]:

cdc_day_births = dow_births(cdc_list)
cdc_day_births


# In[13]:

#Sums births for a requested periods
def calc_counts(data, column_index):
    out_set = {}
    for obj in data:
        tally = obj[column_index]
        births = obj[4]
        if tally in out_set:
            out_set[tally] += births
        else:
            out_set[tally] = births
    return(out_set)

#This function can be improved by making it more user friendly.
#Prompts for input that actually ask for the requested period would be a good improvement.


# In[15]:

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)


# In[16]:

cdc_year_births


# In[17]:

cdc_month_births


# In[18]:

cdc_dom_births


# In[19]:

cdc_dow_births


# In[ ]:



