odoo.define('web_widget_color.widget', function(require) {
    'use strict';

    var core = require('web.core');
    var FieldChar = require('web.form_widgets').FieldChar;

    var _super_getDir = jscolor.getDir.prototype;
    jscolor.getDir = function() {
        var dir = _super_getDir.constructor();
        if (dir.indexOf('web_widget_color') === -1) {
            jscolor.dir = 'web_widget_color/static/lib/jscolor/';
        }
        return jscolor.dir;
    };

    var FieldColor = FieldChar.extend({
        template: 'FieldColor',
        className: 'oe_form_field_color',
        is_syntax_valid: function() {
            var $input = this.$('input');
            if (!this.get("effective_readonly") && $input.size() > 0) {
                var val = $input.val();
                var isOk = /^#[0-9A-F]{6}$/i.test(val);
                if (!isOk) {
                    return false;
                }
                try {
                    this.parse_value(this.$('input').val(), '');
                    return true;
                } catch (e) {
                    return false;
                }
            }
            return true;
        },
        render_value: function() {
            var show_value = this.format_value(this.get('value'), '');
            if (!this.get("effective_readonly")) {
                var $input = this.$el.find('input');
                $input.val(show_value);
                $input.css("background-color", show_value);
                jscolor.init();
            } else {
                this.$(".oe_form_char_content").text(show_value);
                this.$('div').css("background-color", show_value);
            }
        }

    });
    core.form_widget_registry.add('color', FieldColor);

    /*
     * Init jscolor for each editable mode on view form
     */
    // var FormView = core.view_registry.get('form');
    // FormView = FormView.extend({
    //     to_edit_mode: function () {
    //         console.log('here')
    //         this._super();
    //         jscolor.init();
    //     }
    // });
    // core.view_registry.add('form', FormView);

});