import pandas as pd
from data import owners, influencers 
def compare_categories(owner, user):
    owner_categories=set(c["category_name"] for c in owner["preference"].get("categories",[]))
    user_categories=set(c["category_name"] for c in user["preference"].get("categories",[]))
    return {
        "intersec":len(owner_categories & user_categories),
        "total":len(owner_categories)+len(user_categories)
    }
    
def compare_products(owner, user):
    owner_products=set(c["product_name"] for c in owner["preference"].get("products",[]))
    user_products=set(c["product_name"] for c in user["preference"].get("products",[]))
    return {
        "intersec":len(owner_products & user_products),
        "total":len(owner_products)+len(user_products)
    }
def compare_marketing(owner, user):
    owner_marketing=set(c["marketing_type"] for c in owner["preference"].get("marketing",[]))
    user_marketing=set(c["marketing_type"] for c in user["preference"].get("marketing",[]))
    return {
        "intersec":len(owner_marketing & user_marketing),
        "total":len(owner_marketing)+len(user_marketing)
    }


def content_based_filtering():
    owner=pd.DataFrame(owners[0])
    influencers_df=pd.DataFrame(influencers)
    arr=[]
    
        
    for index, user in influencers_df.iterrows():
        scores=[]
        category_score=compare_categories(owner,user)
        product_score=compare_products(owner,user)
        marketing_score=compare_marketing(owner,user)
        
        
        if product_score["total"]!=0:
            scores.append(round(2*product_score["intersec"]/product_score["total"],2))
        if category_score["total"]!=0:
            scores.append(round(2*category_score["intersec"]/category_score["total"],2))
        if marketing_score["total"]!=0:
            scores.append(round(2*marketing_score["intersec"]/marketing_score["total"],2))
        
        result=round(sum(scores)/len(scores), 2) if scores else 0
        
        arr.append({
            "id":user["id"],
            "result":result})
        
    array_df=pd.DataFrame(arr)
    sorted_array=array_df.sort_values(by="result",ascending=False)
   
    preference_array=sorted_array[sorted_array["result"]>0.1]
    
    for influencer_id in preference_array["id"]:
        print(influencers_df[influencers_df["id"]==influencer_id])
        

content_based_filtering()