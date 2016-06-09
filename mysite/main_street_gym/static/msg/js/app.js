'use strict';

angular.module('msgApp', ['ngRoute'])
.config(function($routeProvider) {
        $routeProvider
            // route for the contactus page
           
         .when('/contact', {
                templateUrl : 'views/contact.html'
            })
            .when('/home', {
                templateUrl : 'views/home.html'
            })
            // route for the menu page
            .when('/classes', {
                templateUrl : 'views/classes.html'
            })
            // route for the dish details page
            .when('/about', {
                templateUrl : 'views/about.html'
            })
            .when('/',{
            templateUrl : 'views/home.html'
        })
    })