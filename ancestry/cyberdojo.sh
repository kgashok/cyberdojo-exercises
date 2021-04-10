# Change the version of Node.js to use, see https://nodejs.org
# to see the supported ES6 features see: https://kangax.github.io/compat-table/es6/
# 4.1.1 supports some ES6 (about 50%) features: https://nodejs.org/en/docs/es6/
# 0.12.7 is the latest version without most ES6 (about 20%) features: https://nodejs.org/docs/latest-v0.12.x/api/
#
# set the version to use:

#NODE_VERSION=0.12.7
NODE_VERSION=4.2.1
#
# Use npm package 'n' to call jasmine and jshint with selected node version:
if [ -f .jshintrc ]
  then
    n use $NODE_VERSION /usr/lib/node_modules/jshint/bin/jshint --config .jshintrc *.js | grep -v "underscore-min"
fi
n use $NODE_VERSION /usr/local/lib/node_modules/jasmine/bin/jasmine JASMINE_CONFIG_PATH=./jasmine.json
