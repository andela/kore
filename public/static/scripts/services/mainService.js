app.factory('sessionInjector', function ($cookies) {
    return {
        request: function(config) {
            var token = $cookies.get("token");
            config.headers = config.headers || {};
            if (token) {
                config.headers['Authorization'] = "JWT " + token;
            }

            return config;
        }
    };
});

app.factory('mainService', function ($resource) {
    return {
        auth: $resource('/api/api-token-auth/', {}, {
            login: {
                method: 'POST'
            }
        }, {
            stripTrailingSlashes: false
        }),
        verify: $resource('/api/api-token-verify/', {}, {
            token: {
                method: 'POST'
            }
        }, {
            stripTrailingSlashes: false
        }),
        users: $resource('/api/user/', {}, {
            create: {
                method: 'POST'
            }
        }, {
            stripTrailingSlashes: false
        }),

        OrgConfirmation: $resource('/api/orginvite/:pk/', {pk:'@pk'}, {
            comfirmMember : {

                method: 'GET',
                isArray: false

            }
        }, {
            stripTrailingSlashes: false
        }),

        personal: $resource('/api/personal/', {}, {
            // method to consume the api route to personal projects
            getProjects: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        }),
        org: $resource('/api/orgprojects/', {}, {
            // method to consume the api route to organization projects
            getProjects: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        }),
        other: $resource('/api/otherprojects/', {}, {
            // method to consume the api route to other projects
            getProjects: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        })
    };
});
