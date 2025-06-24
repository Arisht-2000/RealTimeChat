import { useState as p, useRef as h, useEffect as R } from "react";
var x = { exports: {} }, c = {};
/**
 * @license React
 * react-jsx-runtime.production.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var g;
function b() {
  if (g) return c;
  g = 1;
  var d = Symbol.for("react.transitional.element"), a = Symbol.for("react.fragment");
  function n(l, r, e) {
    var u = null;
    if (e !== void 0 && (u = "" + e), r.key !== void 0 && (u = "" + r.key), "key" in r) {
      e = {};
      for (var i in r)
        i !== "key" && (e[i] = r[i]);
    } else e = r;
    return r = e.ref, {
      $$typeof: d,
      type: l,
      key: u,
      ref: r !== void 0 ? r : null,
      props: e
    };
  }
  return c.Fragment = a, c.jsx = n, c.jsxs = n, c;
}
var v;
function y() {
  return v || (v = 1, x.exports = b()), x.exports;
}
var o = y();
const S = () => {
  const [d, a] = p([
    { text: "Welcome to the chatroom!", user: "other" }
  ]), [n, l] = p(""), r = h(null), e = h(null), u = () => {
    const t = window.location.pathname.match(/\/chatroom\/([^/]+)\//), s = t ? t[1] : "default";
    return console.log("roomname:", s), s;
  }, i = window.username || "Anonymous";
  R(() => {
    const t = u();
    return e.current = new window.WebSocket("ws://" + window.location.host + "/ws/chat/" + t + "/"), e.current.onmessage = (s) => {
      try {
        const f = JSON.parse(s.data);
        a((m) => [...m, { text: f.message, user: f.user || "other" }]);
      } catch {
        a((m) => [...m, { text: s.data, user: "other" }]);
      }
    }, e.current.onclose = () => {
      a((s) => [
        ...s,
        { text: "Disconnected from chat. Redirecting to homepage in 5 seconds...", user: "system" }
      ]), setTimeout(() => {
        window.location.href = "/";
      }, 5e3);
    }, () => {
      e.current && e.current.close();
    };
  }, []), R(() => {
    r.current && r.current.scrollIntoView({ behavior: "smooth" });
  }, [d]);
  const w = (t) => {
    t.preventDefault(), n.trim() && e.current && e.current.readyState === 1 && (e.current.send(JSON.stringify({ message: n, user: i })), l(""));
  };
  return /* @__PURE__ */ o.jsxs("div", { style: { display: "flex", flexDirection: "column", height: "100%" }, children: [
    /* @__PURE__ */ o.jsxs("div", { className: "chat-messages", style: { flex: 1, overflowY: "auto", padding: 20, background: "#f7f9fa" }, children: [
      d.map((t, s) => /* @__PURE__ */ o.jsx(
        "div",
        {
          className: `message ${t.user}`,
          style: {
            alignSelf: t.user === "user" ? "flex-end" : "flex-start",
            background: t.user === "user" ? "#007bff" : "#e9ecef",
            color: t.user === "user" ? "#fff" : "#333",
            borderRadius: 18,
            padding: "12px 16px",
            marginBottom: 8,
            maxWidth: "70%",
            boxShadow: "0 2px 8px rgba(0,0,0,0.04)"
          },
          children: t.text
        },
        s
      )),
      /* @__PURE__ */ o.jsx("div", { ref: r })
    ] }),
    /* @__PURE__ */ o.jsxs("form", { className: "chat-input", onSubmit: w, style: { display: "flex", padding: 16, background: "#f1f3f6", borderTop: "1px solid #e0e0e0" }, children: [
      /* @__PURE__ */ o.jsx(
        "input",
        {
          type: "text",
          id: "chatInput",
          value: n,
          onChange: (t) => l(t.target.value),
          placeholder: "Type your message...",
          required: !0,
          style: { flex: 1, padding: "10px 14px", border: "1px solid #ccc", borderRadius: 20, fontSize: "1rem" }
        }
      ),
      /* @__PURE__ */ o.jsx("button", { type: "submit", style: { background: "#007bff", color: "#fff", border: "none", borderRadius: "50%", width: 40, height: 40, marginLeft: 10, fontSize: "1.2rem", cursor: "pointer" }, children: /* @__PURE__ */ o.jsx("i", { className: "fas fa-paper-plane" }) })
    ] })
  ] });
};
export {
  S as default
};
