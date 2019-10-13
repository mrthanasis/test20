# Instructions

Download the files from my GitHub profile, or clone using Git.

https://github.com/mrthanasis/test20


To build the container:

docker build -t my_docker_flask:latest .

To run the container:

docker run -p 9091:9091 my_docker_flask:latest

So to run the API I use Postman,

We place in the body:

{
    "days": "10"
}


if we need data of let's say 10 days

For the order conversion rate of the last 10 days:

http://0.0.0.0:9091/lastxdays

In order to compare the last 10 days order conversion rate with the previous period one:

http://0.0.0.0:9091/periods

Breakdown the above into two dimensions:
- UserType (New or Returning User)
- Platform (Web or Mobile):

http://0.0.0.0:9091/breakdown

CSV export functionality of the Order Conversion rate of the last 10 days:

http://0.0.0.0:9091/download
