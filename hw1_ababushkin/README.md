# Opening Hours

## In short
Your task is to write an endpoint that accepts JSON-formatted opening hours of a
restaurant as an input and returns the rendered human readable format as a text output.

For run application you need:

```commandline
docker pull asbabush/hw1_ababushkin
sudo docker run -d -p 8000:8000 asbabush/hw1_ababushkin 
```


the application will run on http://localhost:8000 and will respond to post requests with a human-readable line.



example:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "params": {
    "monday": [],
    "tuesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 32400}
    ],
     "wednesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 32400}
    ],
     "thursday": [],
     "friday": [
            {"type": "open", "value": 64800}
     ],
     "saturday": [
            {"type": "close", "value": 82800},
            {"type": "close", "value": 3600},
            {"type": "open", "value": 32400},
            {"type": "close", "value": 39600},
            {"type": "open", "value": 57600}
     ],
      "sunday": []
  }
}'
```

response:
```commandline
"monday: close\ntuesday: 01:00 AM - 09:00 AM\nwednesday: 01:00 AM - 09:00 AM\nthursday: close\nfriday: 18:00 PM - 01:00 AM\nsaturday: 09:00 AM - 11:00 AM, 16:00 PM - 23:00 PM\nsunday: close\n"
```