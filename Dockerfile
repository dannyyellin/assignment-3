FROM python:alpine3.17
WORKDIR ./app
RUN pip install flask
RUN pip install flask_restful
RUN pip install requests
RUN pip install simplejson
ENV FLASK_APP=meals.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_DEBUG: "true"
ADD meals.py .
ADD meal_exceptions.py .
ADD My_Ninja_key.py .
Add Ninja_key.py .
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]