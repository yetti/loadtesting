# loadtesting

Load testing Trove's Solr connection manager. 

## Dependencies
* [locust.io](https://locust.io/)
* [Beautiful Soup 4.6.0](https://www.crummy.com/software/BeautifulSoup/)

## Swarm setup

20 slaves generating 1000 users with 10 users/sec over 1 hr.
Above settings will hatch and swarm 50 clients at the rate 0.5 clients/s for each slave.
