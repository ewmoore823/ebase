var gulp = require('gulp');
var gutil = require('gulp-util');
var coffee = require('gulp-coffee');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('default', ['coffee']);

gulp.task('coffee', function() {
    gulp.src('./ebase/main/static/main/coffee/*.coffee')
        .pipe(sourcemaps.init())
        .pipe(coffee({bare:true}).on('error', gutil.log))
        .pipe(sourcemaps.write('./maps'))
        .pipe(gulp.dest('./ebase/main/static/main/lib/'));
});

