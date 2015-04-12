#! /bin/bash
# Desck : Script will populate 30 records into the database using curl


url=http://127.0.0.1:5000/students/
if [[ -z "$1" ]]; then
    echo "using $1 as default url"
else
    $url=$1
fi

contentType="Content-Type: application/json"

# test POST json
for i in `seq 1 10` ; do
    echo -e "populate$i\n"
    curl -H "$contentType" -X POST -d '{"name":"Populate"}' $url
done
echo "Populate done!"

# Bug
# curl requires json parameter to be surrounded by '', bash can't recognize variable inside ''
