var gulp = require('gulp');
var gutil = require('gulp-util');
var coffee = require('gulp-coffee');


gulp.task('default', ['coffee']);

gulp.task('coffee', function() {
    gulp.src('./ebase/main/static/main/coffee/*.coffee')
        .pipe(coffee({bare:true}).on('error', gutil.log))
        .pipe(gulp.dest('./ebase/main/static/main/lib/'));
});
