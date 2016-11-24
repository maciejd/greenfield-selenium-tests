# greenfield-selenium-tests
Selenium test suite for Greenfield app using Python bindings

Requires docker, python, pip

1. Deploy Greenfield app as described in https://github.com/maciejd/greenfield-django

2. Run Selenium Standalone Chrome node `docker run -d -p 4444:4444 selenium/standalone-chrome:3.0.1-aluminum`

4. Clone repo with tests `git clone https://github.com/maciejd/greenfield-selenium-tests.git`

5. Chande directory `cd greenfield-selenium tests`

6. Install selenium `pip install selenium`

7. Modify `DOCKER_HOST_IP` in `greenfield_selenium.py` to match your docker host's IP

8. Run tests `python greenfield_selenium.py`
