from pydantic import BaseModel
#clien sends the target url 
class URLBase(BaseModel):
    target_url:str
#check if url is working
class URL(URLBase):
    is_active:bool
    clicks:int
    class Config:
        orm_mode=True#object relation mapping
#return the information of shortened url  
class URLInfo(URL):
    url:str
    admin_url:str

