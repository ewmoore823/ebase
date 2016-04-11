var gulp = require('gulp');
var gutil = require('gulp-util');
var gulpif = require('gulp-if');
var coffee = require('gulp-coffee');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('default', ['coffee', 'sass']);

var production = false;
gulp.task('coffee', function() {
    gulp.src('./ebase/main/static/main/coffee/*.coffee')
        .pipe(gulpif(!production, sourcemaps.init()))
        .pipe(coffee({bare:true}).on('error', gutil.log))
        .pipe(gulpif(!production, sourcemaps.write('./maps')))
        .pipe(gulp.dest('./ebase/main/static/main/lib/js/'));
});

var sass_task = function(sass_src, sass_dest) {
    return function () {
        return gulp.src(sass_src)
            .pipe(gulpif(!production, sourcemaps.init()))
            .pipe(sass({ outputStyle: production ? 'compressed' : 'nested' }))
            .pipe(sass().on('error', sass.logError))
            .pipe(gulpif(!production, sourcemaps.write('./maps')))
            .pipe(gulp.dest(sass_dest))
    }
};

gulp.task('sass', sass_task('./ebase/main/static/main/scss/*.scss', './ebase/main/static/main/lib/scss'));
gulp.task('sass', sass_task('./ebase/main/static/main/css/foundation/*.css', './ebase/main/static/main/lib/css/foundation/'));

