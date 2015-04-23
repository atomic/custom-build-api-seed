#! /bin/bash
#
# TestEndpoin.sh
# Copyright (C) 2015 Tony Lim <atomictheorist@gmail.com>
#
# Distributed under terms of the MIT license.
#

# if command does not exist
url=http://127.0.0.1:5000/students/
#args="-X POST -d@myfile.txt server-URL"
args="-G"

if [[ -z "$1" ]]; then
    echo "using $1 as default url"
else
    $url=$1
fi

# I for head, s for silent

# first test GET
curl -Is -f $args $url && echo "GET on $url success" || echo "GET on $url FAILS"
echo -e '\n'

# test POST json
curl -f -H "Content-Type: application/json" -X POST -d '{"name":"testPost"}' $url && echo -e "\nPOST on $url success" || echo "\nPOST on $url FAILS"
echo -e '\n'

# test GET
curl -Is -f -G ${url}1 && echo "GET on ${url}1 success" || echo "GET on ${url}1 FAILS"
echo -e '\n'

$args="-H \"Content-Type: application/json\" -X PUT -d '{\"name\":\"testPUTchangeName\"}'"
# test PUT
curl -f $args ${url}1 && echo "POST on ${url}1 success" || echo "POST on ${url}1 FAILS"
