import pandas as pd


dict_bool={'Yes':1, 'No':0}
dict_genre={'Latin':0, 'Rock':1, 'Video game music':2, 'Jazz':3, 'R&B':4, 'K pop':5, 'Country':6, 'EDM':7, 'Hip hop':8, 'Pop':9, 'Rap':10, 'Classical':11, 'Metal':12, 'Folk':13, 'Lofi':14, 'Gospel':15}
dict_frequency={'Never':0, 'Rarely':1, 'Sometimes':2, 'Very frequently':3}
dict_effect={'Worsen':-1,'No effect':0, 'Improve':1}
dict_streaming={'I do not use a streaming service.':0, 'Apple Music':1,'Spotify':2, 'Pandora':3, 'YouTube Music':4,  'Other streaming service':5 }

dict_replace_col={'Primary streaming service':dict_streaming,'While working':dict_bool,'Instrumentalist':dict_bool,'Composer':dict_bool,'Fav genre':dict_genre,
                  'Exploratory':dict_bool,'Foreign languages':dict_bool,'Music effects':dict_effect}


def clean_data(df:pd.DataFrame)->pd.DataFrame:
    """
    Function to drop column BPM in dataframe, to drop row with N/A and to replace str by float in some column
    """
    print("__________________")
    print("Drop col : BPM")
    df = df.drop(columns=['BPM'])
    print("__________________")
    print("Drop Na")
    print(f"Total rows : {df.shape[0]}")
    df = df.dropna()
    print(f"Total rows after drop na : {df.shape[0]}")
    print("__________________")
    print("Replace str by float in each columns")
    for col in df.columns :
        if col in dict_replace_col.keys():
            df[col]=df[col].map(dict_replace_col[col])
        elif col.startswith('Frequency'):
            df[col]=df[col].map(dict_frequency)
    return df

