putting chess but plumbing online

### docs 
api docs [here](https://github.com/theSaneHatter/chess-but-plumbing-online/blob/main/msc/docs/api_docs.mkd)

### how run on windows 
```powershell
cd [cbp home dir]
python3 -m flask run
```
### todo
- better error handling : make errors look like this (with success included) :

``` javascript
        return {"error":"@send_actions:Error:incorrect dataType sent for gid. Likely Json instead of String.","success":"false"},400

```
