# SeleniumBase Docker Image
FROM ubuntu:22.04
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

#==========================================
# Create entrypoint and grab example tests
#==========================================
CMD ["pytest"]
