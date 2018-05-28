{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red118\green0\blue120;\red243\green246\blue249;\red14\green63\blue99;
\red16\green123\blue53;\red31\green124\blue26;\red192\green63\blue68;\red163\green53\blue194;\red93\green103\blue105;
}
{\*\expandedcolortbl;;\cssrgb\c54510\c0\c54510;\cssrgb\c96078\c97255\c98039;\cssrgb\c4706\c31765\c46275;
\cssrgb\c0\c54510\c27059;\cssrgb\c13333\c54510\c13333;\cssrgb\c80392\c33333\c33333;\cssrgb\c70588\c32157\c80392;\cssrgb\c43922\c47843\c48627;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
from\cf4  \cf5 flask\cf4  \cf2 import\cf4  Flask\
\cf2 from\cf4  \cf5 redis\cf4  \cf2 import\cf4  Redis, RedisError\
\cf2 import\cf4  \cf5 os\cf4 \
\cf2 import\cf4  \cf5 socket\cf4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 # Connect to Redis\cf4 \
redis = Redis(host=\cf7 "redis"\cf4 , db=\cf8 0\cf4 , socket_connect_timeout=\cf8 2\cf4 , socket_timeout=\cf8 2\cf4 )\
\
app = Flask(__name__)\
\
\pard\pardeftab720\partightenfactor0
\cf9 @app.route\cf4 (\cf7 "/"\cf4 )\
\pard\pardeftab720\partightenfactor0
\cf2 def\cf4  hello():\
    \cf2 try\cf4 :\
        visits = redis.incr(\cf7 "counter"\cf4 )\
    \cf2 except\cf4  RedisError:\
        visits = \cf7 "<i>cannot connect to Redis, counter disabled</i>"\cf4 \
\
    html = \cf7 "<h3>Hello \{name\}!</h3>"\cf4  \\\
           \cf7 "<b>Hostname:</b> \{hostname\}<br/>"\cf4  \\\
           \cf7 "<b>Visits:</b> \{visits\}"\cf4 \
    \cf2 return\cf4  html.format(name=os.getenv(\cf7 "NAME"\cf4 , \cf7 "world"\cf4 ), hostname=socket.gethostname(), visits=visits)\
\
\cf2 if\cf4  __name__ == \cf7 "__main__"\cf4 :\
    app.run(host=\cf7 '0.0.0.0'\cf4 , port=\cf8 80\cf4 )}