import pandas as pd 
import numpy as np 
from sklearn.base import TransformerMixin, BaseEstimator

def transform_name(sr_name):
    df = sr_name.apply(lambda x: x.split(',')).to_frame('list_name')
    df['surname'] = df['list_name'].apply(lambda x: x[0])
    df['forename'] = df['list_name'].apply(lambda x: x[1])
    return df[['surname', 'forename']]

def get_tck_str(tck):
    try:
        x = tck.split()
        try: 
            a = int(x[0])
            return a
        except:
            return x[0]
    except:
        return None
    
def get_tck_num(tck):
    try:
        x = tck.split()
        try:
            a = int(x[0])
            return a
        except:
            return None
    except:
        return None

def transform_ticket(sr_ticket):
    df_ticket = sr_ticket.to_frame('ticket')
    df_ticket['ticket_str'] = sr_ticket.apply(get_tck_str)
    df_ticket['ticket_num'] = sr_ticket.apply(get_tck_num)
    return df_ticket[['ticket_str', 'ticket_num']]

def transform_cabin(sr_cabin):
    df_cabin = sr_cabin.to_frame('cabin')
    df_cabin_clean = df_cabin[~df_cabin['cabin'].isna()].copy()
    df_cabin_clean['cabin_str'] = df_cabin_clean['cabin'].apply(lambda x: x[0])
    df_cabin_clean['cabin_num'] = df_cabin_clean['cabin'].apply(lambda x: x[1:]).astype(int)
    return df_cabin.join(df_cabin_clean[['cabin_str', 'cabin_num']])[['cabin_str', 'cabin_num']]

class PassNameTransformer(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        self.X = transform_name(X)
        return self.X

    def get_feature_names(self):
        return self.X.columns.tolist()

class TicketTransformer(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        self.X = transform_ticket(X)
        return self.X

    def get_feature_names(self):
        return self.X.columns.tolist()
    
class CabinTransfomer(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        self.X = transform_cabin(X)
        return self.X

    def get_feature_names(self):
        return self.X.columns.tolist()