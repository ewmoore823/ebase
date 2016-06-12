class @SiteModel extends EbaseModel
    constructor: ->
        super
        @top_nav = new NavModel()
        console.log('sitemodel works')

