"use strict";

const _ = require('lodash');
const gulp = require('gulp');
const rename = require('gulp-rename');
const clean = require('gulp-clean');
const mustache = require('gulp-mustache');
const apis = require('clayful-lib-spec/data/api.json');
const aliases = require('clayful-lib-spec/data/aliases.json');

const ext = '.py';

// Change arguments to string and add aliases
apis.forEach(a => {

	_.forEach(aliases, (v, k) => {

		if (!a.method.includes(k)) return;

		a.aliases = (a.aliases || []).concat(v.map(alias => a.method.replace(k, alias)));

	});

});

const byModel = _.groupBy(apis, a => a.className);

gulp.task('clean', () => {

	return gulp.src(['./clayful-python/clayful/models/*'], { read: false })
		.pipe(clean());

});

gulp.task('models', ['clean'], () => {

	_.forEach(byModel, (apis, className) => {

		apis.forEach(a => {

			// python method naming convention
			a.method = _.snakeCase(a.method);
			a.aliases = a.aliases ? a.aliases.map(_.snakeCase) : [];

		});

		gulp.src('./build/model.mustache')
			.pipe(mustache({
				modelName: _.camelCase(className),
				className: className,
				methods:   apis
			}))
			.pipe(rename(path => {
				path.basename = _.snakeCase(className); // python filename convention
				path.extname = ext;
			}))
			.pipe(gulp.dest(`./clayful-python/clayful/models`));

	});

});

gulp.task('binder', ['models'], () => {

	gulp.src('./build/binder.mustache')
		.pipe(mustache({
			models: Object.keys(byModel).map(className => ({
				modelName:  _.camelCase(className),
				className:  className,
				moduleName: _.snakeCase(className)
			}))
		}))
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