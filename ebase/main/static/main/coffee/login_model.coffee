class @LoginModel extends EbaseModel
    constructor: ->
        super
        @username  = ko.observable()
        @password = ko.observable()

    submit: =>
        $.ajax
           url: /login/
           type: 'POST'
           datatype: 'json'
           data:
               'username': @username
               'password': @password
           success: (data, status, jqXHR) =>
               console.log('POST successful')
               console.log('data')
               console.log(data)

           error: =>
               console.log('POST failed')

        # Post ajax to authenticate user

