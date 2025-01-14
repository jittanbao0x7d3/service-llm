1. Set Up a Virtual Environment
```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
2. Install dependencies
```
   pip install -r requirements.txt
```

3. Create env variable `OPENAI_API_KEY="actual_key"` or simplify replace the key in `llm_service.py:56`
4. Run the main file
```
   python main.py
```

The server should be run in http://127.0.0.1:8000 

Try 
```
curl -X 'POST' \
  'http://127.0.0.1:8000/prompt' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "cast of The God Father"
}'
```
The result should be 
```
{
  "collection": "people"
}
```
