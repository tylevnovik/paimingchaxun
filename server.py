# -*- coding: utf-8 -*-
from bottle import route, run, request, get, static_file, error
import csv
import os

# 此处可扩充为完整HTML
queryPage = '''
<!DOCTYPE html>
<html>

<head>
    <meta name="GCD" content="YTk3ODQ3ZWZhN2I4NzZmMzBkNTEwYjJl63551fcd89c6cd1cb07a803d3e388d2f" />
    <meta charset="utf-8">
    <title>排名查询</title>
    <meta name="generator" content="Google Web Designer 10.0.2.0105">
    <style type="text/css" id="gwd-text-style">
        p {
            margin: 0px;
        }

        h1 {
            margin: 0px;
        }

        h2 {
            margin: 0px;
        }

        h3 {
            margin: 0px;
        }
    </style>
    <style type="text/css">
        html,
        body {
            width: 100%;
            height: 100%;
            margin: 0px;
        }

        body {
            background-color: transparent;
            transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
            -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
            -moz-transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
            perspective: 1400px;
            -webkit-perspective: 1400px;
            -moz-perspective: 1400px;
            transform-style: preserve-3d;
            -webkit-transform-style: preserve-3d;
            -moz-transform-style: preserve-3d;
        }

        .gwd-label-18j8 {
            position: absolute;
            top: 111px;
            width: 100px;
            height: 20px;
            left: 49px;
        }

        .gwd-button-1gnh {
            position: absolute;
            border-width: 2px;
            width: 123px;
            height: 42px;
            left: 102px;
            top: 249px;
            font-size: 24px;
            transform-style: preserve-3d;
            -webkit-transform-style: preserve-3d;
            -moz-transform-style: preserve-3d;
            transform: translate3d(12px, 50px, 0px) rotateZ(10deg);
            -webkit-transform: translate3d(12px, 50px, 0px) rotateZ(10deg);
            -moz-transform: translate3d(12px, 50px, 0px) rotateZ(10deg);
        }

        .gwd-label-27js {
            font-size: 21px;
            top: 153px;
        }

        .gwd-label-1u2o {
            top: 121px;
            width: 113px;
        }

        .gwd-particleeffects-occn {
            position: absolute;
            width: 200px;
            height: 140px;
            top: 361px;
            left: 76px;
        }

        .gwd-label-myd5 {
            font-size: 35px;
            width: 281px;
            left: 35px;
            top: 41px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-input-146t {
            position: absolute;
            width: 100px;
            height: 20px;
            top: 108px;
            left: 163px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-18j8 {
            position: absolute;
            top: 111px;
            width: 100px;
            height: 20px;
            left: 49px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-input-fk3t {
            width: 134px;
            left: 114px;
            top: 77px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-bo8s {
            font-size: 20px;
            left: 0px;
            top: 80px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-input-shhh {
            width: 134px;
            left: 114px;
            top: 117px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-19j3 {
            font-size: 21px;
            width: 116px;
            left: 0px;
            top: 120px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-27js {
            font-size: 21px;
            top: 153px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-input-dnuw {
            width: 134px;
            left: 114px;
            top: 37px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-1u2o {
            width: 113px;
            top: 0px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-select-xko4 {
            position: absolute;
            height: 24px;
            width: 134px;
            left: 117px;
            top: 0px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-1otp {
            left: 0px;
            top: 40px;
        }

        [data-gwd-group="Group1"] .gwd-grp-cyef.gwd-label-o9fx {
            left: 0px;
        }

        [data-gwd-group="Group1"] {
            width: 256px;
            height: 143px;
        }

        .gwd-div-1j1w {
            position: absolute;
            top: 121px;
            left: 48px;
        }

        @media (max-height: 523px) and (max-width: 353px) and (min-height: 517px) and (min-width: 347px) {}
    </style>
    <script data-source="googbase_min.js" data-version="4" data-exports-type="googbase">(function () {/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
            (window.goog = window.goog || {}).inherits = function (a, c) { function d() { } d.prototype = c.prototype; a.b = c.prototype; a.prototype = new d; a.prototype.constructor = a; a.a = function (f, g, h) { for (var e = Array(arguments.length - 2), b = 2; b < arguments.length; b++)e[b - 2] = arguments[b]; return c.prototype[g].apply(f, e) } };
        }).call(this);
    </script>
    <script data-source="gwd_webcomponents_v1_min.js" data-version="2" data-exports-type="gwd_webcomponents_v1">/*

Copyright The Closure Library Authors.
SPDX-License-Identifier: Apache-2.0
*/
        /*
        
         Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
         This code may only be used under the BSD style license found at
         http://polymer.github.io/LICENSE.txt The complete set of authors may be found
         at http://polymer.github.io/AUTHORS.txt The complete set of contributors may
         be found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by
         Google as part of the polymer project is also subject to an additional IP
         rights grant found at http://polymer.github.io/PATENTS.txt
        */
        (function () { if (void 0 !== window.Reflect && void 0 !== window.customElements && !window.customElements.polyfillWrapFlushCallback) { var BuiltInHTMLElement = HTMLElement; window.HTMLElement = function () { return Reflect.construct(BuiltInHTMLElement, [], this.constructor) }; HTMLElement.prototype = BuiltInHTMLElement.prototype; HTMLElement.prototype.constructor = HTMLElement; Object.setPrototypeOf(HTMLElement, BuiltInHTMLElement) } })();
        (function () {/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
            var n;/*

 Copyright (c) 2020 The Polymer Project Authors. All rights reserved.
 This code may only be used under the BSD style license found at
 http://polymer.github.io/LICENSE.txt The complete set of authors may be found
 at http://polymer.github.io/AUTHORS.txt The complete set of contributors may
 be found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by
 Google as part of the polymer project is also subject to an additional IP
 rights grant found at http://polymer.github.io/PATENTS.txt
*/
            /*
            
             Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
             This code may only be used under the BSD style license found at
             http://polymer.github.io/LICENSE.txt The complete set of authors may be found
             at http://polymer.github.io/AUTHORS.txt The complete set of contributors may
             be found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by
             Google as part of the polymer project is also subject to an additional IP
             rights grant found at http://polymer.github.io/PATENTS.txt
            */
            var p = window.Document.prototype.createElement, q = window.Document.prototype.createElementNS, aa = window.Document.prototype.importNode, ba = window.Document.prototype.prepend, ca = window.Document.prototype.append, da = window.DocumentFragment.prototype.prepend, ea = window.DocumentFragment.prototype.append, r = window.Node.prototype.cloneNode, t = window.Node.prototype.appendChild, u = window.Node.prototype.insertBefore, v = window.Node.prototype.removeChild, w = window.Node.prototype.replaceChild, x = Object.getOwnPropertyDescriptor(window.Node.prototype,
                "textContent"), z = window.Element.prototype.attachShadow, A = Object.getOwnPropertyDescriptor(window.Element.prototype, "innerHTML"), B = window.Element.prototype.getAttribute, C = window.Element.prototype.setAttribute, D = window.Element.prototype.removeAttribute, E = window.Element.prototype.getAttributeNS, F = window.Element.prototype.setAttributeNS, G = window.Element.prototype.removeAttributeNS, H = window.Element.prototype.insertAdjacentElement, fa = window.Element.prototype.insertAdjacentHTML, ha = window.Element.prototype.prepend,
                ia = window.Element.prototype.append, ja = window.Element.prototype.before, ka = window.Element.prototype.after, la = window.Element.prototype.replaceWith, ma = window.Element.prototype.remove, na = window.HTMLElement, I = Object.getOwnPropertyDescriptor(window.HTMLElement.prototype, "innerHTML"), oa = window.HTMLElement.prototype.insertAdjacentElement, pa = window.HTMLElement.prototype.insertAdjacentHTML; var qa = function () { var a = new Set; "annotation-xml color-profile font-face font-face-src font-face-uri font-face-format font-face-name missing-glyph".split(" ").forEach(function (b) { return a.add(b) }); return a }(); function ra(a) { var b = qa.has(a); a = /^[a-z][.0-9_a-z]*-[-.0-9_a-z]*$/.test(a); return !b && a } var sa = document.contains ? document.contains.bind(document) : document.documentElement.contains.bind(document.documentElement);
            function J(a) { var b = a.isConnected; if (void 0 !== b) return b; if (sa(a)) return !0; for (; a && !(a.__CE_isImportDocument || a instanceof Document);)a = a.parentNode || (window.ShadowRoot && a instanceof ShadowRoot ? a.host : void 0); return !(!a || !(a.__CE_isImportDocument || a instanceof Document)) } function K(a) { var b = a.children; if (b) return Array.prototype.slice.call(b); b = []; for (a = a.firstChild; a; a = a.nextSibling)a.nodeType === Node.ELEMENT_NODE && b.push(a); return b }
            function L(a, b) { for (; b && b !== a && !b.nextSibling;)b = b.parentNode; return b && b !== a ? b.nextSibling : null }
            function M(a, b, c) { for (var e = a; e;) { if (e.nodeType === Node.ELEMENT_NODE) { var d = e; b(d); var f = d.localName; if ("link" === f && "import" === d.getAttribute("rel")) { e = d.import; void 0 === c && (c = new Set); if (e instanceof Node && !c.has(e)) for (c.add(e), e = e.firstChild; e; e = e.nextSibling)M(e, b, c); e = L(a, d); continue } else if ("template" === f) { e = L(a, d); continue } if (d = d.__CE_shadowRoot) for (d = d.firstChild; d; d = d.nextSibling)M(d, b, c) } e = e.firstChild ? e.firstChild : L(a, e) } }; function ta() { var a = !(null === N || void 0 === N || !N.noDocumentConstructionObserver), b = !(null === N || void 0 === N || !N.shadyDomFastWalk); this.f = []; this.s = []; this.c = !1; this.shadyDomFastWalk = b; this.K = !a } function O(a, b, c, e) { var d = window.ShadyDom; if (a.shadyDomFastWalk && d && d.inUse) { if (b.nodeType === Node.ELEMENT_NODE && c(b), b.querySelectorAll) for (a = d.nativeMethods.querySelectorAll.call(b, "*"), b = 0; b < a.length; b++)c(a[b]) } else M(b, c, e) } function ua(a, b) { a.c = !0; a.f.push(b) } function va(a, b) { a.c = !0; a.s.push(b) }
            function P(a, b) { a.c && O(a, b, function (c) { return Q(a, c) }) } function Q(a, b) { if (a.c && !b.__CE_patched) { b.__CE_patched = !0; for (var c = 0; c < a.f.length; c++)a.f[c](b); for (c = 0; c < a.s.length; c++)a.s[c](b) } } function R(a, b) { var c = []; O(a, b, function (d) { return c.push(d) }); for (b = 0; b < c.length; b++) { var e = c[b]; 1 === e.__CE_state ? a.connectedCallback(e) : S(a, e) } } function T(a, b) { var c = []; O(a, b, function (d) { return c.push(d) }); for (b = 0; b < c.length; b++) { var e = c[b]; 1 === e.__CE_state && a.disconnectedCallback(e) } }
            function U(a, b, c) {
                c = void 0 === c ? {} : c; var e = c.L, d = c.upgrade || function (g) { return S(a, g) }, f = []; O(a, b, function (g) {
                    a.c && Q(a, g); if ("link" === g.localName && "import" === g.getAttribute("rel")) {
                        var h = g.import; h instanceof Node && (h.__CE_isImportDocument = !0, h.__CE_registry = document.__CE_registry); h && "complete" === h.readyState ? h.__CE_documentLoadHandled = !0 : g.addEventListener("load", function () {
                            var k = g.import; if (!k.__CE_documentLoadHandled) {
                                k.__CE_documentLoadHandled = !0; var l = new Set; e && (e.forEach(function (m) { return l.add(m) }),
                                    l.delete(k)); U(a, k, { L: l, upgrade: d })
                            }
                        })
                    } else f.push(g)
                }, e); for (b = 0; b < f.length; b++)d(f[b])
            } function S(a, b) { try { var c = a.G(b.ownerDocument, b.localName); c && a.I(b, c) } catch (e) { V(e) } } n = ta.prototype;
            n.I = function (a, b) {
                if (void 0 === a.__CE_state) {
                    b.constructionStack.push(a); try { try { if (new b.constructorFunction !== a) throw Error("The custom element constructor did not produce the element being upgraded."); } finally { b.constructionStack.pop() } } catch (f) { throw a.__CE_state = 2, f; } a.__CE_state = 1; a.__CE_definition = b; if (b.attributeChangedCallback && a.hasAttributes()) { b = b.observedAttributes; for (var c = 0; c < b.length; c++) { var e = b[c], d = a.getAttribute(e); null !== d && this.attributeChangedCallback(a, e, null, d, null) } } J(a) &&
                        this.connectedCallback(a)
                }
            }; n.connectedCallback = function (a) { var b = a.__CE_definition; if (b.connectedCallback) try { b.connectedCallback.call(a) } catch (c) { V(c) } }; n.disconnectedCallback = function (a) { var b = a.__CE_definition; if (b.disconnectedCallback) try { b.disconnectedCallback.call(a) } catch (c) { V(c) } }; n.attributeChangedCallback = function (a, b, c, e, d) { var f = a.__CE_definition; if (f.attributeChangedCallback && -1 < f.observedAttributes.indexOf(b)) try { f.attributeChangedCallback.call(a, b, c, e, d) } catch (g) { V(g) } };
            n.G = function (a, b) { var c = a.__CE_registry; if (c && (a.defaultView || a.__CE_isImportDocument)) return W(c, b) };
            function wa(a, b, c, e) {
                var d = b.__CE_registry; if (d && (null === e || "http://www.w3.org/1999/xhtml" === e) && (d = W(d, c))) try {
                    var f = new d.constructorFunction; if (void 0 === f.__CE_state || void 0 === f.__CE_definition) throw Error("Failed to construct '" + c + "': The returned value was not constructed with the HTMLElement constructor."); if ("http://www.w3.org/1999/xhtml" !== f.namespaceURI) throw Error("Failed to construct '" + c + "': The constructed element's namespace must be the HTML namespace."); if (f.hasAttributes()) throw Error("Failed to construct '" +
                        c + "': The constructed element must not have any attributes."); if (null !== f.firstChild) throw Error("Failed to construct '" + c + "': The constructed element must not have any children."); if (null !== f.parentNode) throw Error("Failed to construct '" + c + "': The constructed element must not have a parent node."); if (f.ownerDocument !== b) throw Error("Failed to construct '" + c + "': The constructed element's owner document is incorrect."); if (f.localName !== c) throw Error("Failed to construct '" + c + "': The constructed element's local name is incorrect.");
                    return f
                } catch (g) { return V(g), b = null === e ? p.call(b, c) : q.call(b, e, c), Object.setPrototypeOf(b, HTMLUnknownElement.prototype), b.__CE_state = 2, b.__CE_definition = void 0, Q(a, b), b } b = null === e ? p.call(b, c) : q.call(b, e, c); Q(a, b); return b
            }
            function V(a) {
                var b = a.message, c = a.sourceURL || a.fileName || "", e = a.line || a.lineNumber || 0, d = a.column || a.columnNumber || 0, f = void 0; void 0 === ErrorEvent.prototype.initErrorEvent ? f = new ErrorEvent("error", { cancelable: !0, message: b, filename: c, lineno: e, colno: d, error: a }) : (f = document.createEvent("ErrorEvent"), f.initErrorEvent("error", !1, !0, b, c, e), f.preventDefault = function () { Object.defineProperty(this, "defaultPrevented", { configurable: !0, get: function () { return !0 } }) }); void 0 === f.error && Object.defineProperty(f, "error",
                    { configurable: !0, enumerable: !0, get: function () { return a } }); window.dispatchEvent(f); f.defaultPrevented || console.error(a)
            }; function xa() { var a = this; this.D = void 0; this.C = new Promise(function (b) { a.H = b }) } xa.prototype.resolve = function (a) { if (this.D) throw Error("Already resolved."); this.D = a; this.H(a) }; function X(a) { var b = document; this.l = void 0; this.a = a; this.g = b; U(this.a, this.g); "loading" === this.g.readyState && (this.l = new MutationObserver(this.F.bind(this)), this.l.observe(this.g, { childList: !0, subtree: !0 })) } X.prototype.disconnect = function () { this.l && this.l.disconnect() }; X.prototype.F = function (a) { var b = this.g.readyState; "interactive" !== b && "complete" !== b || this.disconnect(); for (b = 0; b < a.length; b++)for (var c = a[b].addedNodes, e = 0; e < c.length; e++)U(this.a, c[e]) }; function Y(a) { this.i = new Map; this.j = new Map; this.v = new Map; this.o = !1; this.u = new Map; this.h = function (b) { return b() }; this.b = !1; this.m = []; this.a = a; this.A = a.K ? new X(a) : void 0 } n = Y.prototype; n.J = function (a, b) { var c = this; if (!(b instanceof Function)) throw new TypeError("Custom element constructor getters must be functions."); ya(this, a); this.i.set(a, b); this.m.push(a); this.b || (this.b = !0, this.h(function () { return c.B() })) };
            n.define = function (a, b) { var c = this; if (!(b instanceof Function)) throw new TypeError("Custom element constructors must be functions."); ya(this, a); za(this, a, b); this.m.push(a); this.b || (this.b = !0, this.h(function () { return c.B() })) }; function ya(a, b) { if (!ra(b)) throw new SyntaxError("The element name '" + b + "' is not valid."); if (W(a, b)) throw Error("A custom element with name '" + (b + "' has already been defined.")); if (a.o) throw Error("A custom element is already being defined."); }
            function za(a, b, c) {
                a.o = !0; var e; try { var d = c.prototype; if (!(d instanceof Object)) throw new TypeError("The custom element constructor's prototype is not an object."); var f = function (m) { var y = d[m]; if (void 0 !== y && !(y instanceof Function)) throw Error("The '" + m + "' callback must be a function."); return y }; var g = f("connectedCallback"); var h = f("disconnectedCallback"); var k = f("adoptedCallback"); var l = (e = f("attributeChangedCallback")) && c.observedAttributes || [] } catch (m) { throw m; } finally { a.o = !1 } c = {
                    localName: b,
                    constructorFunction: c, connectedCallback: g, disconnectedCallback: h, adoptedCallback: k, attributeChangedCallback: e, observedAttributes: l, constructionStack: []
                }; a.j.set(b, c); a.v.set(c.constructorFunction, c); return c
            } n.upgrade = function (a) { U(this.a, a) };
            n.B = function () { var a = this; if (!1 !== this.b) { this.b = !1; for (var b = [], c = this.m, e = new Map, d = 0; d < c.length; d++)e.set(c[d], []); U(this.a, document, { upgrade: function (k) { if (void 0 === k.__CE_state) { var l = k.localName, m = e.get(l); m ? m.push(k) : a.j.has(l) && b.push(k) } } }); for (d = 0; d < b.length; d++)S(this.a, b[d]); for (d = 0; d < c.length; d++) { for (var f = c[d], g = e.get(f), h = 0; h < g.length; h++)S(this.a, g[h]); (f = this.u.get(f)) && f.resolve(void 0) } c.length = 0 } }; n.get = function (a) { if (a = W(this, a)) return a.constructorFunction };
            n.whenDefined = function (a) { if (!ra(a)) return Promise.reject(new SyntaxError("'" + a + "' is not a valid custom element name.")); var b = this.u.get(a); if (b) return b.C; b = new xa; this.u.set(a, b); var c = this.j.has(a) || this.i.has(a); a = -1 === this.m.indexOf(a); c && a && b.resolve(void 0); return b.C }; n.polyfillWrapFlushCallback = function (a) { this.A && this.A.disconnect(); var b = this.h; this.h = function (c) { return a(function () { return b(c) }) } };
            function W(a, b) { var c = a.j.get(b); if (c) return c; if (c = a.i.get(b)) { a.i.delete(b); try { return za(a, b, c()) } catch (e) { V(e) } } } window.CustomElementRegistry = Y; Y.prototype.define = Y.prototype.define; Y.prototype.upgrade = Y.prototype.upgrade; Y.prototype.get = Y.prototype.get; Y.prototype.whenDefined = Y.prototype.whenDefined; Y.prototype.polyfillDefineLazy = Y.prototype.J; Y.prototype.polyfillWrapFlushCallback = Y.prototype.polyfillWrapFlushCallback; function Z(a, b, c) { function e(d) { return function (f) { for (var g = [], h = 0; h < arguments.length; ++h)g[h - 0] = arguments[h]; h = []; for (var k = [], l = 0; l < g.length; l++) { var m = g[l]; m instanceof Element && J(m) && k.push(m); if (m instanceof DocumentFragment) for (m = m.firstChild; m; m = m.nextSibling)h.push(m); else h.push(m) } d.apply(this, g); for (g = 0; g < k.length; g++)T(a, k[g]); if (J(this)) for (g = 0; g < h.length; g++)k = h[g], k instanceof Element && R(a, k) } } void 0 !== c.prepend && (b.prepend = e(c.prepend)); void 0 !== c.append && (b.append = e(c.append)) }; function Aa(a) { Document.prototype.createElement = function (b) { return wa(a, this, b, null) }; Document.prototype.importNode = function (b, c) { b = aa.call(this, b, !!c); this.__CE_registry ? U(a, b) : P(a, b); return b }; Document.prototype.createElementNS = function (b, c) { return wa(a, this, c, b) }; Z(a, Document.prototype, { prepend: ba, append: ca }) }; function Ba(a) {
                function b(e) { return function (d) { for (var f = [], g = 0; g < arguments.length; ++g)f[g - 0] = arguments[g]; g = []; for (var h = [], k = 0; k < f.length; k++) { var l = f[k]; l instanceof Element && J(l) && h.push(l); if (l instanceof DocumentFragment) for (l = l.firstChild; l; l = l.nextSibling)g.push(l); else g.push(l) } e.apply(this, f); for (f = 0; f < h.length; f++)T(a, h[f]); if (J(this)) for (f = 0; f < g.length; f++)h = g[f], h instanceof Element && R(a, h) } } var c = Element.prototype; void 0 !== ja && (c.before = b(ja)); void 0 !== ka && (c.after = b(ka)); void 0 !==
                    la && (c.replaceWith = function (e) { for (var d = [], f = 0; f < arguments.length; ++f)d[f - 0] = arguments[f]; f = []; for (var g = [], h = 0; h < d.length; h++) { var k = d[h]; k instanceof Element && J(k) && g.push(k); if (k instanceof DocumentFragment) for (k = k.firstChild; k; k = k.nextSibling)f.push(k); else f.push(k) } h = J(this); la.apply(this, d); for (d = 0; d < g.length; d++)T(a, g[d]); if (h) for (T(a, this), d = 0; d < f.length; d++)g = f[d], g instanceof Element && R(a, g) }); void 0 !== ma && (c.remove = function () { var e = J(this); ma.call(this); e && T(a, this) })
            }; function Ca(a) {
                function b(d, f) { Object.defineProperty(d, "innerHTML", { enumerable: f.enumerable, configurable: !0, get: f.get, set: function (g) { var h = this, k = void 0; J(this) && (k = [], O(a, this, function (y) { y !== h && k.push(y) })); f.set.call(this, g); if (k) for (var l = 0; l < k.length; l++) { var m = k[l]; 1 === m.__CE_state && a.disconnectedCallback(m) } this.ownerDocument.__CE_registry ? U(a, this) : P(a, this); return g } }) } function c(d, f) { d.insertAdjacentElement = function (g, h) { var k = J(h); g = f.call(this, g, h); k && T(a, h); J(g) && R(a, h); return g } } function e(d,
                    f) {
                        function g(h, k) { for (var l = []; h !== k; h = h.nextSibling)l.push(h); for (k = 0; k < l.length; k++)U(a, l[k]) } d.insertAdjacentHTML = function (h, k) {
                            h = h.toLowerCase(); if ("beforebegin" === h) { var l = this.previousSibling; f.call(this, h, k); g(l || this.parentNode.firstChild, this) } else if ("afterbegin" === h) l = this.firstChild, f.call(this, h, k), g(this.firstChild, l); else if ("beforeend" === h) l = this.lastChild, f.call(this, h, k), g(l || this.firstChild, null); else if ("afterend" === h) l = this.nextSibling, f.call(this, h, k), g(this.nextSibling, l);
                            else throw new SyntaxError("The value provided (" + String(h) + ") is not one of 'beforebegin', 'afterbegin', 'beforeend', or 'afterend'.");
                        }
                } z && (Element.prototype.attachShadow = function (d) { d = z.call(this, d); if (a.c && !d.__CE_patched) { d.__CE_patched = !0; for (var f = 0; f < a.f.length; f++)a.f[f](d) } return this.__CE_shadowRoot = d }); A && A.get ? b(Element.prototype, A) : I && I.get ? b(HTMLElement.prototype, I) : va(a, function (d) {
                    b(d, {
                        enumerable: !0, configurable: !0, get: function () { return r.call(this, !0).innerHTML }, set: function (f) {
                            var g =
                                "template" === this.localName, h = g ? this.content : this, k = q.call(document, this.namespaceURI, this.localName); for (k.innerHTML = f; 0 < h.childNodes.length;)v.call(h, h.childNodes[0]); for (f = g ? k.content : k; 0 < f.childNodes.length;)t.call(h, f.childNodes[0])
                        }
                    })
                }); Element.prototype.setAttribute = function (d, f) { if (1 !== this.__CE_state) return C.call(this, d, f); var g = B.call(this, d); C.call(this, d, f); f = B.call(this, d); a.attributeChangedCallback(this, d, g, f, null) }; Element.prototype.setAttributeNS = function (d, f, g) {
                    if (1 !== this.__CE_state) return F.call(this,
                        d, f, g); var h = E.call(this, d, f); F.call(this, d, f, g); g = E.call(this, d, f); a.attributeChangedCallback(this, f, h, g, d)
                }; Element.prototype.removeAttribute = function (d) { if (1 !== this.__CE_state) return D.call(this, d); var f = B.call(this, d); D.call(this, d); null !== f && a.attributeChangedCallback(this, d, f, null, null) }; Element.prototype.removeAttributeNS = function (d, f) { if (1 !== this.__CE_state) return G.call(this, d, f); var g = E.call(this, d, f); G.call(this, d, f); var h = E.call(this, d, f); g !== h && a.attributeChangedCallback(this, f, g, h, d) };
                oa ? c(HTMLElement.prototype, oa) : H && c(Element.prototype, H); pa ? e(HTMLElement.prototype, pa) : fa && e(Element.prototype, fa); Z(a, Element.prototype, { prepend: ha, append: ia }); Ba(a)
            }; var Da = {}; function Ea(a) {
                function b() {
                    var c = this.constructor; var e = document.__CE_registry.v.get(c); if (!e) throw Error("Failed to construct a custom element: The constructor was not registered with `customElements`."); var d = e.constructionStack; if (0 === d.length) return d = p.call(document, e.localName), Object.setPrototypeOf(d, c.prototype), d.__CE_state = 1, d.__CE_definition = e, Q(a, d), d; var f = d.length - 1, g = d[f]; if (g === Da) throw Error("Failed to construct '" + e.localName + "': This element was already constructed."); d[f] = Da;
                    Object.setPrototypeOf(g, c.prototype); Q(a, g); return g
                } b.prototype = na.prototype; Object.defineProperty(HTMLElement.prototype, "constructor", { writable: !0, configurable: !0, enumerable: !1, value: b }); window.HTMLElement = b
            }; function Fa(a) {
                function b(c, e) { Object.defineProperty(c, "textContent", { enumerable: e.enumerable, configurable: !0, get: e.get, set: function (d) { if (this.nodeType === Node.TEXT_NODE) e.set.call(this, d); else { var f = void 0; if (this.firstChild) { var g = this.childNodes, h = g.length; if (0 < h && J(this)) { f = Array(h); for (var k = 0; k < h; k++)f[k] = g[k] } } e.set.call(this, d); if (f) for (d = 0; d < f.length; d++)T(a, f[d]) } } }) } Node.prototype.insertBefore = function (c, e) {
                    if (c instanceof DocumentFragment) {
                        var d = K(c); c = u.call(this, c, e); if (J(this)) for (e =
                            0; e < d.length; e++)R(a, d[e]); return c
                    } d = c instanceof Element && J(c); e = u.call(this, c, e); d && T(a, c); J(this) && R(a, c); return e
                }; Node.prototype.appendChild = function (c) { if (c instanceof DocumentFragment) { var e = K(c); c = t.call(this, c); if (J(this)) for (var d = 0; d < e.length; d++)R(a, e[d]); return c } e = c instanceof Element && J(c); d = t.call(this, c); e && T(a, c); J(this) && R(a, c); return d }; Node.prototype.cloneNode = function (c) { c = r.call(this, !!c); this.ownerDocument.__CE_registry ? U(a, c) : P(a, c); return c }; Node.prototype.removeChild = function (c) {
                    var e =
                        c instanceof Element && J(c), d = v.call(this, c); e && T(a, c); return d
                }; Node.prototype.replaceChild = function (c, e) { if (c instanceof DocumentFragment) { var d = K(c); c = w.call(this, c, e); if (J(this)) for (T(a, e), e = 0; e < d.length; e++)R(a, d[e]); return c } d = c instanceof Element && J(c); var f = w.call(this, c, e), g = J(this); g && T(a, e); d && T(a, c); g && R(a, c); return f }; x && x.get ? b(Node.prototype, x) : ua(a, function (c) {
                    b(c, {
                        enumerable: !0, configurable: !0, get: function () {
                            for (var e = [], d = this.firstChild; d; d = d.nextSibling)d.nodeType !== Node.COMMENT_NODE &&
                                e.push(d.textContent); return e.join("")
                        }, set: function (e) { for (; this.firstChild;)v.call(this, this.firstChild); null != e && "" !== e && t.call(this, document.createTextNode(e)) }
                    })
                })
            }; var N = window.customElements; function Ga() { var a = new ta; Ea(a); Aa(a); Z(a, DocumentFragment.prototype, { prepend: da, append: ea }); Fa(a); Ca(a); a = new Y(a); document.__CE_registry = a; Object.defineProperty(window, "customElements", { configurable: !0, enumerable: !0, value: a }) } N && !N.forcePolyfill && "function" == typeof N.define && "function" == typeof N.get || Ga(); window.__CE_installPolyfill = Ga;/*

Copyright (c) 2017 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/
        })();
        (function () { var b = window.document; window.WebComponents = window.WebComponents || {}; var a = function () { window.removeEventListener("DOMContentLoaded", a); window.WebComponents.ready = !0; var c = b.createEvent("CustomEvent"); c.initEvent("WebComponentsReady", !0, !0); setTimeout(function () { window.document.dispatchEvent(c) }, 0) }; "complete" === b.readyState ? a() : window.addEventListener("DOMContentLoaded", a) })();
    </script>
    <script data-source="gwdparticleeffects_min.js" data-version="4" data-exports-type="gwd-particleeffects">(function () {/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
            'use strict'; var f = "function" == typeof Object.create ? Object.create : function (a) { var b = function () { }; b.prototype = a; return new b }, l; if ("function" == typeof Object.setPrototypeOf) l = Object.setPrototypeOf; else { var m; a: { var n = { G: !0 }, p = {}; try { p.__proto__ = n; m = p.G; break a } catch (a) { } m = !1 } l = m ? function (a, b) { a.__proto__ = b; if (a.__proto__ !== b) throw new TypeError(a + " is not extensible"); return a } : null }
            var q = l, r = function (a, b) { function c() { } c.prototype = b.prototype; a.M = b.prototype; a.prototype = new c; a.prototype.constructor = a; a.N = function (d, e, h) { for (var k = Array(arguments.length - 2), g = 2; g < arguments.length; g++)k[g - 2] = arguments[g]; return b.prototype[e].apply(d, k) } }; var t = function (a, b, c) { a = parseInt(a.getAttribute(b), 10); isNaN(a) && (a = c); return a }, u = function (a) { a = parseFloat(a.getAttribute("time-limit")); isFinite(a) || (a = -1); return 0 < a ? a : -1 }; var v = /[^\d]+$/, w = function (a, b, c) { if (!a.hasAttribute(b)) return 0; b = a.getAttribute(b); if (isNaN(parseFloat(b))) c = 0; else { a = parseFloat(b); (b = (b = b.match(v)) && b[0] || null) && (b = b.trim()); var d = a; "%" == b && (d = Number((a / 100 * c).toFixed(2))); c = d } return c }; var x = function (a, b) { var c = void 0 === c ? null : c; var d = document.createEvent("CustomEvent"); d.initCustomEvent(a, !0, !0, c); b.dispatchEvent(d) }; var y = function (a) { return "gwd-page" == a.tagName.toLowerCase() || "gwd-page" == a.getAttribute("is") }, z = function (a) { if (y(a)) return a; for (; a && 9 != a.nodeType;)if ((a = a.parentElement) && y(a)) return a; return null }; function A(a) { if (Error.captureStackTrace) Error.captureStackTrace(this, A); else { var b = Error().stack; b && (this.stack = b) } a && (this.message = String(a)) } r(A, Error); A.prototype.name = "CustomError"; var B = function (a, b) { a = a.split("%s"); for (var c = "", d = a.length - 1, e = 0; e < d; e++)c += a[e] + (e < b.length ? b[e] : "%s"); A.call(this, c + a[d]) }; r(B, A); B.prototype.name = "AssertionError"; var C = function (a, b, c) { if ("number" !== typeof a) { var d = typeof a, e = ["object" != d ? d : a ? Array.isArray(a) ? "array" : d : "null", a]; d = "Assertion failed"; b ? (d += ": " + b, e = Array.prototype.slice.call(arguments, 2)) : d += ": Expected number but got %s: %s."; throw new B("" + d, e || []); } return a }; var D = function () { var a = HTMLElement.call(this) || this; a.canvas = null; a.j = !1; a.a = []; a.s = a.J.bind(a); a.I = a.K.bind(a); a.h = a.L.bind(a); a.l = []; a.u = a.B.bind(a); a.b = null; a.c = 2; a.m = null; a.i = -1; a.o = null; a.D = !1; return a }, E = HTMLElement; D.prototype = f(E.prototype); D.prototype.constructor = D; if (q) q(D, E); else for (var G in E) if ("prototype" != G) if (Object.defineProperties) { var H = Object.getOwnPropertyDescriptor(E, G); H && Object.defineProperty(D, G, H) } else D[G] = E[G]; D.M = E.prototype;
            D.prototype.connectedCallback = function () {
                var a = this; this.width = this.clientWidth; this.height = this.clientHeight; this.g = window.devicePixelRatio; this.canvas || (this.canvas = this.ownerDocument.createElement("canvas"), this.appendChild(this.canvas)); this.canvas.style.width = this.width + "px"; this.canvas.style.height = this.height + "px"; this.canvas.width = this.width * this.g; this.canvas.height = this.height * this.g; this.f = this.canvas.getContext("2d"); this.H = this.hasAttribute("autoplay"); null === this.o ? this.i = 1E3 * u(this) :
                    this.D && this.play(); setTimeout(function () { if (!a.gwdIsLoaded()) { var b = z(a); b ? b.gwdIsLoaded() && a.gwdLoad() : a.gwdLoad() } }, 0)
            }; D.prototype.disconnectedCallback = function () { this.gwdIsLoaded() ? (this.D = 0 == this.c, this.pause(!1)) : I(this) };
            D.prototype.gwdLoad = function () {
                if (!this.gwdIsLoaded()) {
                    I(this); for (var a = 0, b = 0; b < this.children.length; b++) {
                        var c = this.children[b]; if (J(c)) c.gwdIsLoaded() || K(this, c), this.addEventListener("request-reload", this.I, !1); else if ("image" == c.getAttribute("assettype")) {
                            var d = c.getAttribute("source"), e = w(c, "left", this.width), h = w(c, "top", this.height), k = w(c, "width", this.width), g = w(c, "height", this.height), F = t(c, "opacity", 100); d = {
                                canvas: null, src: d, A: e * this.g, C: h * this.g, F: k * this.g, v: g * this.g, opacity: Math.min((0 <=
                                    F ? F : 100) / 100, 1)
                            }; e = this.ownerDocument.createElement("img"); this.a.push(e); e.addEventListener("load", this.h, !1); e.addEventListener("error", this.h, !1); this.l[a] = d; c.setAttribute("image-index", a); e.setAttribute("image-index", a++); e.width = d.F; e.height = d.v; e.src = d.src
                        }
                    } this.j = !0; L(this)
                }
            }; D.prototype.gwdIsLoaded = function () { return this.j && 0 == this.a.length };
            var K = function (a, b) { -1 == a.a.indexOf(b) && (a.a.push(b), b.addEventListener("ready", a.s, !1)); b.gwdLoad() }, I = function (a) { for (; a.a.length;) { var b = a.a.pop(); b.removeEventListener("ready", a.s, !1); b.removeEventListener("load", a.h, !1); b.removeEventListener("error", a.h, !1) } a.j = !1; a.l.length = 0 }, L = function (a) { a.j && 0 == a.a.length && (x("ready", a), a.H ? a.play(!0) : null != a.m && a.play(a.m), a.m = null) };
            D.prototype.J = function (a) { a = a.target; var b = this.a.indexOf(a); 0 <= b && (this.a.splice(b, 1), a.removeEventListener("ready", this.s, !1), L(this)) }; D.prototype.K = function (a) { K(this, a.target) };
            D.prototype.L = function (a) {
                var b = this, c = a.target; c.removeEventListener("load", this.h, !1); c.removeEventListener("error", this.h, !1); var d = this.a.indexOf(c); if (0 <= d) {
                    var e = parseInt(c.getAttribute("image-index"), 10); if ("load" == a.type) { var h = this.ownerDocument.createElement("canvas"); h.width = c.width; h.height = c.height; var k = this.l[e], g = h.getContext("2d"); g.globalAlpha = k.opacity; setTimeout(function () { d = b.a.indexOf(c); b.a.splice(d, 1); g.drawImage(c, 0, 0, c.width, c.height); k.canvas = h; L(b) }, 50) } else this.a.splice(d,
                        1), L(this)
                }
            }; var J = function (a) { return "gwd-particles" == a.tagName.toLowerCase() }; D.prototype.play = function (a) { a = void 0 === a ? !0 : a; if (!this.gwdIsLoaded()) this.m = 0 != a; else if (0 != this.c) { null == this.o && (this.o = Date.now()); if (2 == this.c) for (var b = 0; b < this.children.length; b++) { var c = this.children[b].hasAttribute("autoplay"); J(this.children[b]) && c && this.children[b].play() } 0 == a ? this.B(!1) : this.b = requestAnimationFrame(this.u); this.c = 0 } };
            D.prototype.pause = function (a) { a = void 0 === a ? !0 : a; this.b && (cancelAnimationFrame(this.b), this.b = null, a && (this.i = -1), this.c = 1) }; D.prototype.stop = function () { if (2 != this.c) { for (var a = 0; a < this.children.length; a++)J(this.children[a]) && this.children[a].stop(); this.b && (cancelAnimationFrame(this.b), this.b = null, this.i = -1); this.c = 2; this.f.clearRect(0, 0, this.canvas.width, this.canvas.height) } };
            D.prototype.B = function (a) {
                if (0 != a && 0 < this.i && Date.now() - C(this.o) > this.i) this.pause(), x("timelimitreached", this); else {
                    this.f.clearRect(0, 0, this.canvas.width, this.canvas.height); for (var b = 0; b < this.children.length; b++) {
                        var c = this.children[b]; c.hasAttribute("hidden") || (J(c) && c.gwdIsLoaded() ? c.updateAndDraw() : "image" == c.getAttribute("assettype") && (c = t(c, "image-index", -1), -1 != c && (c = this.l[c], c.canvas ? this.f.drawImage(c.canvas, c.A, c.C) : this.hasAttribute("data-gwd-node") && (this.f.strokeStyle = "#c0c0c0", this.f.lineWidth =
                            1, this.f.strokeRect(c.A, c.C, c.F, c.v)))))
                    } 0 != a && (this.b = requestAnimationFrame(this.u))
                }
            }; customElements.define("gwd-particleeffects", D);
        }).call(this);
    </script>
    <script data-source="gwdparticles_min.js" data-version="2" data-exports-type="gwd-particles">(function () {/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
            'use strict'; var aa = "function" == typeof Object.create ? Object.create : function (a) { var b = function () { }; b.prototype = a; return new b }, ba = function (a) { a = ["object" == typeof globalThis && globalThis, a, "object" == typeof window && window, "object" == typeof self && self, "object" == typeof global && global]; for (var b = 0; b < a.length; ++b) { var d = a[b]; if (d && d.Math == Math) return d } throw Error("Cannot find global object"); }, ca = ba(this), k;
            if ("function" == typeof Object.setPrototypeOf) k = Object.setPrototypeOf; else { var q; a: { var da = { Qa: !0 }, u = {}; try { u.__proto__ = da; q = u.Qa; break a } catch (a) { } q = !1 } k = q ? function (a, b) { a.__proto__ = b; if (a.__proto__ !== b) throw new TypeError(a + " is not extensible"); return a } : null } var v = k; var ea = { o: 0, s: 0, u: 0, v: 0, A: "#fff", B: "#fff", C: 0, l: 0, g: 0, D: "0px", F: "0px", G: "0px", H: "0px", loop: !1, I: 0, J: 1, K: 1, L: 0, N: !1, shape: "square", P: 1, R: 1, S: 0, T: 0, i: 0, j: 0, aa: "", O: !1, m: 1, U: 0, f: 1, V: 1 }, fa = { o: 0, s: 0, u: 280, v: 260, A: "#fff", B: "#fff", C: 0, l: .005, g: 2, D: "100%", F: "0%", G: "10%", H: "0%", loop: !0, I: 0, J: 1, K: .1, L: 0, N: !0, shape: "circle", P: 12, R: 8, S: 0, T: 0, i: 2, j: 1, aa: "", O: !1, m: 1, U: 0, f: 1, V: 1 }, ha = {
                o: 0, s: .6, u: 271, v: 269, A: "#fff", B: "#fff", C: 0, l: .01, g: 2, D: "100%", F: "0%", G: "10%", H: "0%", loop: !0, I: 0, J: 1, K: .5, L: 0, N: !0, shape: "line", P: 25,
                R: 10, S: 0, T: 100, i: 10, j: 8, aa: "", O: !1, m: 1, U: 0, f: 1, V: 1
            }, ia = { o: 0, s: .6, u: 100, v: 80, A: "#ffdc00", B: "#dc000a", C: 1.2, l: 0, g: 1, D: "20px", F: "10px", G: "40px", H: "35px", loop: !0, I: 10, J: .3, K: .1, L: -.3, N: !1, shape: "teardrop", P: 20, R: 20, S: -30, T: 100, i: 1, j: .5, aa: "", O: !0, m: 20, U: .18, f: 1, V: 30 }, ja = { o: 0, s: .6, u: 100, v: 80, A: "#ffdc00", B: "#dc000a", C: 1, l: 0, g: 2, D: "50px", F: "20px", G: "100px", H: "95px", loop: !0, I: 15, J: .3, K: .1, L: -.3, N: !1, shape: "teardrop", P: 40, R: 40, S: -30, T: 100, i: 2, j: 1, aa: "", O: !0, m: 20, U: .18, f: 1, V: 30 }, ka = {
                o: 0, s: .6, u: 100, v: 80, A: "#ffdc00",
                B: "#dc000a", C: .8, l: 0, g: 4, D: "80px", F: "30px", G: "180px", H: "175px", loop: !0, I: 15, J: .3, K: .1, L: -.3, N: !1, shape: "teardrop", P: 100, R: 100, S: -54, T: 100, i: 3, j: 2, aa: "", O: !0, m: 20, U: .18, f: 1, V: 25
            }, la = { o: 0, s: 0, u: 90, v: 90, A: "#dcdcdc", B: "#dcdcdc", C: 0, l: 0, g: 25, D: "22px", F: "10px", G: "120px", H: "100px", loop: !0, I: 8, J: .03, K: .03, L: -.018, N: !0, shape: "teardrop", P: 15, R: 15, S: -.06, T: 100, i: 1, j: .8, aa: "", O: !0, m: 60, U: .6, f: .5, V: 40 }, ma = {
                o: 0, s: .06, u: 100, v: 80, A: "#dcdcdc", B: "#dcdcdc", C: 0, l: 0, g: 2, D: "35px", F: "10px", G: "150px", H: "148px", loop: !0, I: 300,
                J: .1, K: .1, L: -.03, N: !0, shape: "circle", P: 20, R: 10, S: -1.2, T: 100, i: .8, j: .8, aa: "", O: !0, m: 10, U: 0, f: .5, V: 1
            }; var w = function (a, b, d) { a = parseInt(a.getAttribute(b), 10); isNaN(a) && (a = d); return a }, A = function (a, b, d) { a = w(a, b, d); return 0 < a ? a : d }, B = function (a, b, d) { a = parseFloat(a.getAttribute(b)); isFinite(a) || (a = d); return a }, C = function (a, b, d) { return a.hasAttribute(b) ? a.getAttribute(b) : d }, D = function (a, b, d) { switch (a.getAttribute(b)) { case "true": return !0; case "false": return !1; default: return d } }; var na = /[^\d]+$/, G = function (a, b, d, c) { if (!a.hasAttribute(b)) return d; a = a.getAttribute(b); return isNaN(parseFloat(a)) ? d : E(a, c) }, E = function (a, b) { var d = parseFloat(a); (a = (a = a.match(na)) && a[0] || null) && (a = a.trim()); var c = d; "%" == a && (c = Number((d / 100 * b).toFixed(2))); return c }; var oa = /^#(?:[0-9a-f]{3}){1,2}$/i, pa = /#(.)(.)(.)/, H = [60, 6E3], I = function (a) { if (!oa.test(a)) return null; 4 == a.length && (a = a.replace(pa, "#$1$1$2$2$3$3")); a = a.toLowerCase(); a = parseInt(a.substr(1), 16); return [a >> 16, a >> 8 & 255, a & 255] }, J = function (a, b, d, c, e) { b = B(a, b, c); a = B(a, d, e); b > a && (d = b, b = a, a = d); return [b, a] }, qa = function (a) { switch (a) { case "snow": return fa; case "rain": return ha; case "fire-small": return ia; case "fire-medium": return ja; case "fire-large": return ka; case "steam": return la; case "smoke": return ma; default: return ea } },
                K = function (a, b, d, c, e, f) { b = G(a, b, c, f); a = G(a, d, e, f); b > a && (d = b, b = a, a = d); return [b, a] }; var L = function (a, b, d) { return a + d * (b - a) }, M = function (a) { return a * a * a * (a * (6 * a - 15) + 10) }, P = function (a, b, d, c) { switch (a % 16) { case 0: return b + d; case 1: return -b + d; case 2: return b - d; case 3: return -b - d; case 4: return b + c; case 5: return -b + c; case 6: return b - c; case 7: return -b - c; case 8: return d + c; case 9: return -d + c; case 10: return d - c; case 11: return -d - c; case 12: return b + d; case 13: return -d + c; case 14: return -b + d; case 15: return -d - c; default: return 0 } }, ra = function () {
                    for (var a = Array(256), b = 0; b < a.length; ++b)a[b] = b; for (b = a.length -
                        1; 0 < b; --b) { var d = Math.floor(Math.random() * a.length), c = a[b]; a[b] = a[d]; a[d] = c } this.Wa = a.concat(a)
                }, Q = function (a, b, d, c) { var e = b & 255, f = d & 255, g = c & 255; b -= Math.floor(b); d -= Math.floor(d); c -= Math.floor(c); var l = M(b), h = M(d); a = a.Wa; return L(L(L(P(a[a[a[e] + f] + g], b, d, c), P(a[a[a[e + 1] + f] + g], b - 1, d, c), l), L(P(a[a[a[e] + f + 1] + g], b, d - 1, c), P(a[a[a[e + 1] + f + 1] + g], b - 1, d - 1, c), l), h), L(L(P(a[a[a[e] + f] + g + 1], b, d, c - 1), P(a[a[a[e + 1] + f] + g + 1], b - 1, d, c - 1), l), L(P(a[a[a[e] + f + 1] + g + 1], b, d - 1, c - 1), P(a[a[a[e + 1] + f + 1] + g + 1], b - 1, d - 1, c - 1), l), h), M(c)) }; var R = function (a) { this.Ia = a; this.Fa = []; this.length = this.la = 0 }; R.prototype.get = function (a) { return this.Fa[(a + this.la) % this.length] }; R.prototype.push = function (a) { this.length < this.Ia && this.length++; this.Fa[this.la] = a; this.la = (this.la + 1) % this.Ia }; var sa = 2 * Math.PI, S = function (a, b) { return a + Math.random() * (b - a) }, U = function (a, b) {
                    this.h = []; this.b = b; this.c = a.getContext("2d"); this.xa = window.devicePixelRatio; this.Ca = 1; this.Ga = []; this.Ha = []; if ("image" != this.b.pa.shape) a = null; else if ((a = this.b.pa.Va) && 0 != a.length) {
                        b = []; this.Ca = this.b.oa.max * this.xa; for (var d = 0; d < a.length; d++) {
                            var c = a[d], e = document.createElement("canvas"), f = e.getContext("2d"), g = this.Ca / Math.max(c.naturalWidth, c.naturalHeight), l = c.naturalWidth * g; g *= c.naturalHeight; e.width = Math.ceil(l);
                            e.height = Math.ceil(g); f.drawImage(c, 0, 0, l, g); b.push(e); this.Ga.push(-l / 2); this.Ha.push(-g / 2)
                        } a = b
                    } else this.b.pa.shape = "square", a = null; this.ya = a; this.ma = 0; this.Ta = 0 == this.b.g ? this.b.Aa : 1 / this.b.g; a = this.b.ca; this.wa = a.ha ? 0 : (a.ka - a.ta) * a.Ba; this.va = a.ha ? 0 : (a.ja - a.sa) * a.Ba; this.ua = a.ha ? 0 : (a.ia - a.ra) * a.Ba; this.Da = (a = this.b.Ka) ? new ra : null; this.Ea = a ? a.frequency : 1; this.$a = a ? a.Ya : 1; this.La = a && a.Za - 1 || 0; for (a = 0; a < this.b.Ja; a++)T(this)
                }; U.prototype.reset = function () { for (var a = this.ma = this.h.length = 0; a < this.b.Ja; a++)T(this) };
            var V = function (a) {
                var b = S(a.b.na.Na, a.b.na.Ma), d = S(a.b.na.Pa, a.b.na.Oa), c = S(a.b.oa.min, a.b.oa.max), e = S(a.b.za.min, a.b.za.max), f = a.b.ca, g = f.ta, l = f.sa, h = f.ra; f.ha && (h = Math.random(), g = (1 - h) * f.ta + h * f.ka, l = (1 - h) * f.sa + h * f.ja, h = (1 - h) * f.ra + h * f.ia); var n = S(a.b.qa.j, a.b.qa.i); f = S(a.b.qa.Sa, a.b.qa.Ra); var y = n * Math.cos(f); n *= Math.sin(f); var x = -1; a.ya && (x = Math.floor(S(0, a.ya.length))); return {
                    a: { positionX: b, positionY: d, size: c, Y: g, X: l, W: h, opacity: e, ea: !0, angle: f, fa: x }, velocityX: y, velocityY: n, f: a.$a, ba: a.La ? new R(a.La) :
                        null
                }
            }, T = function (a) {
                for (var b = Date.now() / a.Ea, d = 0; d < a.h.length; d++) {
                    var c = a.h[d], e = a; c.ba && c.ba.push({ positionX: c.a.positionX, positionY: c.a.positionY, size: c.a.size, Y: c.a.Y, X: c.a.X, W: c.a.W, opacity: c.a.opacity, angle: c.a.angle, fa: c.a.fa, ea: c.a.ea }); if (c.a.ea) {
                        c.a.positionX += c.velocityX; c.a.positionY += c.velocityY; if (e.Da && 0 < c.f) { var f = c.a.positionX / e.Ea, g = c.a.positionY / e.Ea; c.a.positionX += c.f * Q(e.Da, f, g, b); c.a.positionY += c.f * Q(e.Da, b, f, g); c.f += e.b.Ka.rate } c.a.size += e.b.oa.rate; c.a.opacity = Math.min(1,
                            c.a.opacity + e.b.za.rate); c.velocityX += e.b.acceleration.x; c.velocityY += e.b.acceleration.y; c.a.angle = Math.atan2(c.velocityY, c.velocityX); f = e.b.ca; f.ha || ((!e.wa || 1 < (f.ka - c.a.Y) / e.wa) && (!e.va || 1 < (f.ja - c.a.X) / e.va) && (!e.ua || 1 < (f.ia - c.a.W) / e.ua) ? (c.a.Y += e.wa, c.a.X += e.va, c.a.W += e.ua) : (c.a.Y = e.b.ca.ka, c.a.X = e.b.ca.ja, c.a.W = e.b.ca.ia))
                    } if (0 > c.a.positionX + c.a.size || c.a.positionX - c.a.size > a.b.width || 0 > c.a.positionY + c.a.size || c.a.positionY - c.a.size > a.b.height || 0 > c.a.opacity || 0 > c.a.size) a.b.Xa ? (c = c.ba, a.h[d] =
                        V(a), a.h[d].ba = c) : c.a.ea = !1
                } if (a.h.length < a.b.Aa) for (a.ma = Math.min(a.ma + a.Ta, a.b.Aa), b = Math.floor(a.ma) - a.h.length, d = 0; d < b; d++)a.h.push(V(a))
            }, ta = function (a, b) {
                if (b.ea) {
                    a.c.fillStyle = "rgba(" + Math.round(b.Y) + ", " + Math.round(b.X) + ", " + Math.round(b.W) + ", " + b.opacity + ")"; a.c.save(); a.c.translate(b.positionX, b.positionY); var d = b.size / a.Ca; a.c.scale(d, d); switch (a.b.pa.shape) {
                        case "circle": a.c.beginPath(); a.c.arc(0, 0, .5, 0, sa); a.c.fill(); break; case "line": a.c.beginPath(); a.c.rotate(b.angle); a.c.fillRect(-.5,
                            -.01, 1, .02); break; case "teardrop": a.c.beginPath(); a.c.moveTo(.08, -.5); a.c.bezierCurveTo(.13, -.21, .16, .04, .3, .07); a.c.bezierCurveTo(.44, .36, .13, .5, -.06, .5); a.c.bezierCurveTo(-.49, .14, -.41, 0, .08, -.5); a.c.fill(); break; case "image": a.c.globalAlpha = b.opacity; a.c.drawImage(a.ya[b.fa], a.Ga[b.fa], a.Ha[b.fa]); break; default: a.c.beginPath(), a.c.fillRect(-.5, -.5, 1, 1)
                    }a.c.restore()
                }
            }; var ua = function (a, b) { var d = void 0 === d ? null : d; var c = document.createEvent("CustomEvent"); c.initCustomEvent(a, !0, !0, d); b.dispatchEvent(c) }; var va = function (a) { return "gwd-page" == a.tagName.toLowerCase() || "gwd-page" == a.getAttribute("is") }, wa = function (a) { if (va(a)) return a; for (; a && 9 != a.nodeType;)if ((a = a.parentElement) && va(a)) return a; return null }, xa = function (a) { return (a = C(a, "sprite-image-src", "")) ? a.split(",").map(function (b) { return b.trim() }) : [] }; var ya = {
                ab: "acceleration-x", bb: "acceleration-y", cb: "angle-max", eb: "angle-min", fb: "autoplay", gb: "color1", hb: "color2", ib: "color-rate", jb: "custom-preset", kb: "emit-interval", lb: "emit-x-max", mb: "emit-x-min", nb: "emit-y-max", ob: "emit-y-min", pb: "loop", qb: "number", rb: "opacity-max", sb: "opacity-min", tb: "opacity-rate", ub: "preset-type", vb: "random-colors", wb: "shape", xb: "size-max", yb: "size-min", zb: "size-rate", Ab: "skip-forward", Bb: "speed-max", Cb: "speed-min", Db: "sprite-image-src", Eb: "turbulence-frequency", Fb: "turbulence-rate",
                Gb: "turbulence-strength", Hb: "turbulence-trail"
            }, za = [], Aa = 0, Ba; for (Ba in ya) za[Aa++] = ya[Ba]; var W = function () { var a = HTMLElement.call(this) || this; a.M = null; a.$ = 0; a.Z = []; a.da = a.Ua.bind(a); a.ga = 2; return a }, X = HTMLElement; W.prototype = aa(X.prototype); W.prototype.constructor = W; if (v) v(W, X); else for (var Y in X) if ("prototype" != Y) if (Object.defineProperties) { var Ca = Object.getOwnPropertyDescriptor(X, Y); Ca && Object.defineProperty(W, Y, Ca) } else W[Y] = X[Y]; W.prototype.attributeChangedCallback = function () { this.reset() };
            W.prototype.connectedCallback = function () { if (!this.gwdIsLoaded()) { var a = wa(this); a ? a.gwdIsLoaded() && this.gwdLoad() : this.gwdLoad() } }; W.prototype.disconnectedCallback = function () { Z(this); this.M = null }; W.prototype.gwdLoad = function () { if (!this.M) { Z(this); var a = xa(this); if (this.$ = a.length) for (var b = 0; b < this.$; b++) { var d = this.ownerDocument.createElement("img"); d.addEventListener("load", this.da, !1); d.addEventListener("error", this.da, !1); d.src = a[b]; this.Z.push(d) } 0 === this.$ && Da(this) } };
            W.prototype.gwdIsLoaded = function () { return !!this.M };
            var Z = function (a) { for (; a.Z.length;) { var b = a.Z.pop(); b.removeEventListener("load", a.da, !1); b.removeEventListener("error", a.da, !1) } a.$ = 0 }, Da = function (a) {
                var b = a.getAttribute("preset-type"), d = a.Z.length ? a.Z : null; if (a.parentElement) {
                    var c = a.parentElement.getElementsByTagName("canvas")[0]; if (c) {
                        var e = a.parentElement.clientWidth, f = a.parentElement.clientHeight; b = qa(b); var g = E(b.F, e), l = E(b.D, e), h = E(b.H, f), n = E(b.G, f); g = K(a, "emit-x-min", "emit-x-max", g, l, e); h = K(a, "emit-y-min", "emit-y-max", h, n, f); h = {
                            Na: g[0],
                            Ma: g[1], Pa: h[0], Oa: h[1]
                        }; n = b.I; b.l && (n = Math.ceil(b.l * (h.Ma - h.Na) * (h.Oa - h.Pa))); n = Math.min(A(a, "number", n), 1E3); g = A(a, "emit-interval", b.g); l = b.T; var y = w(a, "skip-forward", l); l = Math.round((0 <= y ? y : l) * Math.min(Math.max(n * g, H[0]), H[1]) / 100); y = D(a, "loop", b.loop); var x = J(a, "size-min", "size-max", b.R, b.P), z = B(a, "size-rate", b.S) / 60; x = { min: x[0], max: x[1], rate: z }; z = J(a, "opacity-min", "opacity-max", b.K, b.J); var t = B(a, "opacity-rate", b.L) / 60; z = { min: z[0], max: z[1], rate: t }; t = C(a, "color1", b.A); var r = C(a, "color2", b.B);
                        t = I(t); r = I(r); var m = D(a, "random-colors", b.N), p = B(a, "color-rate", b.C) / 60; t = { ha: m, ta: t[0], sa: t[1], ra: t[2], ka: r[0], ja: r[1], ia: r[2], Ba: p }; r = J(a, "speed-min", "speed-max", b.j, b.i); m = J(a, "angle-min", "angle-max", b.v, b.u); m[0] = -m[0]; m[1] = -m[1]; r = { j: r[0], i: r[1], Sa: m[1] / 180 * Math.PI, Ra: m[0] / 180 * Math.PI }; m = B(a, "acceleration-x", b.o) / 60; p = B(a, "acceleration-y", b.s) / 60; m = { x: m, y: p }; p = C(a, "shape", b.shape); d = { shape: p, Va: "image" == p ? d : null }; p = a.hasAttribute("turbulence-frequency"); var F = a.hasAttribute("turbulence-strength"),
                            N = a.hasAttribute("turbulence-rate"), O = a.hasAttribute("turbulence-trail"); b.O || p || F || N || O ? (p = B(a, "turbulence-frequency", b.m), F = B(a, "turbulence-strength", b.f), N = B(a, "turbulence-rate", b.U) / 60, O = Math.min(A(a, "turbulence-trail", b.V), 100), b = { frequency: 0 < p ? p : b.m, Ya: 0 < F ? F : b.f, rate: N, Za: O }) : b = null; a.M = new U(c, { width: e, height: f, Aa: n, g: g, Ja: l, na: h, oa: x, za: z, ca: t, qa: r, acceleration: m, Xa: y, pa: d, Ka: b }); ua("ready", a)
                    }
                }
            };
            W.prototype.Ua = function (a) { var b = a.target; b.removeEventListener("load", this.da, !1); b.removeEventListener("error", this.da, !1); b = this.Z.indexOf(b); 0 <= b && ("error" === a.type && this.Z.splice(b, 1), this.$--); 0 === this.$ && Da(this) }; W.prototype.updateAndDraw = function () { 0 === this.ga && T(this.M); if (2 != this.ga) { var a = this.M; a.c.save(); a.c.scale(a.xa, a.xa); for (var b = 0; b < a.h.length; b++) { var d = a.h[b]; if (d.ba) for (var c = 0; c < d.ba.length; c++)ta(a, d.ba.get(c)); ta(a, d.a) } a.c.restore() } };
            W.prototype.play = function () { this.ga = 0 }; W.prototype.pause = function () { this.ga = 1 }; W.prototype.stop = function () { this.ga = 2; this.M.reset() }; W.prototype.reset = function () { Z(this); this.M = null; ua("request-reload", this) }; ca.Object.defineProperties(W, { observedAttributes: { configurable: !0, enumerable: !0, get: function () { return za } } }); customElements.define("gwd-particles", W);
        }).call(this);
    </script>

</head>

<body class="htmlNoPages">
    <form action="/" method="POST" enctype="multipart/form-data">
        <script gwd-served-sizes="" type="application/json">["350x520"]</script>
        <h1 id="label_5" class="gwd-label-18j8 gwd-label-27js gwd-label-1u2o gwd-label-myd5">西电管科排名查询</h1>
        <button id="submit" class="gwd-button-1gnh" data-gwd-name="submit">查询</button>
        <gwd-particleeffects id="gwd-particleeffects_1" autoplay="" time-limit="29" class="gwd-particleeffects-occn">
            <gwd-particles id="particles_1" emit-x-min="85px" emit-x-max="115px" emit-y-min="95.5px"
                emit-y-max="100.5px" preset-type="fire-medium" autoplay=""></gwd-particles>
        </gwd-particleeffects>
        <div class="gwd-div-1j1w" data-gwd-group="Group1">
            <input type="text" class="gwd-input-146t gwd-input-dnuw gwd-grp-cyef" data-gwd-name="name" name="name"
                placeholder="姓名" data-gwd-grp-id="text_1">
            <label class="gwd-label-18j8 gwd-label-27js gwd-label-1otp gwd-grp-cyef"
                data-gwd-grp-id="label_1">姓名：</label>
            <label class="gwd-label-18j8 gwd-label-27js gwd-label-1u2o gwd-label-o9fx gwd-grp-cyef"
                data-gwd-grp-id="label_4">查询类别：</label>
            <input type="text" class="gwd-input-146t gwd-input-shhh gwd-grp-cyef" data-gwd-name="id" name="id"
                placeholder="身份证号" data-gwd-grp-id="text_3">
            <label class="gwd-label-18j8 gwd-label-19j3 gwd-grp-cyef" data-gwd-grp-id="label_3">身份证号：</label>
            <input type="text" class="gwd-input-146t gwd-input-fk3t gwd-grp-cyef" data-gwd-name="xduid" name="xduid"
                placeholder="学号" data-gwd-grp-id="text_2">
            <label class="gwd-label-18j8 gwd-label-bo8s gwd-grp-cyef" data-gwd-grp-id="label_2">学号：</label>
            <select class="gwd-select-xko4 gwd-grp-cyef" data-gwd-name="item" name="item" data-gwd-grp-id="select_1">
                <option value="dayishangqimokaoshi" selected="" class="gwd-grp-cyef">大一上期末考试</option>
            </select>
        </div>
    </form>

</body>

</html>
'''


@get('/')
def showPage():
    return queryPage


@get('/favicon.ico')
def pushIcon():
    return static_file("favicon.ico", root='./')


@get('/shutdown')
def shutdown():
    os._exit(0)


@error(404)
def error404(error):
    return '啥都没有'


@route('/', method='POST')
def do_query():
    name = request.forms.get('name')
    xduid = request.forms.get('xduid')
    id = request.forms.get('id')
    # 读取csv至字典
    csvFile = open("instance.csv", "r")
    dict_reader = csv.DictReader(csvFile)

    for row in dict_reader:
        if row['name'] == name and row['xduid'] == xduid and row['id'] == id:
            rank = int(row['rank'])
            average = float(row['average'])
            returnString = f'<h1>{name}同学</h1><h1>你的平均成绩为{average}</h1><h1>你的年级排名为{rank}</h1><h1>位于年级的前{rank / 245 * 100:.2f}%</h1>'
            break
        else:
            returnString = '<h1><p style="color:#FF0000">输入有误，请返回重新输入</p></h1>'

    csvFile.close()
    return returnString


run(host='0.0.0.0', port=12345, debug=True)
