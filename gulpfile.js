"use strict";

const _ = require('lodash');
const gulp = require('gulp');
const rename = require('gulp-rename');
const clean = require('gulp-clean');
const mustache = require('gulp-mustache');
const models = require('clayful-lib-spec');

const ext = '.py';

gulp.task('clean', () => {

	return gulp.src(['./clayful-python/clayful/models/*'], { read: false })
		.pipe(clean());

});

gulp.task('models', ['clean'], () => {

	_.forEach(models, model => {

		// python method naming convention
		models.forEach(model => {
			model.apis.forEach(a => a.method = _.snakeCase(a.method));
		});

		gulp.src('./build/model.mustache')
			.pipe(mustache(model))
			.pipe(rename(path => {
				path.basename = _.snakeCase(model.className); // python filename convention
				path.extname = ext;
			}))
			.pipe(gulp.dest(`./clayful-python/clayful/models`));

	});

});

gulp.task('binder', ['models'], () => {

	gulp.src('./build/binder.mustache')
		.pipe(mustache(models.map(model => _.set(model, 'moduleName', _.snakeCase(model.className)))))
		.pipe(rename(path => {
			path.basename = '__init__';
			path.extname = ext;
		}))
		.pipe(gulp.dest(`./clayful-python/clayful/models`));

});

gulp.task('readme', () => {

	gulp.src('./clayful-python/README.md')
		.pipe(gulp.dest('./'));

});

gulp.task('default', ['models', 'binder', 'readme']);