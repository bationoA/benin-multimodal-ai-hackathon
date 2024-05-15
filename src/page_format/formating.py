import os
import pandas as pd
import streamlit as st

from src.utils import get_article_image_base64


def default_pages_config(_title=None, layout="wide"):
    st.set_page_config(page_title=_title,
                       page_icon=None,  # os.path.join("src", "images", "banner0.png"),
                       layout="wide" if layout == "wide" else "centered",
                       initial_sidebar_state="auto",
                       menu_items={"Get help": "mailto:amos.bationoo@gmail.com | maigaabdoulaziz000@gmail.com",
                                   "Report a Bug": "mailto:amos.bationoo@gmail.com | maigaabdoulaziz000@gmail.com",
                                   "About": None})

    boostrap_css = """
        <style>
            @charset "UTF-8";
            /*!
             * Bootstrap  v5.3.0-alpha2 (https://getbootstrap.com/)
             * Copyright 2011-2023 The Bootstrap Authors
             * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
             */
            :root,
            [data-bs-theme=light] {
              --bs-blue: #0d6efd;
              --bs-indigo: #6610f2;
              --bs-purple: #6f42c1;
              --bs-pink: #d63384;
              --bs-red: #dc3545;
              --bs-orange: #fd7e14;
              --bs-yellow: #ffc107;
              --bs-green: #198754;
              --bs-teal: #20c997;
              --bs-cyan: #0dcaf0;
              --bs-black: #000;
              --bs-white: #fff;
              --bs-gray: #6c757d;
              --bs-gray-dark: #343a40;
              --bs-gray-100: #f8f9fa;
              --bs-gray-200: #e9ecef;
              --bs-gray-300: #dee2e6;
              --bs-gray-400: #ced4da;
              --bs-gray-500: #adb5bd;
              --bs-gray-600: #6c757d;
              --bs-gray-700: #495057;
              --bs-gray-800: #343a40;
              --bs-gray-900: #212529;
              --bs-primary: #0d6efd;
              --bs-secondary: #6c757d;
              --bs-success: #198754;
              --bs-info: #0dcaf0;
              --bs-warning: #ffc107;
              --bs-danger: #dc3545;
              --bs-light: #f8f9fa;
              --bs-dark: #212529;
              --bs-primary-rgb: 13, 110, 253;
              --bs-secondary-rgb: 108, 117, 125;
              --bs-success-rgb: 25, 135, 84;
              --bs-info-rgb: 13, 202, 240;
              --bs-warning-rgb: 255, 193, 7;
              --bs-danger-rgb: 220, 53, 69;
              --bs-light-rgb: 248, 249, 250;
              --bs-dark-rgb: 33, 37, 41;
              --bs-primary-text-emphasis: #052c65;
              --bs-secondary-text-emphasis: #2b2f32;
              --bs-success-text-emphasis: #0a3622;
              --bs-info-text-emphasis: #055160;
              --bs-warning-text-emphasis: #664d03;
              --bs-danger-text-emphasis: #58151c;
              --bs-light-text-emphasis: #495057;
              --bs-dark-text-emphasis: #495057;
              --bs-primary-bg-subtle: #cfe2ff;
              --bs-secondary-bg-subtle: #e2e3e5;
              --bs-success-bg-subtle: #d1e7dd;
              --bs-info-bg-subtle: #cff4fc;
              --bs-warning-bg-subtle: #fff3cd;
              --bs-danger-bg-subtle: #f8d7da;
              --bs-light-bg-subtle: #fcfcfd;
              --bs-dark-bg-subtle: #ced4da;
              --bs-primary-border-subtle: #9ec5fe;
              --bs-secondary-border-subtle: #c4c8cb;
              --bs-success-border-subtle: #a3cfbb;
              --bs-info-border-subtle: #9eeaf9;
              --bs-warning-border-subtle: #ffe69c;
              --bs-danger-border-subtle: #f1aeb5;
              --bs-light-border-subtle: #e9ecef;
              --bs-dark-border-subtle: #adb5bd;
              --bs-white-rgb: 255, 255, 255;
              --bs-black-rgb: 0, 0, 0;
              --bs-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
              --bs-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
              --bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
              --bs-body-font-family: var(--bs-font-sans-serif);
              --bs-body-font-size: 1rem;
              --bs-body-font-weight: 400;
              --bs-body-line-height: 1.5;
              --bs-body-color: #212529;
              --bs-body-color-rgb: 33, 37, 41;
              --bs-body-bg: #fff;
              --bs-body-bg-rgb: 255, 255, 255;
              --bs-emphasis-color: #000;
              --bs-emphasis-color-rgb: 0, 0, 0;
              --bs-secondary-color: rgba(33, 37, 41, 0.75);
              --bs-secondary-color-rgb: 33, 37, 41;
              --bs-secondary-bg: #e9ecef;
              --bs-secondary-bg-rgb: 233, 236, 239;
              --bs-tertiary-color: rgba(33, 37, 41, 0.5);
              --bs-tertiary-color-rgb: 33, 37, 41;
              --bs-tertiary-bg: #f8f9fa;
              --bs-tertiary-bg-rgb: 248, 249, 250;
              --bs-link-color: #0d6efd;
              --bs-link-color-rgb: 13, 110, 253;
              --bs-link-decoration: underline;
              --bs-link-hover-color: #0a58ca;
              --bs-link-hover-color-rgb: 10, 88, 202;
              --bs-code-color: #d63384;
              --bs-highlight-bg: #fff3cd;
              --bs-border-width: 1px;
              --bs-border-style: solid;
              --bs-border-color: #dee2e6;
              --bs-border-color-translucent: rgba(0, 0, 0, 0.175);
              --bs-border-radius: 0.375rem;
              --bs-border-radius-sm: 0.25rem;
              --bs-border-radius-lg: 0.5rem;
              --bs-border-radius-xl: 1rem;
              --bs-border-radius-xxl: 2rem;
              --bs-border-radius-2xl: var(--bs-border-radius-xxl);
              --bs-border-radius-pill: 50rem;
              --bs-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
              --bs-box-shadow-sm: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
              --bs-box-shadow-lg: 0 1rem 3rem rgba(0, 0, 0, 0.175);
              --bs-box-shadow-inset: inset 0 1px 2px rgba(0, 0, 0, 0.075);
              --bs-focus-ring-width: 0.25rem;
              --bs-focus-ring-opacity: 0.25;
              --bs-focus-ring-color: rgba(13, 110, 253, 0.25);
              --bs-form-valid-color: #198754;
              --bs-form-valid-border-color: #198754;
              --bs-form-invalid-color: #dc3545;
              --bs-form-invalid-border-color: #dc3545;
            }

            [data-bs-theme=dark] {
              color-scheme: dark;
              --bs-body-color: #adb5bd;
              --bs-body-color-rgb: 173, 181, 189;
              --bs-body-bg: #212529;
              --bs-body-bg-rgb: 33, 37, 41;
              --bs-emphasis-color: #fff;
              --bs-emphasis-color-rgb: 255, 255, 255;
              --bs-secondary-color: rgba(173, 181, 189, 0.75);
              --bs-secondary-color-rgb: 173, 181, 189;
              --bs-secondary-bg: #343a40;
              --bs-secondary-bg-rgb: 52, 58, 64;
              --bs-tertiary-color: rgba(173, 181, 189, 0.5);
              --bs-tertiary-color-rgb: 173, 181, 189;
              --bs-tertiary-bg: #2b3035;
              --bs-tertiary-bg-rgb: 43, 48, 53;
              --bs-primary-text-emphasis: #6ea8fe;
              --bs-secondary-text-emphasis: #a7acb1;
              --bs-success-text-emphasis: #75b798;
              --bs-info-text-emphasis: #6edff6;
              --bs-warning-text-emphasis: #ffda6a;
              --bs-danger-text-emphasis: #ea868f;
              --bs-light-text-emphasis: #f8f9fa;
              --bs-dark-text-emphasis: #dee2e6;
              --bs-primary-bg-subtle: #031633;
              --bs-secondary-bg-subtle: #161719;
              --bs-success-bg-subtle: #051b11;
              --bs-info-bg-subtle: #032830;
              --bs-warning-bg-subtle: #332701;
              --bs-danger-bg-subtle: #2c0b0e;
              --bs-light-bg-subtle: #343a40;
              --bs-dark-bg-subtle: #1a1d20;
              --bs-primary-border-subtle: #084298;
              --bs-secondary-border-subtle: #41464b;
              --bs-success-border-subtle: #0f5132;
              --bs-info-border-subtle: #087990;
              --bs-warning-border-subtle: #997404;
              --bs-danger-border-subtle: #842029;
              --bs-light-border-subtle: #495057;
              --bs-dark-border-subtle: #343a40;
              --bs-link-color: #6ea8fe;
              --bs-link-hover-color: #8bb9fe;
              --bs-link-color-rgb: 110, 168, 254;
              --bs-link-hover-color-rgb: 139, 185, 254;
              --bs-code-color: #e685b5;
              --bs-border-color: #495057;
              --bs-border-color-translucent: rgba(255, 255, 255, 0.15);
              --bs-form-valid-color: #75b798;
              --bs-form-valid-border-color: #75b798;
              --bs-form-invalid-color: #ea868f;
              --bs-form-invalid-border-color: #ea868f;
            }

            *,
            *::before,
            *::after {
              box-sizing: border-box;
            }

            @media (prefers-reduced-motion: no-preference) {
              :root {
                scroll-behavior: smooth;
              }
            }

            body {
              margin: 0;
              font-family: var(--bs-body-font-family);
              font-size: var(--bs-body-font-size);
              font-weight: var(--bs-body-font-weight);
              line-height: var(--bs-body-line-height);
              color: var(--bs-body-color);
              text-align: var(--bs-body-text-align);
              background-color: var(--bs-body-bg);
              -webkit-text-size-adjust: 100%;
              -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            }

            hr {
              margin: 1rem 0;
              color: inherit;
              border: 0;
              border-top: var(--bs-border-width) solid;
              opacity: 0.25;
            }

            h6, .h6, h5, .h5, h4, .h4, h3, .h3, h2, .h2, h1, .h1 {
              margin-top: 0;
              margin-bottom: 0.5rem;
              font-weight: 500;
              line-height: 1.2;
              color: var(--bs-heading-color, inherit);
            }

            h1, .h1 {
              font-size: calc(1.375rem + 1.5vw);
            }
            @media (min-width: 1200px) {
              h1, .h1 {
                font-size: 2.5rem;
              }
            }

            h2, .h2 {
              font-size: calc(1.325rem + 0.9vw);
            }
            @media (min-width: 1200px) {
              h2, .h2 {
                font-size: 2rem;
              }
            }

            h3, .h3 {
              font-size: calc(1.3rem + 0.6vw);
            }
            @media (min-width: 1200px) {
              h3, .h3 {
                font-size: 1.75rem;
              }
            }

            h4, .h4 {
              font-size: calc(1.275rem + 0.3vw);
            }
            @media (min-width: 1200px) {
              h4, .h4 {
                font-size: 1.5rem;
              }
            }

            h5, .h5 {
              font-size: 1.25rem;
            }

            h6, .h6 {
              font-size: 1rem;
            }

            p {
              margin-top: 0;
              margin-bottom: 1rem;
            }

            abbr[title] {
              -webkit-text-decoration: underline dotted;
              text-decoration: underline dotted;
              cursor: help;
              -webkit-text-decoration-skip-ink: none;
              text-decoration-skip-ink: none;
            }

            address {
              margin-bottom: 1rem;
              font-style: normal;
              line-height: inherit;
            }

            ol,
            ul {
              padding-left: 2rem;
            }

            ol,
            ul,
            dl {
              margin-top: 0;
              margin-bottom: 1rem;
            }

            ol ol,
            ul ul,
            ol ul,
            ul ol {
              margin-bottom: 0;
            }

            dt {
              font-weight: 700;
            }

            dd {
              margin-bottom: 0.5rem;
              margin-left: 0;
            }

            blockquote {
              margin: 0 0 1rem;
            }

            b,
            strong {
              font-weight: bolder;
            }

            small, .small {
              font-size: 0.875em;
            }

            mark, .mark {
              padding: 0.1875em;
              background-color: var(--bs-highlight-bg);
            }

            sub,
            sup {
              position: relative;
              font-size: 0.75em;
              line-height: 0;
              vertical-align: baseline;
            }

            sub {
              bottom: -0.25em;
            }

            sup {
              top: -0.5em;
            }

            a {
              color: rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 1));
              text-decoration: underline;
            }
            a:hover {
              --bs-link-color-rgb: var(--bs-link-hover-color-rgb);
            }

            a:not([href]):not([class]), a:not([href]):not([class]):hover {
              color: inherit;
              text-decoration: none;
            }

            pre,
            code,
            kbd,
            samp {
              font-family: var(--bs-font-monospace);
              font-size: 1em;
            }

            pre {
              display: block;
              margin-top: 0;
              margin-bottom: 1rem;
              overflow: auto;
              font-size: 0.875em;
            }
            pre code {
              font-size: inherit;
              color: inherit;
              word-break: normal;
            }

            code {
              font-size: 0.875em;
              color: var(--bs-code-color);
              word-wrap: break-word;
            }
            a > code {
              color: inherit;
            }

            kbd {
              padding: 0.1875rem 0.375rem;
              font-size: 0.875em;
              color: var(--bs-body-bg);
              background-color: var(--bs-body-color);
              border-radius: 0.25rem;
            }
            kbd kbd {
              padding: 0;
              font-size: 1em;
            }

            figure {
              margin: 0 0 1rem;
            }

            img,
            svg {
              vertical-align: middle;
            }

            table {
              caption-side: bottom;
              border-collapse: collapse;
            }

            caption {
              padding-top: 0.5rem;
              padding-bottom: 0.5rem;
              color: var(--bs-secondary-color);
              text-align: left;
            }

            th {
              text-align: inherit;
              text-align: -webkit-match-parent;
            }

            thead,
            tbody,
            tfoot,
            tr,
            td,
            th {
              border-color: inherit;
              border-style: solid;
              border-width: 0;
            }

            label {
              display: inline-block;
            }

            button {
              border-radius: 0;
            }

            button:focus:not(:focus-visible) {
              outline: 0;
            }

            input,
            button,
            select,
            optgroup,
            textarea {
              margin: 0;
              font-family: inherit;
              font-size: inherit;
              line-height: inherit;
            }

            button,
            select {
              text-transform: none;
            }

            [role=button] {
              cursor: pointer;
            }

            select {
              word-wrap: normal;
            }
            select:disabled {
              opacity: 1;
            }

            [list]:not([type=date]):not([type=datetime-local]):not([type=month]):not([type=week]):not([type=time])::-webkit-calendar-picker-indicator {
              display: none !important;
            }

            button,
            [type=button],
            [type=reset],
            [type=submit] {
              -webkit-appearance: button;
            }
            button:not(:disabled),
            [type=button]:not(:disabled),
            [type=reset]:not(:disabled),
            [type=submit]:not(:disabled) {
              cursor: pointer;
            }

            ::-moz-focus-inner {
              padding: 0;
              border-style: none;
            }

            textarea {
              resize: vertical;
            }

            fieldset {
              min-width: 0;
              padding: 0;
              margin: 0;
              border: 0;
            }

            legend {
              float: left;
              width: 100%;
              padding: 0;
              margin-bottom: 0.5rem;
              font-size: calc(1.275rem + 0.3vw);
              line-height: inherit;
            }
            @media (min-width: 1200px) {
              legend {
                font-size: 1.5rem;
              }
            }
            legend + * {
              clear: left;
            }

            ::-webkit-datetime-edit-fields-wrapper,
            ::-webkit-datetime-edit-text,
            ::-webkit-datetime-edit-minute,
            ::-webkit-datetime-edit-hour-field,
            ::-webkit-datetime-edit-day-field,
            ::-webkit-datetime-edit-month-field,
            ::-webkit-datetime-edit-year-field {
              padding: 0;
            }

            ::-webkit-inner-spin-button {
              height: auto;
            }

            [type=search] {
              outline-offset: -2px;
              -webkit-appearance: textfield;
            }

            /* rtl:raw:
            [type="tel"],
            [type="url"],
            [type="email"],
            [type="number"] {
              direction: ltr;
            }
            */
            ::-webkit-search-decoration {
              -webkit-appearance: none;
            }

            ::-webkit-color-swatch-wrapper {
              padding: 0;
            }

            ::-webkit-file-upload-button {
              font: inherit;
              -webkit-appearance: button;
            }

            ::file-selector-button {
              font: inherit;
              -webkit-appearance: button;
            }

            output {
              display: inline-block;
            }

            iframe {
              border: 0;
            }

            summary {
              display: list-item;
              cursor: pointer;
            }

            progress {
              vertical-align: baseline;
            }

            [hidden] {
              display: none !important;
            }

            .lead {
              font-size: 1.25rem;
              font-weight: 300;
            }

            .display-1 {
              font-size: calc(1.625rem + 4.5vw);
              font-weight: 300;
              line-height: 1.2;
            }
            @media (min-width: 1200px) {
              .display-1 {
                font-size: 5rem;
              }
            }

            .display-2 {
              font-size: calc(1.575rem + 3.9vw);
              font-weight: 300;
              line-height: 1.2;
            }
            @media (min-width: 1200px) {
              .display-2 {
                font-size: 4.5rem;
              }
            }

            .display-3 {
              font-size: calc(1.525rem + 3.3vw);
              font-weight: 300;
              line-height: 1.2;
            }
            @media (min-width: 1200px) {
              .display-3 {
                font-size: 4rem;
              }
            }

            .display-4 {
              font-size: calc(1.475rem + 2.7vw);
              font-weight: 300;
              line-height: 1.2;
            }
            @media (min-width: 1200px) {
              .display-4 {
                font-size: 3.5rem;
              }
            }

            .display-5 {
              font-size: calc(1.425rem + 2.1vw);
              font-weight: 300;
              line-height: 1.2;
            }
            @media (min-width: 1200px) {
              .display-5 {
                font-size: 3rem;
              }
            }

            .display-6 {
              font-size: calc(1.375rem + 1.5vw);
              font-weight: 300;
              line-height: 1.2;
            }
            @media (min-width: 1200px) {
              .display-6 {
                font-size: 2.5rem;
              }
            }

            .list-unstyled {
              padding-left: 0;
              list-style: none;
            }

            .list-inline {
              padding-left: 0;
              list-style: none;
            }

            .list-inline-item {
              display: inline-block;
            }
            .list-inline-item:not(:last-child) {
              margin-right: 0.5rem;
            }

            .initialism {
              font-size: 0.875em;
              text-transform: uppercase;
            }

            .blockquote {
              margin-bottom: 1rem;
              font-size: 1.25rem;
            }
            .blockquote > :last-child {
              margin-bottom: 0;
            }

            .blockquote-footer {
              margin-top: -1rem;
              margin-bottom: 1rem;
              font-size: 0.875em;
              color: #6c757d;
            }
            .blockquote-footer::before {
              content: "— ";
            }

            .img-fluid {
              max-width: 100%;
              height: auto;
            }

            .img-thumbnail {
              padding: 0.25rem;
              background-color: var(--bs-body-bg);
              border: var(--bs-border-width) solid var(--bs-border-color);
              border-radius: var(--bs-border-radius);
              max-width: 100%;
              height: auto;
            }

            .figure {
              display: inline-block;
            }

            .figure-img {
              margin-bottom: 0.5rem;
              line-height: 1;
            }

            .figure-caption {
              font-size: 0.875em;
              color: var(--bs-secondary-color);
            }

            .container,
            .container-fluid,
            .container-xxl,
            .container-xl,
            .container-lg,
            .container-md,
            .container-sm {
              --bs-gutter-x: 1.5rem;
              --bs-gutter-y: 0;
              width: 100%;
              padding-right: calc(var(--bs-gutter-x) * 0.5);
              padding-left: calc(var(--bs-gutter-x) * 0.5);
              margin-right: auto;
              margin-left: auto;
            }

            @media (min-width: 576px) {
              .container-sm, .container {
                max-width: 540px;
              }
            }
            @media (min-width: 768px) {
              .container-md, .container-sm, .container {
                max-width: 720px;
              }
            }
            @media (min-width: 992px) {
              .container-lg, .container-md, .container-sm, .container {
                max-width: 960px;
              }
            }
            @media (min-width: 1200px) {
              .container-xl, .container-lg, .container-md, .container-sm, .container {
                max-width: 1140px;
              }
            }
            @media (min-width: 1400px) {
              .container-xxl, .container-xl, .container-lg, .container-md, .container-sm, .container {
                max-width: 1320px;
              }
            }
            :root {
              --bs-breakpoint-xs: 0;
              --bs-breakpoint-sm: 576px;
              --bs-breakpoint-md: 768px;
              --bs-breakpoint-lg: 992px;
              --bs-breakpoint-xl: 1200px;
              --bs-breakpoint-xxl: 1400px;
            }

            .row {
              --bs-gutter-x: 1.5rem;
              --bs-gutter-y: 0;
              display: flex;
              flex-wrap: wrap;
              margin-top: calc(-1 * var(--bs-gutter-y));
              margin-right: calc(-0.5 * var(--bs-gutter-x));
              margin-left: calc(-0.5 * var(--bs-gutter-x));
            }
            .row > * {
              flex-shrink: 0;
              width: 100%;
              max-width: 100%;
              padding-right: calc(var(--bs-gutter-x) * 0.5);
              padding-left: calc(var(--bs-gutter-x) * 0.5);
              margin-top: var(--bs-gutter-y);
            }

            .col {
              flex: 1 0 0%;
            }

            .row-cols-auto > * {
              flex: 0 0 auto;
              width: auto;
            }

            .row-cols-1 > * {
              flex: 0 0 auto;
              width: 100%;
            }

            .row-cols-2 > * {
              flex: 0 0 auto;
              width: 50%;
            }

            .row-cols-3 > * {
              flex: 0 0 auto;
              width: 33.3333333333%;
            }

            .row-cols-4 > * {
              flex: 0 0 auto;
              width: 25%;
            }

            .row-cols-5 > * {
              flex: 0 0 auto;
              width: 20%;
            }

            .row-cols-6 > * {
              flex: 0 0 auto;
              width: 16.6666666667%;
            }

            .col-auto {
              flex: 0 0 auto;
              width: auto;
            }

            .col-1 {
              flex: 0 0 auto;
              width: 8.33333333%;
            }

            .col-2 {
              flex: 0 0 auto;
              width: 16.66666667%;
            }

            .col-3 {
              flex: 0 0 auto;
              width: 25%;
            }

            .col-4 {
              flex: 0 0 auto;
              width: 33.33333333%;
            }

            .col-5 {
              flex: 0 0 auto;
              width: 41.66666667%;
            }

            .col-6 {
              flex: 0 0 auto;
              width: 50%;
            }

            .col-7 {
              flex: 0 0 auto;
              width: 58.33333333%;
            }

            .col-8 {
              flex: 0 0 auto;
              width: 66.66666667%;
            }

            .col-9 {
              flex: 0 0 auto;
              width: 75%;
            }

            .col-10 {
              flex: 0 0 auto;
              width: 83.33333333%;
            }

            .col-11 {
              flex: 0 0 auto;
              width: 91.66666667%;
            }

            .col-12 {
              flex: 0 0 auto;
              width: 100%;
            }

            .offset-1 {
              margin-left: 8.33333333%;
            }

            .offset-2 {
              margin-left: 16.66666667%;
            }

            .offset-3 {
              margin-left: 25%;
            }

            .offset-4 {
              margin-left: 33.33333333%;
            }

            .offset-5 {
              margin-left: 41.66666667%;
            }

            .offset-6 {
              margin-left: 50%;
            }

            .offset-7 {
              margin-left: 58.33333333%;
            }

            .offset-8 {
              margin-left: 66.66666667%;
            }

            .offset-9 {
              margin-left: 75%;
            }

            .offset-10 {
              margin-left: 83.33333333%;
            }

            .offset-11 {
              margin-left: 91.66666667%;
            }

            .g-0,
            .gx-0 {
              --bs-gutter-x: 0;
            }

            .g-0,
            .gy-0 {
              --bs-gutter-y: 0;
            }

            .g-1,
            .gx-1 {
              --bs-gutter-x: 0.25rem;
            }

            .g-1,
            .gy-1 {
              --bs-gutter-y: 0.25rem;
            }

            .g-2,
            .gx-2 {
              --bs-gutter-x: 0.5rem;
            }

            .g-2,
            .gy-2 {
              --bs-gutter-y: 0.5rem;
            }

            .g-3,
            .gx-3 {
              --bs-gutter-x: 1rem;
            }

            .g-3,
            .gy-3 {
              --bs-gutter-y: 1rem;
            }

            .g-4,
            .gx-4 {
              --bs-gutter-x: 1.5rem;
            }

            .g-4,
            .gy-4 {
              --bs-gutter-y: 1.5rem;
            }

            .g-5,
            .gx-5 {
              --bs-gutter-x: 3rem;
            }

            .g-5,
            .gy-5 {
              --bs-gutter-y: 3rem;
            }

            @media (min-width: 576px) {
              .col-sm {
                flex: 1 0 0%;
              }
              .row-cols-sm-auto > * {
                flex: 0 0 auto;
                width: auto;
              }
              .row-cols-sm-1 > * {
                flex: 0 0 auto;
                width: 100%;
              }
              .row-cols-sm-2 > * {
                flex: 0 0 auto;
                width: 50%;
              }
              .row-cols-sm-3 > * {
                flex: 0 0 auto;
                width: 33.3333333333%;
              }
              .row-cols-sm-4 > * {
                flex: 0 0 auto;
                width: 25%;
              }
              .row-cols-sm-5 > * {
                flex: 0 0 auto;
                width: 20%;
              }
              .row-cols-sm-6 > * {
                flex: 0 0 auto;
                width: 16.6666666667%;
              }
              .col-sm-auto {
                flex: 0 0 auto;
                width: auto;
              }
              .col-sm-1 {
                flex: 0 0 auto;
                width: 8.33333333%;
              }
              .col-sm-2 {
                flex: 0 0 auto;
                width: 16.66666667%;
              }
              .col-sm-3 {
                flex: 0 0 auto;
                width: 25%;
              }
              .col-sm-4 {
                flex: 0 0 auto;
                width: 33.33333333%;
              }
              .col-sm-5 {
                flex: 0 0 auto;
                width: 41.66666667%;
              }
              .col-sm-6 {
                flex: 0 0 auto;
                width: 50%;
              }
              .col-sm-7 {
                flex: 0 0 auto;
                width: 58.33333333%;
              }
              .col-sm-8 {
                flex: 0 0 auto;
                width: 66.66666667%;
              }
              .col-sm-9 {
                flex: 0 0 auto;
                width: 75%;
              }
              .col-sm-10 {
                flex: 0 0 auto;
                width: 83.33333333%;
              }
              .col-sm-11 {
                flex: 0 0 auto;
                width: 91.66666667%;
              }
              .col-sm-12 {
                flex: 0 0 auto;
                width: 100%;
              }
              .offset-sm-0 {
                margin-left: 0;
              }
              .offset-sm-1 {
                margin-left: 8.33333333%;
              }
              .offset-sm-2 {
                margin-left: 16.66666667%;
              }
              .offset-sm-3 {
                margin-left: 25%;
              }
              .offset-sm-4 {
                margin-left: 33.33333333%;
              }
              .offset-sm-5 {
                margin-left: 41.66666667%;
              }
              .offset-sm-6 {
                margin-left: 50%;
              }
              .offset-sm-7 {
                margin-left: 58.33333333%;
              }
              .offset-sm-8 {
                margin-left: 66.66666667%;
              }
              .offset-sm-9 {
                margin-left: 75%;
              }
              .offset-sm-10 {
                margin-left: 83.33333333%;
              }
              .offset-sm-11 {
                margin-left: 91.66666667%;
              }
              .g-sm-0,
              .gx-sm-0 {
                --bs-gutter-x: 0;
              }
              .g-sm-0,
              .gy-sm-0 {
                --bs-gutter-y: 0;
              }
              .g-sm-1,
              .gx-sm-1 {
                --bs-gutter-x: 0.25rem;
              }
              .g-sm-1,
              .gy-sm-1 {
                --bs-gutter-y: 0.25rem;
              }
              .g-sm-2,
              .gx-sm-2 {
                --bs-gutter-x: 0.5rem;
              }
              .g-sm-2,
              .gy-sm-2 {
                --bs-gutter-y: 0.5rem;
              }
              .g-sm-3,
              .gx-sm-3 {
                --bs-gutter-x: 1rem;
              }
              .g-sm-3,
              .gy-sm-3 {
                --bs-gutter-y: 1rem;
              }
              .g-sm-4,
              .gx-sm-4 {
                --bs-gutter-x: 1.5rem;
              }
              .g-sm-4,
              .gy-sm-4 {
                --bs-gutter-y: 1.5rem;
              }
              .g-sm-5,
              .gx-sm-5 {
                --bs-gutter-x: 3rem;
              }
              .g-sm-5,
              .gy-sm-5 {
                --bs-gutter-y: 3rem;
              }
            }
            @media (min-width: 768px) {
              .col-md {
                flex: 1 0 0%;
              }
              .row-cols-md-auto > * {
                flex: 0 0 auto;
                width: auto;
              }
              .row-cols-md-1 > * {
                flex: 0 0 auto;
                width: 100%;
              }
              .row-cols-md-2 > * {
                flex: 0 0 auto;
                width: 50%;
              }
              .row-cols-md-3 > * {
                flex: 0 0 auto;
                width: 33.3333333333%;
              }
              .row-cols-md-4 > * {
                flex: 0 0 auto;
                width: 25%;
              }
              .row-cols-md-5 > * {
                flex: 0 0 auto;
                width: 20%;
              }
              .row-cols-md-6 > * {
                flex: 0 0 auto;
                width: 16.6666666667%;
              }
              .col-md-auto {
                flex: 0 0 auto;
                width: auto;
              }
              .col-md-1 {
                flex: 0 0 auto;
                width: 8.33333333%;
              }
              .col-md-2 {
                flex: 0 0 auto;
                width: 16.66666667%;
              }
              .col-md-3 {
                flex: 0 0 auto;
                width: 25%;
              }
              .col-md-4 {
                flex: 0 0 auto;
                width: 33.33333333%;
              }
              .col-md-5 {
                flex: 0 0 auto;
                width: 41.66666667%;
              }
              .col-md-6 {
                flex: 0 0 auto;
                width: 50%;
              }
              .col-md-7 {
                flex: 0 0 auto;
                width: 58.33333333%;
              }
              .col-md-8 {
                flex: 0 0 auto;
                width: 66.66666667%;
              }
              .col-md-9 {
                flex: 0 0 auto;
                width: 75%;
              }
              .col-md-10 {
                flex: 0 0 auto;
                width: 83.33333333%;
              }
              .col-md-11 {
                flex: 0 0 auto;
                width: 91.66666667%;
              }
              .col-md-12 {
                flex: 0 0 auto;
                width: 100%;
              }
              .offset-md-0 {
                margin-left: 0;
              }
              .offset-md-1 {
                margin-left: 8.33333333%;
              }
              .offset-md-2 {
                margin-left: 16.66666667%;
              }
              .offset-md-3 {
                margin-left: 25%;
              }
              .offset-md-4 {
                margin-left: 33.33333333%;
              }
              .offset-md-5 {
                margin-left: 41.66666667%;
              }
              .offset-md-6 {
                margin-left: 50%;
              }
              .offset-md-7 {
                margin-left: 58.33333333%;
              }
              .offset-md-8 {
                margin-left: 66.66666667%;
              }
              .offset-md-9 {
                margin-left: 75%;
              }
              .offset-md-10 {
                margin-left: 83.33333333%;
              }
              .offset-md-11 {
                margin-left: 91.66666667%;
              }
              .g-md-0,
              .gx-md-0 {
                --bs-gutter-x: 0;
              }
              .g-md-0,
              .gy-md-0 {
                --bs-gutter-y: 0;
              }
              .g-md-1,
              .gx-md-1 {
                --bs-gutter-x: 0.25rem;
              }
              .g-md-1,
              .gy-md-1 {
                --bs-gutter-y: 0.25rem;
              }
              .g-md-2,
              .gx-md-2 {
                --bs-gutter-x: 0.5rem;
              }
              .g-md-2,
              .gy-md-2 {
                --bs-gutter-y: 0.5rem;
              }
              .g-md-3,
              .gx-md-3 {
                --bs-gutter-x: 1rem;
              }
              .g-md-3,
              .gy-md-3 {
                --bs-gutter-y: 1rem;
              }
              .g-md-4,
              .gx-md-4 {
                --bs-gutter-x: 1.5rem;
              }
              .g-md-4,
              .gy-md-4 {
                --bs-gutter-y: 1.5rem;
              }
              .g-md-5,
              .gx-md-5 {
                --bs-gutter-x: 3rem;
              }
              .g-md-5,
              .gy-md-5 {
                --bs-gutter-y: 3rem;
              }
            }
            @media (min-width: 992px) {
              .col-lg {
                flex: 1 0 0%;
              }
              .row-cols-lg-auto > * {
                flex: 0 0 auto;
                width: auto;
              }
              .row-cols-lg-1 > * {
                flex: 0 0 auto;
                width: 100%;
              }
              .row-cols-lg-2 > * {
                flex: 0 0 auto;
                width: 50%;
              }
              .row-cols-lg-3 > * {
                flex: 0 0 auto;
                width: 33.3333333333%;
              }
              .row-cols-lg-4 > * {
                flex: 0 0 auto;
                width: 25%;
              }
              .row-cols-lg-5 > * {
                flex: 0 0 auto;
                width: 20%;
              }
              .row-cols-lg-6 > * {
                flex: 0 0 auto;
                width: 16.6666666667%;
              }
              .col-lg-auto {
                flex: 0 0 auto;
                width: auto;
              }
              .col-lg-1 {
                flex: 0 0 auto;
                width: 8.33333333%;
              }
              .col-lg-2 {
                flex: 0 0 auto;
                width: 16.66666667%;
              }
              .col-lg-3 {
                flex: 0 0 auto;
                width: 25%;
              }
              .col-lg-4 {
                flex: 0 0 auto;
                width: 33.33333333%;
              }
              .col-lg-5 {
                flex: 0 0 auto;
                width: 41.66666667%;
              }
              .col-lg-6 {
                flex: 0 0 auto;
                width: 50%;
              }
              .col-lg-7 {
                flex: 0 0 auto;
                width: 58.33333333%;
              }
              .col-lg-8 {
                flex: 0 0 auto;
                width: 66.66666667%;
              }
              .col-lg-9 {
                flex: 0 0 auto;
                width: 75%;
              }
              .col-lg-10 {
                flex: 0 0 auto;
                width: 83.33333333%;
              }
              .col-lg-11 {
                flex: 0 0 auto;
                width: 91.66666667%;
              }
              .col-lg-12 {
                flex: 0 0 auto;
                width: 100%;
              }
              .offset-lg-0 {
                margin-left: 0;
              }
              .offset-lg-1 {
                margin-left: 8.33333333%;
              }
              .offset-lg-2 {
                margin-left: 16.66666667%;
              }
              .offset-lg-3 {
                margin-left: 25%;
              }
              .offset-lg-4 {
                margin-left: 33.33333333%;
              }
              .offset-lg-5 {
                margin-left: 41.66666667%;
              }
              .offset-lg-6 {
                margin-left: 50%;
              }
              .offset-lg-7 {
                margin-left: 58.33333333%;
              }
              .offset-lg-8 {
                margin-left: 66.66666667%;
              }
              .offset-lg-9 {
                margin-left: 75%;
              }
              .offset-lg-10 {
                margin-left: 83.33333333%;
              }
              .offset-lg-11 {
                margin-left: 91.66666667%;
              }
              .g-lg-0,
              .gx-lg-0 {
                --bs-gutter-x: 0;
              }
              .g-lg-0,
              .gy-lg-0 {
                --bs-gutter-y: 0;
              }
              .g-lg-1,
              .gx-lg-1 {
                --bs-gutter-x: 0.25rem;
              }
              .g-lg-1,
              .gy-lg-1 {
                --bs-gutter-y: 0.25rem;
              }
              .g-lg-2,
              .gx-lg-2 {
                --bs-gutter-x: 0.5rem;
              }
              .g-lg-2,
              .gy-lg-2 {
                --bs-gutter-y: 0.5rem;
              }
              .g-lg-3,
              .gx-lg-3 {
                --bs-gutter-x: 1rem;
              }
              .g-lg-3,
              .gy-lg-3 {
                --bs-gutter-y: 1rem;
              }
              .g-lg-4,
              .gx-lg-4 {
                --bs-gutter-x: 1.5rem;
              }
              .g-lg-4,
              .gy-lg-4 {
                --bs-gutter-y: 1.5rem;
              }
              .g-lg-5,
              .gx-lg-5 {
                --bs-gutter-x: 3rem;
              }
              .g-lg-5,
              .gy-lg-5 {
                --bs-gutter-y: 3rem;
              }
            }
            @media (min-width: 1200px) {
              .col-xl {
                flex: 1 0 0%;
              }
              .row-cols-xl-auto > * {
                flex: 0 0 auto;
                width: auto;
              }
              .row-cols-xl-1 > * {
                flex: 0 0 auto;
                width: 100%;
              }
              .row-cols-xl-2 > * {
                flex: 0 0 auto;
                width: 50%;
              }
              .row-cols-xl-3 > * {
                flex: 0 0 auto;
                width: 33.3333333333%;
              }
              .row-cols-xl-4 > * {
                flex: 0 0 auto;
                width: 25%;
              }
              .row-cols-xl-5 > * {
                flex: 0 0 auto;
                width: 20%;
              }
              .row-cols-xl-6 > * {
                flex: 0 0 auto;
                width: 16.6666666667%;
              }
              .col-xl-auto {
                flex: 0 0 auto;
                width: auto;
              }
              .col-xl-1 {
                flex: 0 0 auto;
                width: 8.33333333%;
              }
              .col-xl-2 {
                flex: 0 0 auto;
                width: 16.66666667%;
              }
              .col-xl-3 {
                flex: 0 0 auto;
                width: 25%;
              }
              .col-xl-4 {
                flex: 0 0 auto;
                width: 33.33333333%;
              }
              .col-xl-5 {
                flex: 0 0 auto;
                width: 41.66666667%;
              }
              .col-xl-6 {
                flex: 0 0 auto;
                width: 50%;
              }
              .col-xl-7 {
                flex: 0 0 auto;
                width: 58.33333333%;
              }
              .col-xl-8 {
                flex: 0 0 auto;
                width: 66.66666667%;
              }
              .col-xl-9 {
                flex: 0 0 auto;
                width: 75%;
              }
              .col-xl-10 {
                flex: 0 0 auto;
                width: 83.33333333%;
              }
              .col-xl-11 {
                flex: 0 0 auto;
                width: 91.66666667%;
              }
              .col-xl-12 {
                flex: 0 0 auto;
                width: 100%;
              }
              .offset-xl-0 {
                margin-left: 0;
              }
              .offset-xl-1 {
                margin-left: 8.33333333%;
              }
              .offset-xl-2 {
                margin-left: 16.66666667%;
              }
              .offset-xl-3 {
                margin-left: 25%;
              }
              .offset-xl-4 {
                margin-left: 33.33333333%;
              }
              .offset-xl-5 {
                margin-left: 41.66666667%;
              }
              .offset-xl-6 {
                margin-left: 50%;
              }
              .offset-xl-7 {
                margin-left: 58.33333333%;
              }
              .offset-xl-8 {
                margin-left: 66.66666667%;
              }
              .offset-xl-9 {
                margin-left: 75%;
              }
              .offset-xl-10 {
                margin-left: 83.33333333%;
              }
              .offset-xl-11 {
                margin-left: 91.66666667%;
              }
              .g-xl-0,
              .gx-xl-0 {
                --bs-gutter-x: 0;
              }
              .g-xl-0,
              .gy-xl-0 {
                --bs-gutter-y: 0;
              }
              .g-xl-1,
              .gx-xl-1 {
                --bs-gutter-x: 0.25rem;
              }
              .g-xl-1,
              .gy-xl-1 {
                --bs-gutter-y: 0.25rem;
              }
              .g-xl-2,
              .gx-xl-2 {
                --bs-gutter-x: 0.5rem;
              }
              .g-xl-2,
              .gy-xl-2 {
                --bs-gutter-y: 0.5rem;
              }
              .g-xl-3,
              .gx-xl-3 {
                --bs-gutter-x: 1rem;
              }
              .g-xl-3,
              .gy-xl-3 {
                --bs-gutter-y: 1rem;
              }
              .g-xl-4,
              .gx-xl-4 {
                --bs-gutter-x: 1.5rem;
              }
              .g-xl-4,
              .gy-xl-4 {
                --bs-gutter-y: 1.5rem;
              }
              .g-xl-5,
              .gx-xl-5 {
                --bs-gutter-x: 3rem;
              }
              .g-xl-5,
              .gy-xl-5 {
                --bs-gutter-y: 3rem;
              }
            }
            @media (min-width: 1400px) {
              .col-xxl {
                flex: 1 0 0%;
              }
              .row-cols-xxl-auto > * {
                flex: 0 0 auto;
                width: auto;
              }
              .row-cols-xxl-1 > * {
                flex: 0 0 auto;
                width: 100%;
              }
              .row-cols-xxl-2 > * {
                flex: 0 0 auto;
                width: 50%;
              }
              .row-cols-xxl-3 > * {
                flex: 0 0 auto;
                width: 33.3333333333%;
              }
              .row-cols-xxl-4 > * {
                flex: 0 0 auto;
                width: 25%;
              }
              .row-cols-xxl-5 > * {
                flex: 0 0 auto;
                width: 20%;
              }
              .row-cols-xxl-6 > * {
                flex: 0 0 auto;
                width: 16.6666666667%;
              }
              .col-xxl-auto {
                flex: 0 0 auto;
                width: auto;
              }
              .col-xxl-1 {
                flex: 0 0 auto;
                width: 8.33333333%;
              }
              .col-xxl-2 {
                flex: 0 0 auto;
                width: 16.66666667%;
              }
              .col-xxl-3 {
                flex: 0 0 auto;
                width: 25%;
              }
              .col-xxl-4 {
                flex: 0 0 auto;
                width: 33.33333333%;
              }
              .col-xxl-5 {
                flex: 0 0 auto;
                width: 41.66666667%;
              }
              .col-xxl-6 {
                flex: 0 0 auto;
                width: 50%;
              }
              .col-xxl-7 {
                flex: 0 0 auto;
                width: 58.33333333%;
              }
              .col-xxl-8 {
                flex: 0 0 auto;
                width: 66.66666667%;
              }
              .col-xxl-9 {
                flex: 0 0 auto;
                width: 75%;
              }
              .col-xxl-10 {
                flex: 0 0 auto;
                width: 83.33333333%;
              }
              .col-xxl-11 {
                flex: 0 0 auto;
                width: 91.66666667%;
              }
              .col-xxl-12 {
                flex: 0 0 auto;
                width: 100%;
              }
              .offset-xxl-0 {
                margin-left: 0;
              }
              .offset-xxl-1 {
                margin-left: 8.33333333%;
              }
              .offset-xxl-2 {
                margin-left: 16.66666667%;
              }
              .offset-xxl-3 {
                margin-left: 25%;
              }
              .offset-xxl-4 {
                margin-left: 33.33333333%;
              }
              .offset-xxl-5 {
                margin-left: 41.66666667%;
              }
              .offset-xxl-6 {
                margin-left: 50%;
              }
              .offset-xxl-7 {
                margin-left: 58.33333333%;
              }
              .offset-xxl-8 {
                margin-left: 66.66666667%;
              }
              .offset-xxl-9 {
                margin-left: 75%;
              }
              .offset-xxl-10 {
                margin-left: 83.33333333%;
              }
              .offset-xxl-11 {
                margin-left: 91.66666667%;
              }
              .g-xxl-0,
              .gx-xxl-0 {
                --bs-gutter-x: 0;
              }
              .g-xxl-0,
              .gy-xxl-0 {
                --bs-gutter-y: 0;
              }
              .g-xxl-1,
              .gx-xxl-1 {
                --bs-gutter-x: 0.25rem;
              }
              .g-xxl-1,
              .gy-xxl-1 {
                --bs-gutter-y: 0.25rem;
              }
              .g-xxl-2,
              .gx-xxl-2 {
                --bs-gutter-x: 0.5rem;
              }
              .g-xxl-2,
              .gy-xxl-2 {
                --bs-gutter-y: 0.5rem;
              }
              .g-xxl-3,
              .gx-xxl-3 {
                --bs-gutter-x: 1rem;
              }
              .g-xxl-3,
              .gy-xxl-3 {
                --bs-gutter-y: 1rem;
              }
              .g-xxl-4,
              .gx-xxl-4 {
                --bs-gutter-x: 1.5rem;
              }
              .g-xxl-4,
              .gy-xxl-4 {
                --bs-gutter-y: 1.5rem;
              }
              .g-xxl-5,
              .gx-xxl-5 {
                --bs-gutter-x: 3rem;
              }
              .g-xxl-5,
              .gy-xxl-5 {
                --bs-gutter-y: 3rem;
              }
            }
            .table {
              --bs-table-color: var(--bs-body-color);
              --bs-table-bg: transparent;
              --bs-table-border-color: var(--bs-border-color);
              --bs-table-accent-bg: transparent;
              --bs-table-striped-color: var(--bs-body-color);
              --bs-table-striped-bg: rgba(0, 0, 0, 0.05);
              --bs-table-active-color: var(--bs-body-color);
              --bs-table-active-bg: rgba(0, 0, 0, 0.1);
              --bs-table-hover-color: var(--bs-body-color);
              --bs-table-hover-bg: rgba(0, 0, 0, 0.075);
              width: 100%;
              margin-bottom: 1rem;
              color: var(--bs-table-color);
              vertical-align: top;
              border-color: var(--bs-table-border-color);
            }
            .table > :not(caption) > * > * {
              padding: 0.5rem 0.5rem;
              background-color: var(--bs-table-bg);
              border-bottom-width: var(--bs-border-width);
              box-shadow: inset 0 0 0 9999px var(--bs-table-accent-bg);
            }
            .table > tbody {
              vertical-align: inherit;
            }
            .table > thead {
              vertical-align: bottom;
            }

            .table-group-divider {
              border-top: calc(var(--bs-border-width) * 2) solid currentcolor;
            }

            .caption-top {
              caption-side: top;
            }

            .table-sm > :not(caption) > * > * {
              padding: 0.25rem 0.25rem;
            }

            .table-bordered > :not(caption) > * {
              border-width: var(--bs-border-width) 0;
            }
            .table-bordered > :not(caption) > * > * {
              border-width: 0 var(--bs-border-width);
            }

            .table-borderless > :not(caption) > * > * {
              border-bottom-width: 0;
            }
            .table-borderless > :not(:first-child) {
              border-top-width: 0;
            }

            .table-striped > tbody > tr:nth-of-type(odd) > * {
              --bs-table-accent-bg: var(--bs-table-striped-bg);
              color: var(--bs-table-striped-color);
            }

            .table-striped-columns > :not(caption) > tr > :nth-child(even) {
              --bs-table-accent-bg: var(--bs-table-striped-bg);
              color: var(--bs-table-striped-color);
            }

            .table-active {
              --bs-table-accent-bg: var(--bs-table-active-bg);
              color: var(--bs-table-active-color);
            }

            .table-hover > tbody > tr:hover > * {
              --bs-table-accent-bg: var(--bs-table-hover-bg);
              color: var(--bs-table-hover-color);
            }

            .table-primary {
              --bs-table-color: #000;
              --bs-table-bg: #cfe2ff;
              --bs-table-border-color: #bacbe6;
              --bs-table-striped-bg: #c5d7f2;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #bacbe6;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #bfd1ec;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-secondary {
              --bs-table-color: #000;
              --bs-table-bg: #e2e3e5;
              --bs-table-border-color: #cbccce;
              --bs-table-striped-bg: #d7d8da;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #cbccce;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #d1d2d4;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-success {
              --bs-table-color: #000;
              --bs-table-bg: #d1e7dd;
              --bs-table-border-color: #bcd0c7;
              --bs-table-striped-bg: #c7dbd2;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #bcd0c7;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #c1d6cc;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-info {
              --bs-table-color: #000;
              --bs-table-bg: #cff4fc;
              --bs-table-border-color: #badce3;
              --bs-table-striped-bg: #c5e8ef;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #badce3;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #bfe2e9;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-warning {
              --bs-table-color: #000;
              --bs-table-bg: #fff3cd;
              --bs-table-border-color: #e6dbb9;
              --bs-table-striped-bg: #f2e7c3;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #e6dbb9;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #ece1be;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-danger {
              --bs-table-color: #000;
              --bs-table-bg: #f8d7da;
              --bs-table-border-color: #dfc2c4;
              --bs-table-striped-bg: #eccccf;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #dfc2c4;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #e5c7ca;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-light {
              --bs-table-color: #000;
              --bs-table-bg: #f8f9fa;
              --bs-table-border-color: #dfe0e1;
              --bs-table-striped-bg: #ecedee;
              --bs-table-striped-color: #000;
              --bs-table-active-bg: #dfe0e1;
              --bs-table-active-color: #000;
              --bs-table-hover-bg: #e5e6e7;
              --bs-table-hover-color: #000;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-dark {
              --bs-table-color: #fff;
              --bs-table-bg: #212529;
              --bs-table-border-color: #373b3e;
              --bs-table-striped-bg: #2c3034;
              --bs-table-striped-color: #fff;
              --bs-table-active-bg: #373b3e;
              --bs-table-active-color: #fff;
              --bs-table-hover-bg: #323539;
              --bs-table-hover-color: #fff;
              color: var(--bs-table-color);
              border-color: var(--bs-table-border-color);
            }

            .table-responsive {
              overflow-x: auto;
              -webkit-overflow-scrolling: touch;
            }

            @media (max-width: 575.98px) {
              .table-responsive-sm {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
              }
            }
            @media (max-width: 767.98px) {
              .table-responsive-md {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
              }
            }
            @media (max-width: 991.98px) {
              .table-responsive-lg {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
              }
            }
            @media (max-width: 1199.98px) {
              .table-responsive-xl {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
              }
            }
            @media (max-width: 1399.98px) {
              .table-responsive-xxl {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
              }
            }
            .form-label {
              margin-bottom: 0.5rem;
            }

            .col-form-label {
              padding-top: calc(0.375rem + var(--bs-border-width));
              padding-bottom: calc(0.375rem + var(--bs-border-width));
              margin-bottom: 0;
              font-size: inherit;
              line-height: 1.5;
            }

            .col-form-label-lg {
              padding-top: calc(0.5rem + var(--bs-border-width));
              padding-bottom: calc(0.5rem + var(--bs-border-width));
              font-size: 1.25rem;
            }

            .col-form-label-sm {
              padding-top: calc(0.25rem + var(--bs-border-width));
              padding-bottom: calc(0.25rem + var(--bs-border-width));
              font-size: 0.875rem;
            }

            .form-text {
              margin-top: 0.25rem;
              font-size: 0.875em;
              color: var(--bs-secondary-color);
            }

            .form-control {
              display: block;
              width: 100%;
              padding: 0.375rem 0.75rem;
              font-size: 1rem;
              font-weight: 400;
              line-height: 1.5;
              color: var(--bs-body-color);
              background-color: var(--bs-body-bg);
              background-clip: padding-box;
              border: var(--bs-border-width) solid var(--bs-border-color);
              -webkit-appearance: none;
              -moz-appearance: none;
              appearance: none;
              border-radius: 0.375rem;
              transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-control {
                transition: none;
              }
            }
            .form-control[type=file] {
              overflow: hidden;
            }
            .form-control[type=file]:not(:disabled):not([readonly]) {
              cursor: pointer;
            }
            .form-control:focus {
              color: var(--bs-body-color);
              background-color: var(--bs-body-bg);
              border-color: #86b7fe;
              outline: 0;
              box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
            }
            .form-control::-webkit-date-and-time-value {
              min-width: 85px;
              height: 1.5em;
              margin: 0;
            }
            .form-control::-webkit-datetime-edit {
              display: block;
              padding: 0;
            }
            .form-control::-moz-placeholder {
              color: var(--bs-secondary-color);
              opacity: 1;
            }
            .form-control::placeholder {
              color: var(--bs-secondary-color);
              opacity: 1;
            }
            .form-control:disabled {
              background-color: var(--bs-secondary-bg);
              opacity: 1;
            }
            .form-control::-webkit-file-upload-button {
              padding: 0.375rem 0.75rem;
              margin: -0.375rem -0.75rem;
              -webkit-margin-end: 0.75rem;
              margin-inline-end: 0.75rem;
              color: var(--bs-body-color);
              background-color: var(--bs-tertiary-bg);
              pointer-events: none;
              border-color: inherit;
              border-style: solid;
              border-width: 0;
              border-inline-end-width: var(--bs-border-width);
              border-radius: 0;
              -webkit-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
              transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
            }
            .form-control::file-selector-button {
              padding: 0.375rem 0.75rem;
              margin: -0.375rem -0.75rem;
              -webkit-margin-end: 0.75rem;
              margin-inline-end: 0.75rem;
              color: var(--bs-body-color);
              background-color: var(--bs-tertiary-bg);
              pointer-events: none;
              border-color: inherit;
              border-style: solid;
              border-width: 0;
              border-inline-end-width: var(--bs-border-width);
              border-radius: 0;
              transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-control::-webkit-file-upload-button {
                -webkit-transition: none;
                transition: none;
              }
              .form-control::file-selector-button {
                transition: none;
              }
            }
            .form-control:hover:not(:disabled):not([readonly])::-webkit-file-upload-button {
              background-color: var(--bs-secondary-bg);
            }
            .form-control:hover:not(:disabled):not([readonly])::file-selector-button {
              background-color: var(--bs-secondary-bg);
            }

            .form-control-plaintext {
              display: block;
              width: 100%;
              padding: 0.375rem 0;
              margin-bottom: 0;
              line-height: 1.5;
              color: var(--bs-body-color);
              background-color: transparent;
              border: solid transparent;
              border-width: var(--bs-border-width) 0;
            }
            .form-control-plaintext:focus {
              outline: 0;
            }
            .form-control-plaintext.form-control-sm, .form-control-plaintext.form-control-lg {
              padding-right: 0;
              padding-left: 0;
            }

            .form-control-sm {
              min-height: calc(1.5em + 0.5rem + calc(var(--bs-border-width) * 2));
              padding: 0.25rem 0.5rem;
              font-size: 0.875rem;
              border-radius: 0.25rem;
            }
            .form-control-sm::-webkit-file-upload-button {
              padding: 0.25rem 0.5rem;
              margin: -0.25rem -0.5rem;
              -webkit-margin-end: 0.5rem;
              margin-inline-end: 0.5rem;
            }
            .form-control-sm::file-selector-button {
              padding: 0.25rem 0.5rem;
              margin: -0.25rem -0.5rem;
              -webkit-margin-end: 0.5rem;
              margin-inline-end: 0.5rem;
            }

            .form-control-lg {
              min-height: calc(1.5em + 1rem + calc(var(--bs-border-width) * 2));
              padding: 0.5rem 1rem;
              font-size: 1.25rem;
              border-radius: 0.5rem;
            }
            .form-control-lg::-webkit-file-upload-button {
              padding: 0.5rem 1rem;
              margin: -0.5rem -1rem;
              -webkit-margin-end: 1rem;
              margin-inline-end: 1rem;
            }
            .form-control-lg::file-selector-button {
              padding: 0.5rem 1rem;
              margin: -0.5rem -1rem;
              -webkit-margin-end: 1rem;
              margin-inline-end: 1rem;
            }

            textarea.form-control {
              min-height: calc(1.5em + 0.75rem + calc(var(--bs-border-width) * 2));
            }
            textarea.form-control-sm {
              min-height: calc(1.5em + 0.5rem + calc(var(--bs-border-width) * 2));
            }
            textarea.form-control-lg {
              min-height: calc(1.5em + 1rem + calc(var(--bs-border-width) * 2));
            }

            .form-control-color {
              width: 3rem;
              height: calc(1.5em + 0.75rem + calc(var(--bs-border-width) * 2));
              padding: 0.375rem;
            }
            .form-control-color:not(:disabled):not([readonly]) {
              cursor: pointer;
            }
            .form-control-color::-moz-color-swatch {
              border: 0 !important;
              border-radius: 0.375rem;
            }
            .form-control-color::-webkit-color-swatch {
              border: 0 !important;
              border-radius: 0.375rem;
            }
            .form-control-color.form-control-sm {
              height: calc(1.5em + 0.5rem + calc(var(--bs-border-width) * 2));
            }
            .form-control-color.form-control-lg {
              height: calc(1.5em + 1rem + calc(var(--bs-border-width) * 2));
            }

            .form-select {
              --bs-form-select-bg-img: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23343a40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e");
              display: block;
              width: 100%;
              padding: 0.375rem 2.25rem 0.375rem 0.75rem;
              font-size: 1rem;
              font-weight: 400;
              line-height: 1.5;
              color: var(--bs-body-color);
              background-color: var(--bs-body-bg);
              background-image: var(--bs-form-select-bg-img), var(--bs-form-select-bg-icon, none);
              background-repeat: no-repeat;
              background-position: right 0.75rem center;
              background-size: 16px 12px;
              border: var(--bs-border-width) solid var(--bs-border-color);
              border-radius: 0.375rem;
              transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
              -webkit-appearance: none;
              -moz-appearance: none;
              appearance: none;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-select {
                transition: none;
              }
            }
            .form-select:focus {
              border-color: #86b7fe;
              outline: 0;
              box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
            }
            .form-select[multiple], .form-select[size]:not([size="1"]) {
              padding-right: 0.75rem;
              background-image: none;
            }
            .form-select:disabled {
              background-color: var(--bs-secondary-bg);
            }
            .form-select:-moz-focusring {
              color: transparent;
              text-shadow: 0 0 0 var(--bs-body-color);
            }

            .form-select-sm {
              padding-top: 0.25rem;
              padding-bottom: 0.25rem;
              padding-left: 0.5rem;
              font-size: 0.875rem;
              border-radius: 0.25rem;
            }

            .form-select-lg {
              padding-top: 0.5rem;
              padding-bottom: 0.5rem;
              padding-left: 1rem;
              font-size: 1.25rem;
              border-radius: 0.5rem;
            }

            [data-bs-theme=dark] .form-select {
              --bs-form-select-bg-img: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23adb5bd' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3e%3c/svg%3e");
            }

            .form-check {
              display: block;
              min-height: 1.5rem;
              padding-left: 1.5em;
              margin-bottom: 0.125rem;
            }
            .form-check .form-check-input {
              float: left;
              margin-left: -1.5em;
            }

            .form-check-reverse {
              padding-right: 1.5em;
              padding-left: 0;
              text-align: right;
            }
            .form-check-reverse .form-check-input {
              float: right;
              margin-right: -1.5em;
              margin-left: 0;
            }

            .form-check-input {
              --bs-form-check-bg: var(--bs-body-bg);
              width: 1em;
              height: 1em;
              margin-top: 0.25em;
              vertical-align: top;
              background-color: var(--bs-form-check-bg);
              background-image: var(--bs-form-check-bg-image);
              background-repeat: no-repeat;
              background-position: center;
              background-size: contain;
              border: var(--bs-border-width) solid var(--bs-border-color);
              -webkit-appearance: none;
              -moz-appearance: none;
              appearance: none;
              -webkit-print-color-adjust: exact;
              color-adjust: exact;
              print-color-adjust: exact;
            }
            .form-check-input[type=checkbox] {
              border-radius: 0.25em;
            }
            .form-check-input[type=radio] {
              border-radius: 50%;
            }
            .form-check-input:active {
              filter: brightness(90%);
            }
            .form-check-input:focus {
              border-color: #86b7fe;
              outline: 0;
              box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
            }
            .form-check-input:checked {
              background-color: #0d6efd;
              border-color: #0d6efd;
            }
            .form-check-input:checked[type=checkbox] {
              --bs-form-check-bg-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='m6 10 3 3 6-6'/%3e%3c/svg%3e");
            }
            .form-check-input:checked[type=radio] {
              --bs-form-check-bg-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='2' fill='%23fff'/%3e%3c/svg%3e");
            }
            .form-check-input[type=checkbox]:indeterminate {
              background-color: #0d6efd;
              border-color: #0d6efd;
              --bs-form-check-bg-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10h8'/%3e%3c/svg%3e");
            }
            .form-check-input:disabled {
              pointer-events: none;
              filter: none;
              opacity: 0.5;
            }
            .form-check-input[disabled] ~ .form-check-label, .form-check-input:disabled ~ .form-check-label {
              cursor: default;
              opacity: 0.5;
            }

            .form-switch {
              padding-left: 2.5em;
            }
            .form-switch .form-check-input {
              --bs-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%280, 0, 0, 0.25%29'/%3e%3c/svg%3e");
              width: 2em;
              margin-left: -2.5em;
              background-image: var(--bs-form-switch-bg);
              background-position: left center;
              border-radius: 2em;
              transition: background-position 0.15s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-switch .form-check-input {
                transition: none;
              }
            }
            .form-switch .form-check-input:focus {
              --bs-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%2386b7fe'/%3e%3c/svg%3e");
            }
            .form-switch .form-check-input:checked {
              background-position: right center;
              --bs-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e");
            }
            .form-switch.form-check-reverse {
              padding-right: 2.5em;
              padding-left: 0;
            }
            .form-switch.form-check-reverse .form-check-input {
              margin-right: -2.5em;
              margin-left: 0;
            }

            .form-check-inline {
              display: inline-block;
              margin-right: 1rem;
            }

            .btn-check {
              position: absolute;
              clip: rect(0, 0, 0, 0);
              pointer-events: none;
            }
            .btn-check[disabled] + .btn, .btn-check:disabled + .btn {
              pointer-events: none;
              filter: none;
              opacity: 0.65;
            }

            [data-bs-theme=dark] .form-switch .form-check-input:not(:checked):not(:focus) {
              --bs-form-switch-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='rgba%28255, 255, 255, 0.25%29'/%3e%3c/svg%3e");
            }

            .form-range {
              width: 100%;
              height: 1.5rem;
              padding: 0;
              background-color: transparent;
              -webkit-appearance: none;
              -moz-appearance: none;
              appearance: none;
            }
            .form-range:focus {
              outline: 0;
            }
            .form-range:focus::-webkit-slider-thumb {
              box-shadow: 0 0 0 1px #fff, 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
            }
            .form-range:focus::-moz-range-thumb {
              box-shadow: 0 0 0 1px #fff, 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
            }
            .form-range::-moz-focus-outer {
              border: 0;
            }
            .form-range::-webkit-slider-thumb {
              width: 1rem;
              height: 1rem;
              margin-top: -0.25rem;
              background-color: #0d6efd;
              border: 0;
              border-radius: 1rem;
              -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
              transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
              -webkit-appearance: none;
              appearance: none;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-range::-webkit-slider-thumb {
                -webkit-transition: none;
                transition: none;
              }
            }
            .form-range::-webkit-slider-thumb:active {
              background-color: #b6d4fe;
            }
            .form-range::-webkit-slider-runnable-track {
              width: 100%;
              height: 0.5rem;
              color: transparent;
              cursor: pointer;
              background-color: var(--bs-tertiary-bg);
              border-color: transparent;
              border-radius: 1rem;
            }
            .form-range::-moz-range-thumb {
              width: 1rem;
              height: 1rem;
              background-color: #0d6efd;
              border: 0;
              border-radius: 1rem;
              -moz-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
              transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
              -moz-appearance: none;
              appearance: none;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-range::-moz-range-thumb {
                -moz-transition: none;
                transition: none;
              }
            }
            .form-range::-moz-range-thumb:active {
              background-color: #b6d4fe;
            }
            .form-range::-moz-range-track {
              width: 100%;
              height: 0.5rem;
              color: transparent;
              cursor: pointer;
              background-color: var(--bs-tertiary-bg);
              border-color: transparent;
              border-radius: 1rem;
            }
            .form-range:disabled {
              pointer-events: none;
            }
            .form-range:disabled::-webkit-slider-thumb {
              background-color: var(--bs-secondary-color);
            }
            .form-range:disabled::-moz-range-thumb {
              background-color: var(--bs-secondary-color);
            }

            .form-floating {
              position: relative;
            }
            .form-floating:not(.form-control:disabled)::before {
              position: absolute;
              top: var(--bs-border-width);
              left: var(--bs-border-width);
              width: calc(100% - (calc(calc(0.375em + 0.1875rem) + calc(0.75em + 0.375rem))));
              height: 1.875em;
              content: "";
              background-color: var(--bs-body-bg);
              border-radius: 0.375rem;
            }
            .form-floating > .form-control,
            .form-floating > .form-control-plaintext,
            .form-floating > .form-select {
              height: calc(3.5rem + calc(var(--bs-border-width) * 2));
              line-height: 1.25;
            }
            .form-floating > label {
              position: absolute;
              top: 0;
              left: 0;
              width: 100%;
              height: 100%;
              padding: 1rem 0.75rem;
              overflow: hidden;
              text-align: start;
              text-overflow: ellipsis;
              white-space: nowrap;
              pointer-events: none;
              border: var(--bs-border-width) solid transparent;
              transform-origin: 0 0;
              transition: opacity 0.1s ease-in-out, transform 0.1s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .form-floating > label {
                transition: none;
              }
            }
            .form-floating > .form-control,
            .form-floating > .form-control-plaintext {
              padding: 1rem 0.75rem;
            }
            .form-floating > .form-control::-moz-placeholder, .form-floating > .form-control-plaintext::-moz-placeholder {
              color: transparent;
            }
            .form-floating > .form-control::placeholder,
            .form-floating > .form-control-plaintext::placeholder {
              color: transparent;
            }
            .form-floating > .form-control:not(:-moz-placeholder-shown), .form-floating > .form-control-plaintext:not(:-moz-placeholder-shown) {
              padding-top: 1.625rem;
              padding-bottom: 0.625rem;
            }
            .form-floating > .form-control:focus, .form-floating > .form-control:not(:placeholder-shown),
            .form-floating > .form-control-plaintext:focus,
            .form-floating > .form-control-plaintext:not(:placeholder-shown) {
              padding-top: 1.625rem;
              padding-bottom: 0.625rem;
            }
            .form-floating > .form-control:-webkit-autofill,
            .form-floating > .form-control-plaintext:-webkit-autofill {
              padding-top: 1.625rem;
              padding-bottom: 0.625rem;
            }
            .form-floating > .form-select {
              padding-top: 1.625rem;
              padding-bottom: 0.625rem;
            }
            .form-floating > .form-control:not(:-moz-placeholder-shown) ~ label {
              opacity: 0.65;
              transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem);
            }
            .form-floating > .form-control:focus ~ label,
            .form-floating > .form-control:not(:placeholder-shown) ~ label,
            .form-floating > .form-control-plaintext ~ label,
            .form-floating > .form-select ~ label {
              opacity: 0.65;
              transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem);
            }
            .form-floating > .form-control:-webkit-autofill ~ label {
              opacity: 0.65;
              transform: scale(0.85) translateY(-0.5rem) translateX(0.15rem);
            }
            .form-floating > .form-control-plaintext ~ label {
              border-width: var(--bs-border-width) 0;
            }
            .form-floating > .form-control:disabled ~ label {
              color: #6c757d;
            }

            .input-group {
              position: relative;
              display: flex;
              flex-wrap: wrap;
              align-items: stretch;
              width: 100%;
            }
            .input-group > .form-control,
            .input-group > .form-select,
            .input-group > .form-floating {
              position: relative;
              flex: 1 1 auto;
              width: 1%;
              min-width: 0;
            }
            .input-group > .form-control:focus,
            .input-group > .form-select:focus,
            .input-group > .form-floating:focus-within {
              z-index: 5;
            }
            .input-group .btn {
              position: relative;
              z-index: 2;
            }
            .input-group .btn:focus {
              z-index: 5;
            }

            .input-group-text {
              display: flex;
              align-items: center;
              padding: 0.375rem 0.75rem;
              font-size: 1rem;
              font-weight: 400;
              line-height: 1.5;
              color: var(--bs-body-color);
              text-align: center;
              white-space: nowrap;
              background-color: var(--bs-tertiary-bg);
              border: var(--bs-border-width) solid var(--bs-border-color);
              border-radius: 0.375rem;
            }

            .input-group-lg > .form-control,
            .input-group-lg > .form-select,
            .input-group-lg > .input-group-text,
            .input-group-lg > .btn {
              padding: 0.5rem 1rem;
              font-size: 1.25rem;
              border-radius: 0.5rem;
            }

            .input-group-sm > .form-control,
            .input-group-sm > .form-select,
            .input-group-sm > .input-group-text,
            .input-group-sm > .btn {
              padding: 0.25rem 0.5rem;
              font-size: 0.875rem;
              border-radius: 0.25rem;
            }

            .input-group-lg > .form-select,
            .input-group-sm > .form-select {
              padding-right: 3rem;
            }

            .input-group:not(.has-validation) > :not(:last-child):not(.dropdown-toggle):not(.dropdown-menu):not(.form-floating),
            .input-group:not(.has-validation) > .dropdown-toggle:nth-last-child(n+3),
            .input-group:not(.has-validation) > .form-floating:not(:last-child) > .form-control,
            .input-group:not(.has-validation) > .form-floating:not(:last-child) > .form-select {
              border-top-right-radius: 0;
              border-bottom-right-radius: 0;
            }
            .input-group.has-validation > :nth-last-child(n+3):not(.dropdown-toggle):not(.dropdown-menu):not(.form-floating),
            .input-group.has-validation > .dropdown-toggle:nth-last-child(n+4),
            .input-group.has-validation > .form-floating:nth-last-child(n+3) > .form-control,
            .input-group.has-validation > .form-floating:nth-last-child(n+3) > .form-select {
              border-top-right-radius: 0;
              border-bottom-right-radius: 0;
            }
            .input-group > :not(:first-child):not(.dropdown-menu):not(.valid-tooltip):not(.valid-feedback):not(.invalid-tooltip):not(.invalid-feedback) {
              margin-left: calc(var(--bs-border-width) * -1);
              border-top-left-radius: 0;
              border-bottom-left-radius: 0;
            }
            .input-group > .form-floating:not(:first-child) > .form-control,
            .input-group > .form-floating:not(:first-child) > .form-select {
              border-top-left-radius: 0;
              border-bottom-left-radius: 0;
            }

            .valid-feedback {
              display: none;
              width: 100%;
              margin-top: 0.25rem;
              font-size: 0.875em;
              color: var(--bs-form-valid-color);
            }

            .valid-tooltip {
              position: absolute;
              top: 100%;
              z-index: 5;
              display: none;
              max-width: 100%;
              padding: 0.25rem 0.5rem;
              margin-top: 0.1rem;
              font-size: 0.875rem;
              color: #fff;
              background-color: var(--bs-success);
              border-radius: var(--bs-border-radius);
            }

            .was-validated :valid ~ .valid-feedback,
            .was-validated :valid ~ .valid-tooltip,
            .is-valid ~ .valid-feedback,
            .is-valid ~ .valid-tooltip {
              display: block;
            }

            .was-validated .form-control:valid, .form-control.is-valid {
              border-color: var(--bs-form-valid-border-color);
              padding-right: calc(1.5em + 0.75rem);
              background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
              background-repeat: no-repeat;
              background-position: right calc(0.375em + 0.1875rem) center;
              background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
            }
            .was-validated .form-control:valid:focus, .form-control.is-valid:focus {
              border-color: var(--bs-form-valid-border-color);
              box-shadow: 0 0 0 0.25rem rgba(var(--bs-success-rgb), 0.25);
            }

            .was-validated textarea.form-control:valid, textarea.form-control.is-valid {
              padding-right: calc(1.5em + 0.75rem);
              background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem);
            }

            .was-validated .form-select:valid, .form-select.is-valid {
              border-color: var(--bs-form-valid-border-color);
            }
            .was-validated .form-select:valid:not([multiple]):not([size]), .was-validated .form-select:valid:not([multiple])[size="1"], .form-select.is-valid:not([multiple]):not([size]), .form-select.is-valid:not([multiple])[size="1"] {
              --bs-form-select-bg-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
              padding-right: 4.125rem;
              background-position: right 0.75rem center, center right 2.25rem;
              background-size: 16px 12px, calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
            }
            .was-validated .form-select:valid:focus, .form-select.is-valid:focus {
              border-color: var(--bs-form-valid-border-color);
              box-shadow: 0 0 0 0.25rem rgba(var(--bs-success-rgb), 0.25);
            }

            .was-validated .form-control-color:valid, .form-control-color.is-valid {
              width: calc(3rem + calc(1.5em + 0.75rem));
            }

            .was-validated .form-check-input:valid, .form-check-input.is-valid {
              border-color: var(--bs-form-valid-border-color);
            }
            .was-validated .form-check-input:valid:checked, .form-check-input.is-valid:checked {
              background-color: var(--bs-form-valid-color);
            }
            .was-validated .form-check-input:valid:focus, .form-check-input.is-valid:focus {
              box-shadow: 0 0 0 0.25rem rgba(var(--bs-success-rgb), 0.25);
            }
            .was-validated .form-check-input:valid ~ .form-check-label, .form-check-input.is-valid ~ .form-check-label {
              color: var(--bs-form-valid-color);
            }

            .form-check-inline .form-check-input ~ .valid-feedback {
              margin-left: 0.5em;
            }

            .was-validated .input-group > .form-control:not(:focus):valid, .input-group > .form-control:not(:focus).is-valid,
            .was-validated .input-group > .form-select:not(:focus):valid,
            .input-group > .form-select:not(:focus).is-valid,
            .was-validated .input-group > .form-floating:not(:focus-within):valid,
            .input-group > .form-floating:not(:focus-within).is-valid {
              z-index: 3;
            }

            .invalid-feedback {
              display: none;
              width: 100%;
              margin-top: 0.25rem;
              font-size: 0.875em;
              color: var(--bs-form-invalid-color);
            }

            .invalid-tooltip {
              position: absolute;
              top: 100%;
              z-index: 5;
              display: none;
              max-width: 100%;
              padding: 0.25rem 0.5rem;
              margin-top: 0.1rem;
              font-size: 0.875rem;
              color: #fff;
              background-color: var(--bs-danger);
              border-radius: var(--bs-border-radius);
            }

            .was-validated :invalid ~ .invalid-feedback,
            .was-validated :invalid ~ .invalid-tooltip,
            .is-invalid ~ .invalid-feedback,
            .is-invalid ~ .invalid-tooltip {
              display: block;
            }

            .was-validated .form-control:invalid, .form-control.is-invalid {
              border-color: var(--bs-form-invalid-border-color);
              padding-right: calc(1.5em + 0.75rem);
              background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
              background-repeat: no-repeat;
              background-position: right calc(0.375em + 0.1875rem) center;
              background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
            }
            .was-validated .form-control:invalid:focus, .form-control.is-invalid:focus {
              border-color: var(--bs-form-invalid-border-color);
              box-shadow: 0 0 0 0.25rem rgba(var(--bs-danger-rgb), 0.25);
            }

            .was-validated textarea.form-control:invalid, textarea.form-control.is-invalid {
              padding-right: calc(1.5em + 0.75rem);
              background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem);
            }

            .was-validated .form-select:invalid, .form-select.is-invalid {
              border-color: var(--bs-form-invalid-border-color);
            }
            .was-validated .form-select:invalid:not([multiple]):not([size]), .was-validated .form-select:invalid:not([multiple])[size="1"], .form-select.is-invalid:not([multiple]):not([size]), .form-select.is-invalid:not([multiple])[size="1"] {
              --bs-form-select-bg-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
              padding-right: 4.125rem;
              background-position: right 0.75rem center, center right 2.25rem;
              background-size: 16px 12px, calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
            }
            .was-validated .form-select:invalid:focus, .form-select.is-invalid:focus {
              border-color: var(--bs-form-invalid-border-color);
              box-shadow: 0 0 0 0.25rem rgba(var(--bs-danger-rgb), 0.25);
            }

            .was-validated .form-control-color:invalid, .form-control-color.is-invalid {
              width: calc(3rem + calc(1.5em + 0.75rem));
            }

            .was-validated .form-check-input:invalid, .form-check-input.is-invalid {
              border-color: var(--bs-form-invalid-border-color);
            }
            .was-validated .form-check-input:invalid:checked, .form-check-input.is-invalid:checked {
              background-color: var(--bs-form-invalid-color);
            }
            .was-validated .form-check-input:invalid:focus, .form-check-input.is-invalid:focus {
              box-shadow: 0 0 0 0.25rem rgba(var(--bs-danger-rgb), 0.25);
            }
            .was-validated .form-check-input:invalid ~ .form-check-label, .form-check-input.is-invalid ~ .form-check-label {
              color: var(--bs-form-invalid-color);
            }

            .form-check-inline .form-check-input ~ .invalid-feedback {
              margin-left: 0.5em;
            }

            .was-validated .input-group > .form-control:not(:focus):invalid, .input-group > .form-control:not(:focus).is-invalid,
            .was-validated .input-group > .form-select:not(:focus):invalid,
            .input-group > .form-select:not(:focus).is-invalid,
            .was-validated .input-group > .form-floating:not(:focus-within):invalid,
            .input-group > .form-floating:not(:focus-within).is-invalid {
              z-index: 4;
            }

            .btn {
              --bs-btn-padding-x: 0.75rem;
              --bs-btn-padding-y: 0.375rem;
              --bs-btn-font-family: ;
              --bs-btn-font-size: 1rem;
              --bs-btn-font-weight: 400;
              --bs-btn-line-height: 1.5;
              --bs-btn-color: var(--bs-body-color);
              --bs-btn-bg: transparent;
              --bs-btn-border-width: var(--bs-border-width);
              --bs-btn-border-color: transparent;
              --bs-btn-border-radius: 0.375rem;
              --bs-btn-hover-border-color: transparent;
              --bs-btn-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 1px 1px rgba(0, 0, 0, 0.075);
              --bs-btn-disabled-opacity: 0.65;
              --bs-btn-focus-box-shadow: 0 0 0 0.25rem rgba(var(--bs-btn-focus-shadow-rgb), .5);
              display: inline-block;
              padding: var(--bs-btn-padding-y) var(--bs-btn-padding-x);
              font-family: var(--bs-btn-font-family);
              font-size: var(--bs-btn-font-size);
              font-weight: var(--bs-btn-font-weight);
              line-height: var(--bs-btn-line-height);
              color: var(--bs-btn-color);
              text-align: center;
              text-decoration: none;
              vertical-align: middle;
              cursor: pointer;
              -webkit-user-select: none;
              -moz-user-select: none;
              user-select: none;
              border: var(--bs-btn-border-width) solid var(--bs-btn-border-color);
              border-radius: var(--bs-btn-border-radius);
              background-color: var(--bs-btn-bg);
              transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .btn {
                transition: none;
              }
            }
            .btn:hover {
              color: var(--bs-btn-hover-color);
              background-color: var(--bs-btn-hover-bg);
              border-color: var(--bs-btn-hover-border-color);
            }
            .btn-check + .btn:hover {
              color: var(--bs-btn-color);
              background-color: var(--bs-btn-bg);
              border-color: var(--bs-btn-border-color);
            }
            .btn:focus-visible {
              color: var(--bs-btn-hover-color);
              background-color: var(--bs-btn-hover-bg);
              border-color: var(--bs-btn-hover-border-color);
              outline: 0;
              box-shadow: var(--bs-btn-focus-box-shadow);
            }
            .btn-check:focus-visible + .btn {
              border-color: var(--bs-btn-hover-border-color);
              outline: 0;
              box-shadow: var(--bs-btn-focus-box-shadow);
            }
            .btn-check:checked + .btn, :not(.btn-check) + .btn:active, .btn:first-child:active, .btn.active, .btn.show {
              color: var(--bs-btn-active-color);
              background-color: var(--bs-btn-active-bg);
              border-color: var(--bs-btn-active-border-color);
            }
            .btn-check:checked + .btn:focus-visible, :not(.btn-check) + .btn:active:focus-visible, .btn:first-child:active:focus-visible, .btn.active:focus-visible, .btn.show:focus-visible {
              box-shadow: var(--bs-btn-focus-box-shadow);
            }
            .btn:disabled, .btn.disabled, fieldset:disabled .btn {
              color: var(--bs-btn-disabled-color);
              pointer-events: none;
              background-color: var(--bs-btn-disabled-bg);
              border-color: var(--bs-btn-disabled-border-color);
              opacity: var(--bs-btn-disabled-opacity);
            }

            .btn-primary {
              --bs-btn-color: #fff;
              --bs-btn-bg: #0d6efd;
              --bs-btn-border-color: #0d6efd;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #0b5ed7;
              --bs-btn-hover-border-color: #0a58ca;
              --bs-btn-focus-shadow-rgb: 49, 132, 253;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #0a58ca;
              --bs-btn-active-border-color: #0a53be;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #fff;
              --bs-btn-disabled-bg: #0d6efd;
              --bs-btn-disabled-border-color: #0d6efd;
            }

            .btn-secondary {
              --bs-btn-color: #fff;
              --bs-btn-bg: #6c757d;
              --bs-btn-border-color: #6c757d;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #5c636a;
              --bs-btn-hover-border-color: #565e64;
              --bs-btn-focus-shadow-rgb: 130, 138, 145;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #565e64;
              --bs-btn-active-border-color: #51585e;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #fff;
              --bs-btn-disabled-bg: #6c757d;
              --bs-btn-disabled-border-color: #6c757d;
            }

            .btn-success {
              --bs-btn-color: #fff;
              --bs-btn-bg: #198754;
              --bs-btn-border-color: #198754;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #157347;
              --bs-btn-hover-border-color: #146c43;
              --bs-btn-focus-shadow-rgb: 60, 153, 110;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #146c43;
              --bs-btn-active-border-color: #13653f;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #fff;
              --bs-btn-disabled-bg: #198754;
              --bs-btn-disabled-border-color: #198754;
            }

            .btn-info {
              --bs-btn-color: #000;
              --bs-btn-bg: #0dcaf0;
              --bs-btn-border-color: #0dcaf0;
              --bs-btn-hover-color: #000;
              --bs-btn-hover-bg: #31d2f2;
              --bs-btn-hover-border-color: #25cff2;
              --bs-btn-focus-shadow-rgb: 11, 172, 204;
              --bs-btn-active-color: #000;
              --bs-btn-active-bg: #3dd5f3;
              --bs-btn-active-border-color: #25cff2;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #000;
              --bs-btn-disabled-bg: #0dcaf0;
              --bs-btn-disabled-border-color: #0dcaf0;
            }

            .btn-warning {
              --bs-btn-color: #000;
              --bs-btn-bg: #ffc107;
              --bs-btn-border-color: #ffc107;
              --bs-btn-hover-color: #000;
              --bs-btn-hover-bg: #ffca2c;
              --bs-btn-hover-border-color: #ffc720;
              --bs-btn-focus-shadow-rgb: 217, 164, 6;
              --bs-btn-active-color: #000;
              --bs-btn-active-bg: #ffcd39;
              --bs-btn-active-border-color: #ffc720;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #000;
              --bs-btn-disabled-bg: #ffc107;
              --bs-btn-disabled-border-color: #ffc107;
            }

            .btn-danger {
              --bs-btn-color: #fff;
              --bs-btn-bg: #dc3545;
              --bs-btn-border-color: #dc3545;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #bb2d3b;
              --bs-btn-hover-border-color: #b02a37;
              --bs-btn-focus-shadow-rgb: 225, 83, 97;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #b02a37;
              --bs-btn-active-border-color: #a52834;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #fff;
              --bs-btn-disabled-bg: #dc3545;
              --bs-btn-disabled-border-color: #dc3545;
            }

            .btn-light {
              --bs-btn-color: #000;
              --bs-btn-bg: #f8f9fa;
              --bs-btn-border-color: #f8f9fa;
              --bs-btn-hover-color: #000;
              --bs-btn-hover-bg: #d3d4d5;
              --bs-btn-hover-border-color: #c6c7c8;
              --bs-btn-focus-shadow-rgb: 211, 212, 213;
              --bs-btn-active-color: #000;
              --bs-btn-active-bg: #c6c7c8;
              --bs-btn-active-border-color: #babbbc;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #000;
              --bs-btn-disabled-bg: #f8f9fa;
              --bs-btn-disabled-border-color: #f8f9fa;
            }

            .btn-dark {
              --bs-btn-color: #fff;
              --bs-btn-bg: #212529;
              --bs-btn-border-color: #212529;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #424649;
              --bs-btn-hover-border-color: #373b3e;
              --bs-btn-focus-shadow-rgb: 66, 70, 73;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #4d5154;
              --bs-btn-active-border-color: #373b3e;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #fff;
              --bs-btn-disabled-bg: #212529;
              --bs-btn-disabled-border-color: #212529;
            }

            .btn-outline-primary {
              --bs-btn-color: #0d6efd;
              --bs-btn-border-color: #0d6efd;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #0d6efd;
              --bs-btn-hover-border-color: #0d6efd;
              --bs-btn-focus-shadow-rgb: 13, 110, 253;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #0d6efd;
              --bs-btn-active-border-color: #0d6efd;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #0d6efd;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #0d6efd;
              --bs-gradient: none;
            }

            .btn-outline-secondary {
              --bs-btn-color: #6c757d;
              --bs-btn-border-color: #6c757d;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #6c757d;
              --bs-btn-hover-border-color: #6c757d;
              --bs-btn-focus-shadow-rgb: 108, 117, 125;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #6c757d;
              --bs-btn-active-border-color: #6c757d;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #6c757d;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #6c757d;
              --bs-gradient: none;
            }

            .btn-outline-success {
              --bs-btn-color: #198754;
              --bs-btn-border-color: #198754;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #198754;
              --bs-btn-hover-border-color: #198754;
              --bs-btn-focus-shadow-rgb: 25, 135, 84;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #198754;
              --bs-btn-active-border-color: #198754;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #198754;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #198754;
              --bs-gradient: none;
            }

            .btn-outline-info {
              --bs-btn-color: #0dcaf0;
              --bs-btn-border-color: #0dcaf0;
              --bs-btn-hover-color: #000;
              --bs-btn-hover-bg: #0dcaf0;
              --bs-btn-hover-border-color: #0dcaf0;
              --bs-btn-focus-shadow-rgb: 13, 202, 240;
              --bs-btn-active-color: #000;
              --bs-btn-active-bg: #0dcaf0;
              --bs-btn-active-border-color: #0dcaf0;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #0dcaf0;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #0dcaf0;
              --bs-gradient: none;
            }

            .btn-outline-warning {
              --bs-btn-color: #ffc107;
              --bs-btn-border-color: #ffc107;
              --bs-btn-hover-color: #000;
              --bs-btn-hover-bg: #ffc107;
              --bs-btn-hover-border-color: #ffc107;
              --bs-btn-focus-shadow-rgb: 255, 193, 7;
              --bs-btn-active-color: #000;
              --bs-btn-active-bg: #ffc107;
              --bs-btn-active-border-color: #ffc107;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #ffc107;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #ffc107;
              --bs-gradient: none;
            }

            .btn-outline-danger {
              --bs-btn-color: #dc3545;
              --bs-btn-border-color: #dc3545;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #dc3545;
              --bs-btn-hover-border-color: #dc3545;
              --bs-btn-focus-shadow-rgb: 220, 53, 69;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #dc3545;
              --bs-btn-active-border-color: #dc3545;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #dc3545;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #dc3545;
              --bs-gradient: none;
            }

            .btn-outline-light {
              --bs-btn-color: #f8f9fa;
              --bs-btn-border-color: #f8f9fa;
              --bs-btn-hover-color: #000;
              --bs-btn-hover-bg: #f8f9fa;
              --bs-btn-hover-border-color: #f8f9fa;
              --bs-btn-focus-shadow-rgb: 248, 249, 250;
              --bs-btn-active-color: #000;
              --bs-btn-active-bg: #f8f9fa;
              --bs-btn-active-border-color: #f8f9fa;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #f8f9fa;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #f8f9fa;
              --bs-gradient: none;
            }

            .btn-outline-dark {
              --bs-btn-color: #212529;
              --bs-btn-border-color: #212529;
              --bs-btn-hover-color: #fff;
              --bs-btn-hover-bg: #212529;
              --bs-btn-hover-border-color: #212529;
              --bs-btn-focus-shadow-rgb: 33, 37, 41;
              --bs-btn-active-color: #fff;
              --bs-btn-active-bg: #212529;
              --bs-btn-active-border-color: #212529;
              --bs-btn-active-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
              --bs-btn-disabled-color: #212529;
              --bs-btn-disabled-bg: transparent;
              --bs-btn-disabled-border-color: #212529;
              --bs-gradient: none;
            }

            .btn-link {
              --bs-btn-font-weight: 400;
              --bs-btn-color: var(--bs-link-color);
              --bs-btn-bg: transparent;
              --bs-btn-border-color: transparent;
              --bs-btn-hover-color: var(--bs-link-hover-color);
              --bs-btn-hover-border-color: transparent;
              --bs-btn-active-color: var(--bs-link-hover-color);
              --bs-btn-active-border-color: transparent;
              --bs-btn-disabled-color: #6c757d;
              --bs-btn-disabled-border-color: transparent;
              --bs-btn-box-shadow: 0 0 0 #000;
              --bs-btn-focus-shadow-rgb: 49, 132, 253;
              text-decoration: underline;
            }
            .btn-link:focus-visible {
              color: var(--bs-btn-color);
            }
            .btn-link:hover {
              color: var(--bs-btn-hover-color);
            }

            .btn-lg, .btn-group-lg > .btn {
              --bs-btn-padding-y: 0.5rem;
              --bs-btn-padding-x: 1rem;
              --bs-btn-font-size: 1.25rem;
              --bs-btn-border-radius: 0.5rem;
            }

            .btn-sm, .btn-group-sm > .btn {
              --bs-btn-padding-y: 0.25rem;
              --bs-btn-padding-x: 0.5rem;
              --bs-btn-font-size: 0.875rem;
              --bs-btn-border-radius: 0.25rem;
            }

            .fade {
              transition: opacity 0.15s linear;
            }
            @media (prefers-reduced-motion: reduce) {
              .fade {
                transition: none;
              }
            }
            .fade:not(.show) {
              opacity: 0;
            }

            .collapse:not(.show) {
              display: none;
            }

            .collapsing {
              height: 0;
              overflow: hidden;
              transition: height 0.35s ease;
            }
            @media (prefers-reduced-motion: reduce) {
              .collapsing {
                transition: none;
              }
            }
            .collapsing.collapse-horizontal {
              width: 0;
              height: auto;
              transition: width 0.35s ease;
            }
            @media (prefers-reduced-motion: reduce) {
              .collapsing.collapse-horizontal {
                transition: none;
              }
            }

            .dropup,
            .dropend,
            .dropdown,
            .dropstart,
            .dropup-center,
            .dropdown-center {
              position: relative;
            }

            .dropdown-toggle {
              white-space: nowrap;
            }
            .dropdown-toggle::after {
              display: inline-block;
              margin-left: 0.255em;
              vertical-align: 0.255em;
              content: "";
              border-top: 0.3em solid;
              border-right: 0.3em solid transparent;
              border-bottom: 0;
              border-left: 0.3em solid transparent;
            }
            .dropdown-toggle:empty::after {
              margin-left: 0;
            }

            .dropdown-menu {
              --bs-dropdown-zindex: 1000;
              --bs-dropdown-min-width: 10rem;
              --bs-dropdown-padding-x: 0;
              --bs-dropdown-padding-y: 0.5rem;
              --bs-dropdown-spacer: 0.125rem;
              --bs-dropdown-font-size: 1rem;
              --bs-dropdown-color: var(--bs-body-color);
              --bs-dropdown-bg: var(--bs-body-bg);
              --bs-dropdown-border-color: var(--bs-border-color-translucent);
              --bs-dropdown-border-radius: 0.375rem;
              --bs-dropdown-border-width: var(--bs-border-width);
              --bs-dropdown-inner-border-radius: calc(0.375rem - var(--bs-border-width));
              --bs-dropdown-divider-bg: var(--bs-border-color-translucent);
              --bs-dropdown-divider-margin-y: 0.5rem;
              --bs-dropdown-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
              --bs-dropdown-link-color: var(--bs-body-color);
              --bs-dropdown-link-hover-color: var(--bs-body-color);
              --bs-dropdown-link-hover-bg: var(--bs-tertiary-bg);
              --bs-dropdown-link-active-color: #fff;
              --bs-dropdown-link-active-bg: #0d6efd;
              --bs-dropdown-link-disabled-color: var(--bs-tertiary-color);
              --bs-dropdown-item-padding-x: 1rem;
              --bs-dropdown-item-padding-y: 0.25rem;
              --bs-dropdown-header-color: #6c757d;
              --bs-dropdown-header-padding-x: 1rem;
              --bs-dropdown-header-padding-y: 0.5rem;
              position: absolute;
              z-index: var(--bs-dropdown-zindex);
              display: none;
              min-width: var(--bs-dropdown-min-width);
              padding: var(--bs-dropdown-padding-y) var(--bs-dropdown-padding-x);
              margin: 0;
              font-size: var(--bs-dropdown-font-size);
              color: var(--bs-dropdown-color);
              text-align: left;
              list-style: none;
              background-color: var(--bs-dropdown-bg);
              background-clip: padding-box;
              border: var(--bs-dropdown-border-width) solid var(--bs-dropdown-border-color);
              border-radius: var(--bs-dropdown-border-radius);
            }
            .dropdown-menu[data-bs-popper] {
              top: 100%;
              left: 0;
              margin-top: var(--bs-dropdown-spacer);
            }

            .dropdown-menu-start {
              --bs-position: start;
            }
            .dropdown-menu-start[data-bs-popper] {
              right: auto;
              left: 0;
            }

            .dropdown-menu-end {
              --bs-position: end;
            }
            .dropdown-menu-end[data-bs-popper] {
              right: 0;
              left: auto;
            }

            @media (min-width: 576px) {
              .dropdown-menu-sm-start {
                --bs-position: start;
              }
              .dropdown-menu-sm-start[data-bs-popper] {
                right: auto;
                left: 0;
              }
              .dropdown-menu-sm-end {
                --bs-position: end;
              }
              .dropdown-menu-sm-end[data-bs-popper] {
                right: 0;
                left: auto;
              }
            }
            @media (min-width: 768px) {
              .dropdown-menu-md-start {
                --bs-position: start;
              }
              .dropdown-menu-md-start[data-bs-popper] {
                right: auto;
                left: 0;
              }
              .dropdown-menu-md-end {
                --bs-position: end;
              }
              .dropdown-menu-md-end[data-bs-popper] {
                right: 0;
                left: auto;
              }
            }
            @media (min-width: 992px) {
              .dropdown-menu-lg-start {
                --bs-position: start;
              }
              .dropdown-menu-lg-start[data-bs-popper] {
                right: auto;
                left: 0;
              }
              .dropdown-menu-lg-end {
                --bs-position: end;
              }
              .dropdown-menu-lg-end[data-bs-popper] {
                right: 0;
                left: auto;
              }
            }
            @media (min-width: 1200px) {
              .dropdown-menu-xl-start {
                --bs-position: start;
              }
              .dropdown-menu-xl-start[data-bs-popper] {
                right: auto;
                left: 0;
              }
              .dropdown-menu-xl-end {
                --bs-position: end;
              }
              .dropdown-menu-xl-end[data-bs-popper] {
                right: 0;
                left: auto;
              }
            }
            @media (min-width: 1400px) {
              .dropdown-menu-xxl-start {
                --bs-position: start;
              }
              .dropdown-menu-xxl-start[data-bs-popper] {
                right: auto;
                left: 0;
              }
              .dropdown-menu-xxl-end {
                --bs-position: end;
              }
              .dropdown-menu-xxl-end[data-bs-popper] {
                right: 0;
                left: auto;
              }
            }
            .dropup .dropdown-menu[data-bs-popper] {
              top: auto;
              bottom: 100%;
              margin-top: 0;
              margin-bottom: var(--bs-dropdown-spacer);
            }
            .dropup .dropdown-toggle::after {
              display: inline-block;
              margin-left: 0.255em;
              vertical-align: 0.255em;
              content: "";
              border-top: 0;
              border-right: 0.3em solid transparent;
              border-bottom: 0.3em solid;
              border-left: 0.3em solid transparent;
            }
            .dropup .dropdown-toggle:empty::after {
              margin-left: 0;
            }

            .dropend .dropdown-menu[data-bs-popper] {
              top: 0;
              right: auto;
              left: 100%;
              margin-top: 0;
              margin-left: var(--bs-dropdown-spacer);
            }
            .dropend .dropdown-toggle::after {
              display: inline-block;
              margin-left: 0.255em;
              vertical-align: 0.255em;
              content: "";
              border-top: 0.3em solid transparent;
              border-right: 0;
              border-bottom: 0.3em solid transparent;
              border-left: 0.3em solid;
            }
            .dropend .dropdown-toggle:empty::after {
              margin-left: 0;
            }
            .dropend .dropdown-toggle::after {
              vertical-align: 0;
            }

            .dropstart .dropdown-menu[data-bs-popper] {
              top: 0;
              right: 100%;
              left: auto;
              margin-top: 0;
              margin-right: var(--bs-dropdown-spacer);
            }
            .dropstart .dropdown-toggle::after {
              display: inline-block;
              margin-left: 0.255em;
              vertical-align: 0.255em;
              content: "";
            }
            .dropstart .dropdown-toggle::after {
              display: none;
            }
            .dropstart .dropdown-toggle::before {
              display: inline-block;
              margin-right: 0.255em;
              vertical-align: 0.255em;
              content: "";
              border-top: 0.3em solid transparent;
              border-right: 0.3em solid;
              border-bottom: 0.3em solid transparent;
            }
            .dropstart .dropdown-toggle:empty::after {
              margin-left: 0;
            }
            .dropstart .dropdown-toggle::before {
              vertical-align: 0;
            }

            .dropdown-divider {
              height: 0;
              margin: var(--bs-dropdown-divider-margin-y) 0;
              overflow: hidden;
              border-top: 1px solid var(--bs-dropdown-divider-bg);
              opacity: 1;
            }

            .dropdown-item {
              display: block;
              width: 100%;
              padding: var(--bs-dropdown-item-padding-y) var(--bs-dropdown-item-padding-x);
              clear: both;
              font-weight: 400;
              color: var(--bs-dropdown-link-color);
              text-align: inherit;
              text-decoration: none;
              white-space: nowrap;
              background-color: transparent;
              border: 0;
              border-radius: var(--bs-dropdown-item-border-radius, 0);
            }
            .dropdown-item:hover, .dropdown-item:focus {
              color: var(--bs-dropdown-link-hover-color);
              background-color: var(--bs-dropdown-link-hover-bg);
            }
            .dropdown-item.active, .dropdown-item:active {
              color: var(--bs-dropdown-link-active-color);
              text-decoration: none;
              background-color: var(--bs-dropdown-link-active-bg);
            }
            .dropdown-item.disabled, .dropdown-item:disabled {
              color: var(--bs-dropdown-link-disabled-color);
              pointer-events: none;
              background-color: transparent;
            }

            .dropdown-menu.show {
              display: block;
            }

            .dropdown-header {
              display: block;
              padding: var(--bs-dropdown-header-padding-y) var(--bs-dropdown-header-padding-x);
              margin-bottom: 0;
              font-size: 0.875rem;
              color: var(--bs-dropdown-header-color);
              white-space: nowrap;
            }

            .dropdown-item-text {
              display: block;
              padding: var(--bs-dropdown-item-padding-y) var(--bs-dropdown-item-padding-x);
              color: var(--bs-dropdown-link-color);
            }

            .dropdown-menu-dark {
              --bs-dropdown-color: #dee2e6;
              --bs-dropdown-bg: #343a40;
              --bs-dropdown-border-color: var(--bs-border-color-translucent);
              --bs-dropdown-box-shadow: ;
              --bs-dropdown-link-color: #dee2e6;
              --bs-dropdown-link-hover-color: #fff;
              --bs-dropdown-divider-bg: var(--bs-border-color-translucent);
              --bs-dropdown-link-hover-bg: rgba(255, 255, 255, 0.15);
              --bs-dropdown-link-active-color: #fff;
              --bs-dropdown-link-active-bg: #0d6efd;
              --bs-dropdown-link-disabled-color: #adb5bd;
              --bs-dropdown-header-color: #adb5bd;
            }

            .btn-group,
            .btn-group-vertical {
              position: relative;
              display: inline-flex;
              vertical-align: middle;
            }
            .btn-group > .btn,
            .btn-group-vertical > .btn {
              position: relative;
              flex: 1 1 auto;
            }
            .btn-group > .btn-check:checked + .btn,
            .btn-group > .btn-check:focus + .btn,
            .btn-group > .btn:hover,
            .btn-group > .btn:focus,
            .btn-group > .btn:active,
            .btn-group > .btn.active,
            .btn-group-vertical > .btn-check:checked + .btn,
            .btn-group-vertical > .btn-check:focus + .btn,
            .btn-group-vertical > .btn:hover,
            .btn-group-vertical > .btn:focus,
            .btn-group-vertical > .btn:active,
            .btn-group-vertical > .btn.active {
              z-index: 1;
            }

            .btn-toolbar {
              display: flex;
              flex-wrap: wrap;
              justify-content: flex-start;
            }
            .btn-toolbar .input-group {
              width: auto;
            }

            .btn-group {
              border-radius: 0.375rem;
            }
            .btn-group > :not(.btn-check:first-child) + .btn,
            .btn-group > .btn-group:not(:first-child) {
              margin-left: calc(var(--bs-border-width) * -1);
            }
            .btn-group > .btn:not(:last-child):not(.dropdown-toggle),
            .btn-group > .btn.dropdown-toggle-split:first-child,
            .btn-group > .btn-group:not(:last-child) > .btn {
              border-top-right-radius: 0;
              border-bottom-right-radius: 0;
            }
            .btn-group > .btn:nth-child(n+3),
            .btn-group > :not(.btn-check) + .btn,
            .btn-group > .btn-group:not(:first-child) > .btn {
              border-top-left-radius: 0;
              border-bottom-left-radius: 0;
            }

            .dropdown-toggle-split {
              padding-right: 0.5625rem;
              padding-left: 0.5625rem;
            }
            .dropdown-toggle-split::after, .dropup .dropdown-toggle-split::after, .dropend .dropdown-toggle-split::after {
              margin-left: 0;
            }
            .dropstart .dropdown-toggle-split::before {
              margin-right: 0;
            }

            .btn-sm + .dropdown-toggle-split, .btn-group-sm > .btn + .dropdown-toggle-split {
              padding-right: 0.375rem;
              padding-left: 0.375rem;
            }

            .btn-lg + .dropdown-toggle-split, .btn-group-lg > .btn + .dropdown-toggle-split {
              padding-right: 0.75rem;
              padding-left: 0.75rem;
            }

            .btn-group-vertical {
              flex-direction: column;
              align-items: flex-start;
              justify-content: center;
            }
            .btn-group-vertical > .btn,
            .btn-group-vertical > .btn-group {
              width: 100%;
            }
            .btn-group-vertical > .btn:not(:first-child),
            .btn-group-vertical > .btn-group:not(:first-child) {
              margin-top: calc(var(--bs-border-width) * -1);
            }
            .btn-group-vertical > .btn:not(:last-child):not(.dropdown-toggle),
            .btn-group-vertical > .btn-group:not(:last-child) > .btn {
              border-bottom-right-radius: 0;
              border-bottom-left-radius: 0;
            }
            .btn-group-vertical > .btn ~ .btn,
            .btn-group-vertical > .btn-group:not(:first-child) > .btn {
              border-top-left-radius: 0;
              border-top-right-radius: 0;
            }

            .nav {
              --bs-nav-link-padding-x: 1rem;
              --bs-nav-link-padding-y: 0.5rem;
              --bs-nav-link-font-weight: ;
              --bs-nav-link-color: var(--bs-link-color);
              --bs-nav-link-hover-color: var(--bs-link-hover-color);
              --bs-nav-link-disabled-color: var(--bs-secondary-color);
              display: flex;
              flex-wrap: wrap;
              padding-left: 0;
              margin-bottom: 0;
              list-style: none;
            }

            .nav-link {
              display: block;
              padding: var(--bs-nav-link-padding-y) var(--bs-nav-link-padding-x);
              font-size: var(--bs-nav-link-font-size);
              font-weight: var(--bs-nav-link-font-weight);
              color: var(--bs-nav-link-color);
              text-decoration: none;
              background: none;
              border: 0;
              transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .nav-link {
                transition: none;
              }
            }
            .nav-link:hover, .nav-link:focus {
              color: var(--bs-nav-link-hover-color);
            }
            .nav-link:focus-visible {
              outline: 0;
              box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
            }
            .nav-link.disabled {
              color: var(--bs-nav-link-disabled-color);
              pointer-events: none;
              cursor: default;
            }

            .nav-tabs {
              --bs-nav-tabs-border-width: var(--bs-border-width);
              --bs-nav-tabs-border-color: var(--bs-border-color);
              --bs-nav-tabs-border-radius: var(--bs-border-radius);
              --bs-nav-tabs-link-hover-border-color: var(--bs-secondary-bg) var(--bs-secondary-bg) var(--bs-border-color);
              --bs-nav-tabs-link-active-color: var(--bs-emphasis-color);
              --bs-nav-tabs-link-active-bg: var(--bs-body-bg);
              --bs-nav-tabs-link-active-border-color: var(--bs-border-color) var(--bs-border-color) var(--bs-body-bg);
              border-bottom: var(--bs-nav-tabs-border-width) solid var(--bs-nav-tabs-border-color);
            }
            .nav-tabs .nav-link {
              margin-bottom: calc(-1 * var(--bs-nav-tabs-border-width));
              border: var(--bs-nav-tabs-border-width) solid transparent;
              border-top-left-radius: var(--bs-nav-tabs-border-radius);
              border-top-right-radius: var(--bs-nav-tabs-border-radius);
            }
            .nav-tabs .nav-link:hover, .nav-tabs .nav-link:focus {
              isolation: isolate;
              border-color: var(--bs-nav-tabs-link-hover-border-color);
            }
            .nav-tabs .nav-link.disabled, .nav-tabs .nav-link:disabled {
              color: var(--bs-nav-link-disabled-color);
              background-color: transparent;
              border-color: transparent;
            }
            .nav-tabs .nav-link.active,
            .nav-tabs .nav-item.show .nav-link {
              color: var(--bs-nav-tabs-link-active-color);
              background-color: var(--bs-nav-tabs-link-active-bg);
              border-color: var(--bs-nav-tabs-link-active-border-color);
            }
            .nav-tabs .dropdown-menu {
              margin-top: calc(-1 * var(--bs-nav-tabs-border-width));
              border-top-left-radius: 0;
              border-top-right-radius: 0;
            }

            .nav-pills {
              --bs-nav-pills-border-radius: 0.375rem;
              --bs-nav-pills-link-active-color: #fff;
              --bs-nav-pills-link-active-bg: #0d6efd;
            }
            .nav-pills .nav-link {
              border-radius: var(--bs-nav-pills-border-radius);
            }
            .nav-pills .nav-link:disabled {
              color: var(--bs-nav-link-disabled-color);
              background-color: transparent;
              border-color: transparent;
            }
            .nav-pills .nav-link.active,
            .nav-pills .show > .nav-link {
              color: var(--bs-nav-pills-link-active-color);
              background-color: var(--bs-nav-pills-link-active-bg);
            }

            .nav-underline {
              --bs-nav-underline-gap: 1rem;
              --bs-nav-underline-border-width: 0.125rem;
              --bs-nav-underline-link-active-color: var(--bs-emphasis-color);
              gap: var(--bs-nav-underline-gap);
            }
            .nav-underline .nav-link {
              padding-right: 0;
              padding-left: 0;
              border-bottom: var(--bs-nav-underline-border-width) solid transparent;
            }
            .nav-underline .nav-link:hover, .nav-underline .nav-link:focus {
              border-bottom-color: currentcolor;
            }
            .nav-underline .nav-link.active,
            .nav-underline .show > .nav-link {
              font-weight: 700;
              color: var(--bs-nav-underline-link-active-color);
              border-bottom-color: currentcolor;
            }

            .nav-fill > .nav-link,
            .nav-fill .nav-item {
              flex: 1 1 auto;
              text-align: center;
            }

            .nav-justified > .nav-link,
            .nav-justified .nav-item {
              flex-basis: 0;
              flex-grow: 1;
              text-align: center;
            }

            .nav-fill .nav-item .nav-link,
            .nav-justified .nav-item .nav-link {
              width: 100%;
            }

            .tab-content > .tab-pane {
              display: none;
            }
            .tab-content > .active {
              display: block;
            }

            .navbar {
              --bs-navbar-padding-x: 0;
              --bs-navbar-padding-y: 0.5rem;
              --bs-navbar-color: rgba(var(--bs-emphasis-color-rgb), 0.65);
              --bs-navbar-hover-color: rgba(var(--bs-emphasis-color-rgb), 0.8);
              --bs-navbar-disabled-color: rgba(var(--bs-emphasis-color-rgb), 0.3);
              --bs-navbar-active-color: rgba(var(--bs-emphasis-color-rgb), 1);
              --bs-navbar-brand-padding-y: 0.3125rem;
              --bs-navbar-brand-margin-end: 1rem;
              --bs-navbar-brand-font-size: 1.25rem;
              --bs-navbar-brand-color: rgba(var(--bs-emphasis-color-rgb), 1);
              --bs-navbar-brand-hover-color: rgba(var(--bs-emphasis-color-rgb), 1);
              --bs-navbar-nav-link-padding-x: 0.5rem;
              --bs-navbar-toggler-padding-y: 0.25rem;
              --bs-navbar-toggler-padding-x: 0.75rem;
              --bs-navbar-toggler-font-size: 1.25rem;
              --bs-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%2833, 37, 41, 0.75%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
              --bs-navbar-toggler-border-color: rgba(var(--bs-emphasis-color-rgb), 0.15);
              --bs-navbar-toggler-border-radius: 0.375rem;
              --bs-navbar-toggler-focus-width: 0.25rem;
              --bs-navbar-toggler-transition: box-shadow 0.15s ease-in-out;
              position: relative;
              display: flex;
              flex-wrap: wrap;
              align-items: center;
              justify-content: space-between;
              padding: var(--bs-navbar-padding-y) var(--bs-navbar-padding-x);
            }
            .navbar > .container,
            .navbar > .container-fluid,
            .navbar > .container-sm,
            .navbar > .container-md,
            .navbar > .container-lg,
            .navbar > .container-xl,
            .navbar > .container-xxl {
              display: flex;
              flex-wrap: inherit;
              align-items: center;
              justify-content: space-between;
            }
            .navbar-brand {
              padding-top: var(--bs-navbar-brand-padding-y);
              padding-bottom: var(--bs-navbar-brand-padding-y);
              margin-right: var(--bs-navbar-brand-margin-end);
              font-size: var(--bs-navbar-brand-font-size);
              color: var(--bs-navbar-brand-color);
              text-decoration: none;
              white-space: nowrap;
            }
            .navbar-brand:hover, .navbar-brand:focus {
              color: var(--bs-navbar-brand-hover-color);
            }

            .navbar-nav {
              --bs-nav-link-padding-x: 0;
              --bs-nav-link-padding-y: 0.5rem;
              --bs-nav-link-font-weight: ;
              --bs-nav-link-color: var(--bs-navbar-color);
              --bs-nav-link-hover-color: var(--bs-navbar-hover-color);
              --bs-nav-link-disabled-color: var(--bs-navbar-disabled-color);
              display: flex;
              flex-direction: column;
              padding-left: 0;
              margin-bottom: 0;
              list-style: none;
            }
            .navbar-nav .nav-link.active, .navbar-nav .nav-link.show {
              color: var(--bs-navbar-active-color);
            }
            .navbar-nav .dropdown-menu {
              position: static;
            }

            .navbar-text {
              padding-top: 0.5rem;
              padding-bottom: 0.5rem;
              color: var(--bs-navbar-color);
            }
            .navbar-text a,
            .navbar-text a:hover,
            .navbar-text a:focus {
              color: var(--bs-navbar-active-color);
            }

            .navbar-collapse {
              flex-basis: 100%;
              flex-grow: 1;
              align-items: center;
            }

            .navbar-toggler {
              padding: var(--bs-navbar-toggler-padding-y) var(--bs-navbar-toggler-padding-x);
              font-size: var(--bs-navbar-toggler-font-size);
              line-height: 1;
              color: var(--bs-navbar-color);
              background-color: transparent;
              border: var(--bs-border-width) solid var(--bs-navbar-toggler-border-color);
              border-radius: var(--bs-navbar-toggler-border-radius);
              transition: var(--bs-navbar-toggler-transition);
            }
            @media (prefers-reduced-motion: reduce) {
              .navbar-toggler {
                transition: none;
              }
            }
            .navbar-toggler:hover {
              text-decoration: none;
            }
            .navbar-toggler:focus {
              text-decoration: none;
              outline: 0;
              box-shadow: 0 0 0 var(--bs-navbar-toggler-focus-width);
            }

            .navbar-toggler-icon {
              display: inline-block;
              width: 1.5em;
              height: 1.5em;
              vertical-align: middle;
              background-image: var(--bs-navbar-toggler-icon-bg);
              background-repeat: no-repeat;
              background-position: center;
              background-size: 100%;
            }

            .navbar-nav-scroll {
              max-height: var(--bs-scroll-height, 75vh);
              overflow-y: auto;
            }

            @media (min-width: 576px) {
              .navbar-expand-sm {
                flex-wrap: nowrap;
                justify-content: flex-start;
              }
              .navbar-expand-sm .navbar-nav {
                flex-direction: row;
              }
              .navbar-expand-sm .navbar-nav .dropdown-menu {
                position: absolute;
              }
              .navbar-expand-sm .navbar-nav .nav-link {
                padding-right: var(--bs-navbar-nav-link-padding-x);
                padding-left: var(--bs-navbar-nav-link-padding-x);
              }
              .navbar-expand-sm .navbar-nav-scroll {
                overflow: visible;
              }
              .navbar-expand-sm .navbar-collapse {
                display: flex !important;
                flex-basis: auto;
              }
              .navbar-expand-sm .navbar-toggler {
                display: none;
              }
              .navbar-expand-sm .offcanvas {
                position: static;
                z-index: auto;
                flex-grow: 1;
                width: auto !important;
                height: auto !important;
                visibility: visible !important;
                background-color: transparent !important;
                border: 0 !important;
                transform: none !important;
                transition: none;
              }
              .navbar-expand-sm .offcanvas .offcanvas-header {
                display: none;
              }
              .navbar-expand-sm .offcanvas .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
              }
            }
            @media (min-width: 768px) {
              .navbar-expand-md {
                flex-wrap: nowrap;
                justify-content: flex-start;
              }
              .navbar-expand-md .navbar-nav {
                flex-direction: row;
              }
              .navbar-expand-md .navbar-nav .dropdown-menu {
                position: absolute;
              }
              .navbar-expand-md .navbar-nav .nav-link {
                padding-right: var(--bs-navbar-nav-link-padding-x);
                padding-left: var(--bs-navbar-nav-link-padding-x);
              }
              .navbar-expand-md .navbar-nav-scroll {
                overflow: visible;
              }
              .navbar-expand-md .navbar-collapse {
                display: flex !important;
                flex-basis: auto;
              }
              .navbar-expand-md .navbar-toggler {
                display: none;
              }
              .navbar-expand-md .offcanvas {
                position: static;
                z-index: auto;
                flex-grow: 1;
                width: auto !important;
                height: auto !important;
                visibility: visible !important;
                background-color: transparent !important;
                border: 0 !important;
                transform: none !important;
                transition: none;
              }
              .navbar-expand-md .offcanvas .offcanvas-header {
                display: none;
              }
              .navbar-expand-md .offcanvas .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
              }
            }
            @media (min-width: 992px) {
              .navbar-expand-lg {
                flex-wrap: nowrap;
                justify-content: flex-start;
              }
              .navbar-expand-lg .navbar-nav {
                flex-direction: row;
              }
              .navbar-expand-lg .navbar-nav .dropdown-menu {
                position: absolute;
              }
              .navbar-expand-lg .navbar-nav .nav-link {
                padding-right: var(--bs-navbar-nav-link-padding-x);
                padding-left: var(--bs-navbar-nav-link-padding-x);
              }
              .navbar-expand-lg .navbar-nav-scroll {
                overflow: visible;
              }
              .navbar-expand-lg .navbar-collapse {
                display: flex !important;
                flex-basis: auto;
              }
              .navbar-expand-lg .navbar-toggler {
                display: none;
              }
              .navbar-expand-lg .offcanvas {
                position: static;
                z-index: auto;
                flex-grow: 1;
                width: auto !important;
                height: auto !important;
                visibility: visible !important;
                background-color: transparent !important;
                border: 0 !important;
                transform: none !important;
                transition: none;
              }
              .navbar-expand-lg .offcanvas .offcanvas-header {
                display: none;
              }
              .navbar-expand-lg .offcanvas .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
              }
            }
            @media (min-width: 1200px) {
              .navbar-expand-xl {
                flex-wrap: nowrap;
                justify-content: flex-start;
              }
              .navbar-expand-xl .navbar-nav {
                flex-direction: row;
              }
              .navbar-expand-xl .navbar-nav .dropdown-menu {
                position: absolute;
              }
              .navbar-expand-xl .navbar-nav .nav-link {
                padding-right: var(--bs-navbar-nav-link-padding-x);
                padding-left: var(--bs-navbar-nav-link-padding-x);
              }
              .navbar-expand-xl .navbar-nav-scroll {
                overflow: visible;
              }
              .navbar-expand-xl .navbar-collapse {
                display: flex !important;
                flex-basis: auto;
              }
              .navbar-expand-xl .navbar-toggler {
                display: none;
              }
              .navbar-expand-xl .offcanvas {
                position: static;
                z-index: auto;
                flex-grow: 1;
                width: auto !important;
                height: auto !important;
                visibility: visible !important;
                background-color: transparent !important;
                border: 0 !important;
                transform: none !important;
                transition: none;
              }
              .navbar-expand-xl .offcanvas .offcanvas-header {
                display: none;
              }
              .navbar-expand-xl .offcanvas .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
              }
            }
            @media (min-width: 1400px) {
              .navbar-expand-xxl {
                flex-wrap: nowrap;
                justify-content: flex-start;
              }
              .navbar-expand-xxl .navbar-nav {
                flex-direction: row;
              }
              .navbar-expand-xxl .navbar-nav .dropdown-menu {
                position: absolute;
              }
              .navbar-expand-xxl .navbar-nav .nav-link {
                padding-right: var(--bs-navbar-nav-link-padding-x);
                padding-left: var(--bs-navbar-nav-link-padding-x);
              }
              .navbar-expand-xxl .navbar-nav-scroll {
                overflow: visible;
              }
              .navbar-expand-xxl .navbar-collapse {
                display: flex !important;
                flex-basis: auto;
              }
              .navbar-expand-xxl .navbar-toggler {
                display: none;
              }
              .navbar-expand-xxl .offcanvas {
                position: static;
                z-index: auto;
                flex-grow: 1;
                width: auto !important;
                height: auto !important;
                visibility: visible !important;
                background-color: transparent !important;
                border: 0 !important;
                transform: none !important;
                transition: none;
              }
              .navbar-expand-xxl .offcanvas .offcanvas-header {
                display: none;
              }
              .navbar-expand-xxl .offcanvas .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
              }
            }
            .navbar-expand {
              flex-wrap: nowrap;
              justify-content: flex-start;
            }
            .navbar-expand .navbar-nav {
              flex-direction: row;
            }
            .navbar-expand .navbar-nav .dropdown-menu {
              position: absolute;
            }
            .navbar-expand .navbar-nav .nav-link {
              padding-right: var(--bs-navbar-nav-link-padding-x);
              padding-left: var(--bs-navbar-nav-link-padding-x);
            }
            .navbar-expand .navbar-nav-scroll {
              overflow: visible;
            }
            .navbar-expand .navbar-collapse {
              display: flex !important;
              flex-basis: auto;
            }
            .navbar-expand .navbar-toggler {
              display: none;
            }
            .navbar-expand .offcanvas {
              position: static;
              z-index: auto;
              flex-grow: 1;
              width: auto !important;
              height: auto !important;
              visibility: visible !important;
              background-color: transparent !important;
              border: 0 !important;
              transform: none !important;
              transition: none;
            }
            .navbar-expand .offcanvas .offcanvas-header {
              display: none;
            }
            .navbar-expand .offcanvas .offcanvas-body {
              display: flex;
              flex-grow: 0;
              padding: 0;
              overflow-y: visible;
            }

            .navbar-dark {
              --bs-navbar-color: rgba(255, 255, 255, 0.55);
              --bs-navbar-hover-color: rgba(255, 255, 255, 0.75);
              --bs-navbar-disabled-color: rgba(255, 255, 255, 0.25);
              --bs-navbar-active-color: #fff;
              --bs-navbar-brand-color: #fff;
              --bs-navbar-brand-hover-color: #fff;
              --bs-navbar-toggler-border-color: rgba(255, 255, 255, 0.1);
              --bs-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
            }

            [data-bs-theme=dark] .navbar-toggler-icon {
              --bs-navbar-toggler-icon-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
            }

            .card {
              --bs-card-spacer-y: 1rem;
              --bs-card-spacer-x: 1rem;
              --bs-card-title-spacer-y: 0.5rem;
              --bs-card-title-color: ;
              --bs-card-subtitle-color: ;
              --bs-card-border-width: var(--bs-border-width);
              --bs-card-border-color: var(--bs-border-color-translucent);
              --bs-card-border-radius: var(--bs-border-radius);
              --bs-card-box-shadow: ;
              --bs-card-inner-border-radius: calc(var(--bs-border-radius) - (var(--bs-border-width)));
              --bs-card-cap-padding-y: 0.5rem;
              --bs-card-cap-padding-x: 1rem;
              --bs-card-cap-bg: rgba(var(--bs-body-color-rgb), 0.03);
              --bs-card-cap-color: ;
              --bs-card-height: ;
              --bs-card-color: ;
              --bs-card-bg: var(--bs-body-bg);
              --bs-card-img-overlay-padding: 1rem;
              --bs-card-group-margin: 0.75rem;
              position: relative;
              display: flex;
              flex-direction: column;
              min-width: 0;
              height: var(--bs-card-height);
              color: var(--bs-body-color);
              word-wrap: break-word;
              background-color: var(--bs-card-bg);
              background-clip: border-box;
              border: var(--bs-card-border-width) solid var(--bs-card-border-color);
              border-radius: var(--bs-card-border-radius);
            }
            .card > hr {
              margin-right: 0;
              margin-left: 0;
            }
            .card > .list-group {
              border-top: inherit;
              border-bottom: inherit;
            }
            .card > .list-group:first-child {
              border-top-width: 0;
              border-top-left-radius: var(--bs-card-inner-border-radius);
              border-top-right-radius: var(--bs-card-inner-border-radius);
            }
            .card > .list-group:last-child {
              border-bottom-width: 0;
              border-bottom-right-radius: var(--bs-card-inner-border-radius);
              border-bottom-left-radius: var(--bs-card-inner-border-radius);
            }
            .card > .card-header + .list-group,
            .card > .list-group + .card-footer {
              border-top: 0;
            }

            .card-body {
              flex: 1 1 auto;
              padding: var(--bs-card-spacer-y) var(--bs-card-spacer-x);
              color: var(--bs-card-color);
            }

            .card-title {
              margin-bottom: var(--bs-card-title-spacer-y);
              color: var(--bs-card-title-color);
            }

            .card-subtitle {
              margin-top: calc(-0.5 * var(--bs-card-title-spacer-y));
              margin-bottom: 0;
              color: var(--bs-card-subtitle-color);
            }

            .card-text:last-child {
              margin-bottom: 0;
            }

            .card-link + .card-link {
              margin-left: var(--bs-card-spacer-x);
            }

            .card-header {
              padding: var(--bs-card-cap-padding-y) var(--bs-card-cap-padding-x);
              margin-bottom: 0;
              color: var(--bs-card-cap-color);
              background-color: var(--bs-card-cap-bg);
              border-bottom: var(--bs-card-border-width) solid var(--bs-card-border-color);
            }
            .card-header:first-child {
              border-radius: var(--bs-card-inner-border-radius) var(--bs-card-inner-border-radius) 0 0;
            }

            .card-footer {
              padding: var(--bs-card-cap-padding-y) var(--bs-card-cap-padding-x);
              color: var(--bs-card-cap-color);
              background-color: var(--bs-card-cap-bg);
              border-top: var(--bs-card-border-width) solid var(--bs-card-border-color);
            }
            .card-footer:last-child {
              border-radius: 0 0 var(--bs-card-inner-border-radius) var(--bs-card-inner-border-radius);
            }

            .card-header-tabs {
              margin-right: calc(-0.5 * var(--bs-card-cap-padding-x));
              margin-bottom: calc(-1 * var(--bs-card-cap-padding-y));
              margin-left: calc(-0.5 * var(--bs-card-cap-padding-x));
              border-bottom: 0;
            }
            .card-header-tabs .nav-link.active {
              background-color: var(--bs-card-bg);
              border-bottom-color: var(--bs-card-bg);
            }

            .card-header-pills {
              margin-right: calc(-0.5 * var(--bs-card-cap-padding-x));
              margin-left: calc(-0.5 * var(--bs-card-cap-padding-x));
            }

            .card-img-overlay {
              position: absolute;
              top: 0;
              right: 0;
              bottom: 0;
              left: 0;
              padding: var(--bs-card-img-overlay-padding);
              border-radius: var(--bs-card-inner-border-radius);
            }

            .card-img,
            .card-img-top,
            .card-img-bottom {
              width: 100%;
            }

            .card-img,
            .card-img-top {
              border-top-left-radius: var(--bs-card-inner-border-radius);
              border-top-right-radius: var(--bs-card-inner-border-radius);
            }

            .card-img,
            .card-img-bottom {
              border-bottom-right-radius: var(--bs-card-inner-border-radius);
              border-bottom-left-radius: var(--bs-card-inner-border-radius);
            }

            .card-group > .card {
              margin-bottom: var(--bs-card-group-margin);
            }
            @media (min-width: 576px) {
              .card-group {
                display: flex;
                flex-flow: row wrap;
              }
              .card-group > .card {
                flex: 1 0 0%;
                margin-bottom: 0;
              }
              .card-group > .card + .card {
                margin-left: 0;
                border-left: 0;
              }
              .card-group > .card:not(:last-child) {
                border-top-right-radius: 0;
                border-bottom-right-radius: 0;
              }
              .card-group > .card:not(:last-child) .card-img-top,
              .card-group > .card:not(:last-child) .card-header {
                border-top-right-radius: 0;
              }
              .card-group > .card:not(:last-child) .card-img-bottom,
              .card-group > .card:not(:last-child) .card-footer {
                border-bottom-right-radius: 0;
              }
              .card-group > .card:not(:first-child) {
                border-top-left-radius: 0;
                border-bottom-left-radius: 0;
              }
              .card-group > .card:not(:first-child) .card-img-top,
              .card-group > .card:not(:first-child) .card-header {
                border-top-left-radius: 0;
              }
              .card-group > .card:not(:first-child) .card-img-bottom,
              .card-group > .card:not(:first-child) .card-footer {
                border-bottom-left-radius: 0;
              }
            }

            .accordion {
              --bs-accordion-color: var(--bs-body-color);
              --bs-accordion-bg: var(--bs-body-bg);
              --bs-accordion-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, border-radius 0.15s ease;
              --bs-accordion-border-color: var(--bs-border-color);
              --bs-accordion-border-width: var(--bs-border-width);
              --bs-accordion-border-radius: var(--bs-border-radius);
              --bs-accordion-inner-border-radius: calc(var(--bs-border-radius) - (var(--bs-border-width)));
              --bs-accordion-btn-padding-x: 1.25rem;
              --bs-accordion-btn-padding-y: 1rem;
              --bs-accordion-btn-color: var(--bs-body-color);
              --bs-accordion-btn-bg: var(--bs-accordion-bg);
              --bs-accordion-btn-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23212529'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
              --bs-accordion-btn-icon-width: 1.25rem;
              --bs-accordion-btn-icon-transform: rotate(-180deg);
              --bs-accordion-btn-icon-transition: transform 0.2s ease-in-out;
              --bs-accordion-btn-active-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23052c65'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
              --bs-accordion-btn-focus-border-color: #86b7fe;
              --bs-accordion-btn-focus-box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
              --bs-accordion-body-padding-x: 1.25rem;
              --bs-accordion-body-padding-y: 1rem;
              --bs-accordion-active-color: var(--bs-primary-text-emphasis);
              --bs-accordion-active-bg: var(--bs-primary-bg-subtle);
            }

            .accordion-button {
              position: relative;
              display: flex;
              align-items: center;
              width: 100%;
              padding: var(--bs-accordion-btn-padding-y) var(--bs-accordion-btn-padding-x);
              font-size: 1rem;
              color: var(--bs-accordion-btn-color);
              text-align: left;
              background-color: var(--bs-accordion-btn-bg);
              border: 0;
              border-radius: 0;
              overflow-anchor: none;
              transition: var(--bs-accordion-transition);
            }
            @media (prefers-reduced-motion: reduce) {
              .accordion-button {
                transition: none;
              }
            }
            .accordion-button:not(.collapsed) {
              color: var(--bs-accordion-active-color);
              background-color: var(--bs-accordion-active-bg);
              box-shadow: inset 0 calc(-1 * var(--bs-accordion-border-width)) 0 var(--bs-accordion-border-color);
            }
            .accordion-button:not(.collapsed)::after {
              background-image: var(--bs-accordion-btn-active-icon);
              transform: var(--bs-accordion-btn-icon-transform);
            }
            .accordion-button::after {
              flex-shrink: 0;
              width: var(--bs-accordion-btn-icon-width);
              height: var(--bs-accordion-btn-icon-width);
              margin-left: auto;
              content: "";
              background-image: var(--bs-accordion-btn-icon);
              background-repeat: no-repeat;
              background-size: var(--bs-accordion-btn-icon-width);
              transition: var(--bs-accordion-btn-icon-transition);
            }
            @media (prefers-reduced-motion: reduce) {
              .accordion-button::after {
                transition: none;
              }
            }
            .accordion-button:hover {
              z-index: 2;
            }
            .accordion-button:focus {
              z-index: 3;
              border-color: var(--bs-accordion-btn-focus-border-color);
              outline: 0;
              box-shadow: var(--bs-accordion-btn-focus-box-shadow);
            }

            .accordion-header {
              margin-bottom: 0;
            }

            .accordion-item {
              color: var(--bs-accordion-color);
              background-color: var(--bs-accordion-bg);
              border: var(--bs-accordion-border-width) solid var(--bs-accordion-border-color);
            }
            .accordion-item:first-of-type {
              border-top-left-radius: var(--bs-accordion-border-radius);
              border-top-right-radius: var(--bs-accordion-border-radius);
            }
            .accordion-item:first-of-type .accordion-button {
              border-top-left-radius: var(--bs-accordion-inner-border-radius);
              border-top-right-radius: var(--bs-accordion-inner-border-radius);
            }
            .accordion-item:not(:first-of-type) {
              border-top: 0;
            }
            .accordion-item:last-of-type {
              border-bottom-right-radius: var(--bs-accordion-border-radius);
              border-bottom-left-radius: var(--bs-accordion-border-radius);
            }
            .accordion-item:last-of-type .accordion-button.collapsed {
              border-bottom-right-radius: var(--bs-accordion-inner-border-radius);
              border-bottom-left-radius: var(--bs-accordion-inner-border-radius);
            }
            .accordion-item:last-of-type .accordion-collapse {
              border-bottom-right-radius: var(--bs-accordion-border-radius);
              border-bottom-left-radius: var(--bs-accordion-border-radius);
            }

            .accordion-body {
              padding: var(--bs-accordion-body-padding-y) var(--bs-accordion-body-padding-x);
            }

            .accordion-flush .accordion-collapse {
              border-width: 0;
            }
            .accordion-flush .accordion-item {
              border-right: 0;
              border-left: 0;
              border-radius: 0;
            }
            .accordion-flush .accordion-item:first-child {
              border-top: 0;
            }
            .accordion-flush .accordion-item:last-child {
              border-bottom: 0;
            }
            .accordion-flush .accordion-item .accordion-button, .accordion-flush .accordion-item .accordion-button.collapsed {
              border-radius: 0;
            }

            [data-bs-theme=dark] .accordion-button::after {
              --bs-accordion-btn-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%236ea8fe'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
              --bs-accordion-btn-active-icon: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%236ea8fe'%3e%3cpath fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
            }

            .breadcrumb {
              --bs-breadcrumb-padding-x: 0;
              --bs-breadcrumb-padding-y: 0;
              --bs-breadcrumb-margin-bottom: 1rem;
              --bs-breadcrumb-bg: ;
              --bs-breadcrumb-border-radius: ;
              --bs-breadcrumb-divider-color: var(--bs-secondary-color);
              --bs-breadcrumb-item-padding-x: 0.5rem;
              --bs-breadcrumb-item-active-color: var(--bs-secondary-color);
              display: flex;
              flex-wrap: wrap;
              padding: var(--bs-breadcrumb-padding-y) var(--bs-breadcrumb-padding-x);
              margin-bottom: var(--bs-breadcrumb-margin-bottom);
              font-size: var(--bs-breadcrumb-font-size);
              list-style: none;
              background-color: var(--bs-breadcrumb-bg);
              border-radius: var(--bs-breadcrumb-border-radius);
            }

            .breadcrumb-item + .breadcrumb-item {
              padding-left: var(--bs-breadcrumb-item-padding-x);
            }
            .breadcrumb-item + .breadcrumb-item::before {
              float: left;
              padding-right: var(--bs-breadcrumb-item-padding-x);
              color: var(--bs-breadcrumb-divider-color);
              content: var(--bs-breadcrumb-divider, "/") /* rtl: var(--bs-breadcrumb-divider, "/") */;
            }
            .breadcrumb-item.active {
              color: var(--bs-breadcrumb-item-active-color);
            }

            .pagination {
              --bs-pagination-padding-x: 0.75rem;
              --bs-pagination-padding-y: 0.375rem;
              --bs-pagination-font-size: 1rem;
              --bs-pagination-color: var(--bs-link-color);
              --bs-pagination-bg: var(--bs-body-bg);
              --bs-pagination-border-width: var(--bs-border-width);
              --bs-pagination-border-color: var(--bs-border-color);
              --bs-pagination-border-radius: var(--bs-border-radius);
              --bs-pagination-hover-color: var(--bs-link-hover-color);
              --bs-pagination-hover-bg: var(--bs-tertiary-bg);
              --bs-pagination-hover-border-color: var(--bs-border-color);
              --bs-pagination-focus-color: var(--bs-link-hover-color);
              --bs-pagination-focus-bg: var(--bs-secondary-bg);
              --bs-pagination-focus-box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
              --bs-pagination-active-color: #fff;
              --bs-pagination-active-bg: #0d6efd;
              --bs-pagination-active-border-color: #0d6efd;
              --bs-pagination-disabled-color: var(--bs-secondary-color);
              --bs-pagination-disabled-bg: var(--bs-secondary-bg);
              --bs-pagination-disabled-border-color: var(--bs-border-color);
              display: flex;
              padding-left: 0;
              list-style: none;
            }

            .page-link {
              position: relative;
              display: block;
              padding: var(--bs-pagination-padding-y) var(--bs-pagination-padding-x);
              font-size: var(--bs-pagination-font-size);
              color: var(--bs-pagination-color);
              text-decoration: none;
              background-color: var(--bs-pagination-bg);
              border: var(--bs-pagination-border-width) solid var(--bs-pagination-border-color);
              transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .page-link {
                transition: none;
              }
            }
            .page-link:hover {
              z-index: 2;
              color: var(--bs-pagination-hover-color);
              background-color: var(--bs-pagination-hover-bg);
              border-color: var(--bs-pagination-hover-border-color);
            }
            .page-link:focus {
              z-index: 3;
              color: var(--bs-pagination-focus-color);
              background-color: var(--bs-pagination-focus-bg);
              outline: 0;
              box-shadow: var(--bs-pagination-focus-box-shadow);
            }
            .page-link.active, .active > .page-link {
              z-index: 3;
              color: var(--bs-pagination-active-color);
              background-color: var(--bs-pagination-active-bg);
              border-color: var(--bs-pagination-active-border-color);
            }
            .page-link.disabled, .disabled > .page-link {
              color: var(--bs-pagination-disabled-color);
              pointer-events: none;
              background-color: var(--bs-pagination-disabled-bg);
              border-color: var(--bs-pagination-disabled-border-color);
            }

            .page-item:not(:first-child) .page-link {
              margin-left: calc(var(--bs-border-width) * -1);
            }
            .page-item:first-child .page-link {
              border-top-left-radius: var(--bs-pagination-border-radius);
              border-bottom-left-radius: var(--bs-pagination-border-radius);
            }
            .page-item:last-child .page-link {
              border-top-right-radius: var(--bs-pagination-border-radius);
              border-bottom-right-radius: var(--bs-pagination-border-radius);
            }

            .pagination-lg {
              --bs-pagination-padding-x: 1.5rem;
              --bs-pagination-padding-y: 0.75rem;
              --bs-pagination-font-size: 1.25rem;
              --bs-pagination-border-radius: 0.5rem;
            }

            .pagination-sm {
              --bs-pagination-padding-x: 0.5rem;
              --bs-pagination-padding-y: 0.25rem;
              --bs-pagination-font-size: 0.875rem;
              --bs-pagination-border-radius: 0.25rem;
            }

            .badge {
              --bs-badge-padding-x: 0.65em;
              --bs-badge-padding-y: 0.35em;
              --bs-badge-font-size: 0.75em;
              --bs-badge-font-weight: 700;
              --bs-badge-color: #fff;
              --bs-badge-border-radius: 0.375rem;
              display: inline-block;
              padding: var(--bs-badge-padding-y) var(--bs-badge-padding-x);
              font-size: var(--bs-badge-font-size);
              font-weight: var(--bs-badge-font-weight);
              line-height: 1;
              color: var(--bs-badge-color);
              text-align: center;
              white-space: nowrap;
              vertical-align: baseline;
              border-radius: var(--bs-badge-border-radius);
            }
            .badge:empty {
              display: none;
            }

            .btn .badge {
              position: relative;
              top: -1px;
            }

            .alert {
              --bs-alert-bg: transparent;
              --bs-alert-padding-x: 1rem;
              --bs-alert-padding-y: 1rem;
              --bs-alert-margin-bottom: 1rem;
              --bs-alert-color: inherit;
              --bs-alert-border-color: transparent;
              --bs-alert-border: var(--bs-border-width) solid var(--bs-alert-border-color);
              --bs-alert-border-radius: 0.375rem;
              --bs-alert-link-color: inherit;
              position: relative;
              padding: var(--bs-alert-padding-y) var(--bs-alert-padding-x);
              margin-bottom: var(--bs-alert-margin-bottom);
              color: var(--bs-alert-color);
              background-color: var(--bs-alert-bg);
              border: var(--bs-alert-border);
              border-radius: var(--bs-alert-border-radius);
            }

            .alert-heading {
              color: inherit;
            }

            .alert-link {
              font-weight: 700;
              color: var(--bs-alert-link-color);
            }

            .alert-dismissible {
              padding-right: 3rem;
            }
            .alert-dismissible .btn-close {
              position: absolute;
              top: 0;
              right: 0;
              z-index: 2;
              padding: 1.25rem 1rem;
            }

            .alert-primary {
              --bs-alert-color: var(--bs-primary-text-emphasis);
              --bs-alert-bg: var(--bs-primary-bg-subtle);
              --bs-alert-border-color: var(--bs-primary-border-subtle);
              --bs-alert-link-color: var(--bs-primary-text-emphasis);
            }

            .alert-secondary {
              --bs-alert-color: var(--bs-secondary-text-emphasis);
              --bs-alert-bg: var(--bs-secondary-bg-subtle);
              --bs-alert-border-color: var(--bs-secondary-border-subtle);
              --bs-alert-link-color: var(--bs-secondary-text-emphasis);
            }

            .alert-success {
              --bs-alert-color: var(--bs-success-text-emphasis);
              --bs-alert-bg: var(--bs-success-bg-subtle);
              --bs-alert-border-color: var(--bs-success-border-subtle);
              --bs-alert-link-color: var(--bs-success-text-emphasis);
            }

            .alert-info {
              --bs-alert-color: var(--bs-info-text-emphasis);
              --bs-alert-bg: var(--bs-info-bg-subtle);
              --bs-alert-border-color: var(--bs-info-border-subtle);
              --bs-alert-link-color: var(--bs-info-text-emphasis);
            }

            .alert-warning {
              --bs-alert-color: var(--bs-warning-text-emphasis);
              --bs-alert-bg: var(--bs-warning-bg-subtle);
              --bs-alert-border-color: var(--bs-warning-border-subtle);
              --bs-alert-link-color: var(--bs-warning-text-emphasis);
            }

            .alert-danger {
              --bs-alert-color: var(--bs-danger-text-emphasis);
              --bs-alert-bg: var(--bs-danger-bg-subtle);
              --bs-alert-border-color: var(--bs-danger-border-subtle);
              --bs-alert-link-color: var(--bs-danger-text-emphasis);
            }

            .alert-light {
              --bs-alert-color: var(--bs-light-text-emphasis);
              --bs-alert-bg: var(--bs-light-bg-subtle);
              --bs-alert-border-color: var(--bs-light-border-subtle);
              --bs-alert-link-color: var(--bs-light-text-emphasis);
            }

            .alert-dark {
              --bs-alert-color: var(--bs-dark-text-emphasis);
              --bs-alert-bg: var(--bs-dark-bg-subtle);
              --bs-alert-border-color: var(--bs-dark-border-subtle);
              --bs-alert-link-color: var(--bs-dark-text-emphasis);
            }

            @keyframes progress-bar-stripes {
              0% {
                background-position-x: 1rem;
              }
            }
            .progress,
            .progress-stacked {
              --bs-progress-height: 1rem;
              --bs-progress-font-size: 0.75rem;
              --bs-progress-bg: var(--bs-secondary-bg);
              --bs-progress-border-radius: var(--bs-border-radius);
              --bs-progress-box-shadow: var(--bs-box-shadow-inset);
              --bs-progress-bar-color: #fff;
              --bs-progress-bar-bg: #0d6efd;
              --bs-progress-bar-transition: width 0.6s ease;
              display: flex;
              height: var(--bs-progress-height);
              overflow: hidden;
              font-size: var(--bs-progress-font-size);
              background-color: var(--bs-progress-bg);
              border-radius: var(--bs-progress-border-radius);
            }

            .progress-bar {
              display: flex;
              flex-direction: column;
              justify-content: center;
              overflow: hidden;
              color: var(--bs-progress-bar-color);
              text-align: center;
              white-space: nowrap;
              background-color: var(--bs-progress-bar-bg);
              transition: var(--bs-progress-bar-transition);
            }
            @media (prefers-reduced-motion: reduce) {
              .progress-bar {
                transition: none;
              }
            }

            .progress-bar-striped {
              background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
              background-size: var(--bs-progress-height) var(--bs-progress-height);
            }

            .progress-stacked > .progress {
              overflow: visible;
            }

            .progress-stacked > .progress > .progress-bar {
              width: 100%;
            }

            .progress-bar-animated {
              animation: 1s linear infinite progress-bar-stripes;
            }
            @media (prefers-reduced-motion: reduce) {
              .progress-bar-animated {
                animation: none;
              }
            }

            .list-group {
              --bs-list-group-color: var(--bs-body-color);
              --bs-list-group-bg: var(--bs-body-bg);
              --bs-list-group-border-color: var(--bs-border-color);
              --bs-list-group-border-width: var(--bs-border-width);
              --bs-list-group-border-radius: var(--bs-border-radius);
              --bs-list-group-item-padding-x: 1rem;
              --bs-list-group-item-padding-y: 0.5rem;
              --bs-list-group-action-color: var(--bs-secondary-color);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-tertiary-bg);
              --bs-list-group-action-active-color: var(--bs-body-color);
              --bs-list-group-action-active-bg: var(--bs-secondary-bg);
              --bs-list-group-disabled-color: var(--bs-secondary-color);
              --bs-list-group-disabled-bg: var(--bs-body-bg);
              --bs-list-group-active-color: #fff;
              --bs-list-group-active-bg: #0d6efd;
              --bs-list-group-active-border-color: #0d6efd;
              display: flex;
              flex-direction: column;
              padding-left: 0;
              margin-bottom: 0;
              border-radius: var(--bs-list-group-border-radius);
            }

            .list-group-numbered {
              list-style-type: none;
              counter-reset: section;
            }
            .list-group-numbered > .list-group-item::before {
              content: counters(section, ".") ". ";
              counter-increment: section;
            }

            .list-group-item-action {
              width: 100%;
              color: var(--bs-list-group-action-color);
              text-align: inherit;
            }
            .list-group-item-action:hover, .list-group-item-action:focus {
              z-index: 1;
              color: var(--bs-list-group-action-hover-color);
              text-decoration: none;
              background-color: var(--bs-list-group-action-hover-bg);
            }
            .list-group-item-action:active {
              color: var(--bs-list-group-action-active-color);
              background-color: var(--bs-list-group-action-active-bg);
            }

            .list-group-item {
              position: relative;
              display: block;
              padding: var(--bs-list-group-item-padding-y) var(--bs-list-group-item-padding-x);
              color: var(--bs-list-group-color);
              text-decoration: none;
              background-color: var(--bs-list-group-bg);
              border: var(--bs-list-group-border-width) solid var(--bs-list-group-border-color);
            }
            .list-group-item:first-child {
              border-top-left-radius: inherit;
              border-top-right-radius: inherit;
            }
            .list-group-item:last-child {
              border-bottom-right-radius: inherit;
              border-bottom-left-radius: inherit;
            }
            .list-group-item.disabled, .list-group-item:disabled {
              color: var(--bs-list-group-disabled-color);
              pointer-events: none;
              background-color: var(--bs-list-group-disabled-bg);
            }
            .list-group-item.active {
              z-index: 2;
              color: var(--bs-list-group-active-color);
              background-color: var(--bs-list-group-active-bg);
              border-color: var(--bs-list-group-active-border-color);
            }
            .list-group-item + .list-group-item {
              border-top-width: 0;
            }
            .list-group-item + .list-group-item.active {
              margin-top: calc(-1 * var(--bs-list-group-border-width));
              border-top-width: var(--bs-list-group-border-width);
            }

            .list-group-horizontal {
              flex-direction: row;
            }
            .list-group-horizontal > .list-group-item:first-child:not(:last-child) {
              border-bottom-left-radius: var(--bs-list-group-border-radius);
              border-top-right-radius: 0;
            }
            .list-group-horizontal > .list-group-item:last-child:not(:first-child) {
              border-top-right-radius: var(--bs-list-group-border-radius);
              border-bottom-left-radius: 0;
            }
            .list-group-horizontal > .list-group-item.active {
              margin-top: 0;
            }
            .list-group-horizontal > .list-group-item + .list-group-item {
              border-top-width: var(--bs-list-group-border-width);
              border-left-width: 0;
            }
            .list-group-horizontal > .list-group-item + .list-group-item.active {
              margin-left: calc(-1 * var(--bs-list-group-border-width));
              border-left-width: var(--bs-list-group-border-width);
            }

            @media (min-width: 576px) {
              .list-group-horizontal-sm {
                flex-direction: row;
              }
              .list-group-horizontal-sm > .list-group-item:first-child:not(:last-child) {
                border-bottom-left-radius: var(--bs-list-group-border-radius);
                border-top-right-radius: 0;
              }
              .list-group-horizontal-sm > .list-group-item:last-child:not(:first-child) {
                border-top-right-radius: var(--bs-list-group-border-radius);
                border-bottom-left-radius: 0;
              }
              .list-group-horizontal-sm > .list-group-item.active {
                margin-top: 0;
              }
              .list-group-horizontal-sm > .list-group-item + .list-group-item {
                border-top-width: var(--bs-list-group-border-width);
                border-left-width: 0;
              }
              .list-group-horizontal-sm > .list-group-item + .list-group-item.active {
                margin-left: calc(-1 * var(--bs-list-group-border-width));
                border-left-width: var(--bs-list-group-border-width);
              }
            }
            @media (min-width: 768px) {
              .list-group-horizontal-md {
                flex-direction: row;
              }
              .list-group-horizontal-md > .list-group-item:first-child:not(:last-child) {
                border-bottom-left-radius: var(--bs-list-group-border-radius);
                border-top-right-radius: 0;
              }
              .list-group-horizontal-md > .list-group-item:last-child:not(:first-child) {
                border-top-right-radius: var(--bs-list-group-border-radius);
                border-bottom-left-radius: 0;
              }
              .list-group-horizontal-md > .list-group-item.active {
                margin-top: 0;
              }
              .list-group-horizontal-md > .list-group-item + .list-group-item {
                border-top-width: var(--bs-list-group-border-width);
                border-left-width: 0;
              }
              .list-group-horizontal-md > .list-group-item + .list-group-item.active {
                margin-left: calc(-1 * var(--bs-list-group-border-width));
                border-left-width: var(--bs-list-group-border-width);
              }
            }
            @media (min-width: 992px) {
              .list-group-horizontal-lg {
                flex-direction: row;
              }
              .list-group-horizontal-lg > .list-group-item:first-child:not(:last-child) {
                border-bottom-left-radius: var(--bs-list-group-border-radius);
                border-top-right-radius: 0;
              }
              .list-group-horizontal-lg > .list-group-item:last-child:not(:first-child) {
                border-top-right-radius: var(--bs-list-group-border-radius);
                border-bottom-left-radius: 0;
              }
              .list-group-horizontal-lg > .list-group-item.active {
                margin-top: 0;
              }
              .list-group-horizontal-lg > .list-group-item + .list-group-item {
                border-top-width: var(--bs-list-group-border-width);
                border-left-width: 0;
              }
              .list-group-horizontal-lg > .list-group-item + .list-group-item.active {
                margin-left: calc(-1 * var(--bs-list-group-border-width));
                border-left-width: var(--bs-list-group-border-width);
              }
            }
            @media (min-width: 1200px) {
              .list-group-horizontal-xl {
                flex-direction: row;
              }
              .list-group-horizontal-xl > .list-group-item:first-child:not(:last-child) {
                border-bottom-left-radius: var(--bs-list-group-border-radius);
                border-top-right-radius: 0;
              }
              .list-group-horizontal-xl > .list-group-item:last-child:not(:first-child) {
                border-top-right-radius: var(--bs-list-group-border-radius);
                border-bottom-left-radius: 0;
              }
              .list-group-horizontal-xl > .list-group-item.active {
                margin-top: 0;
              }
              .list-group-horizontal-xl > .list-group-item + .list-group-item {
                border-top-width: var(--bs-list-group-border-width);
                border-left-width: 0;
              }
              .list-group-horizontal-xl > .list-group-item + .list-group-item.active {
                margin-left: calc(-1 * var(--bs-list-group-border-width));
                border-left-width: var(--bs-list-group-border-width);
              }
            }
            @media (min-width: 1400px) {
              .list-group-horizontal-xxl {
                flex-direction: row;
              }
              .list-group-horizontal-xxl > .list-group-item:first-child:not(:last-child) {
                border-bottom-left-radius: var(--bs-list-group-border-radius);
                border-top-right-radius: 0;
              }
              .list-group-horizontal-xxl > .list-group-item:last-child:not(:first-child) {
                border-top-right-radius: var(--bs-list-group-border-radius);
                border-bottom-left-radius: 0;
              }
              .list-group-horizontal-xxl > .list-group-item.active {
                margin-top: 0;
              }
              .list-group-horizontal-xxl > .list-group-item + .list-group-item {
                border-top-width: var(--bs-list-group-border-width);
                border-left-width: 0;
              }
              .list-group-horizontal-xxl > .list-group-item + .list-group-item.active {
                margin-left: calc(-1 * var(--bs-list-group-border-width));
                border-left-width: var(--bs-list-group-border-width);
              }
            }
            .list-group-flush {
              border-radius: 0;
            }
            .list-group-flush > .list-group-item {
              border-width: 0 0 var(--bs-list-group-border-width);
            }
            .list-group-flush > .list-group-item:last-child {
              border-bottom-width: 0;
            }

            .list-group-item-primary {
              --bs-list-group-color: var(--bs-primary-text-emphasis);
              --bs-list-group-bg: var(--bs-primary-bg-subtle);
              --bs-list-group-border-color: var(--bs-primary-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-primary-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-primary-border-subtle);
              --bs-list-group-active-color: var(--bs-primary-bg-subtle);
              --bs-list-group-active-bg: var(--bs-primary-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-primary-text-emphasis);
            }

            .list-group-item-secondary {
              --bs-list-group-color: var(--bs-secondary-text-emphasis);
              --bs-list-group-bg: var(--bs-secondary-bg-subtle);
              --bs-list-group-border-color: var(--bs-secondary-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-secondary-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-secondary-border-subtle);
              --bs-list-group-active-color: var(--bs-secondary-bg-subtle);
              --bs-list-group-active-bg: var(--bs-secondary-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-secondary-text-emphasis);
            }

            .list-group-item-success {
              --bs-list-group-color: var(--bs-success-text-emphasis);
              --bs-list-group-bg: var(--bs-success-bg-subtle);
              --bs-list-group-border-color: var(--bs-success-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-success-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-success-border-subtle);
              --bs-list-group-active-color: var(--bs-success-bg-subtle);
              --bs-list-group-active-bg: var(--bs-success-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-success-text-emphasis);
            }

            .list-group-item-info {
              --bs-list-group-color: var(--bs-info-text-emphasis);
              --bs-list-group-bg: var(--bs-info-bg-subtle);
              --bs-list-group-border-color: var(--bs-info-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-info-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-info-border-subtle);
              --bs-list-group-active-color: var(--bs-info-bg-subtle);
              --bs-list-group-active-bg: var(--bs-info-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-info-text-emphasis);
            }

            .list-group-item-warning {
              --bs-list-group-color: var(--bs-warning-text-emphasis);
              --bs-list-group-bg: var(--bs-warning-bg-subtle);
              --bs-list-group-border-color: var(--bs-warning-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-warning-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-warning-border-subtle);
              --bs-list-group-active-color: var(--bs-warning-bg-subtle);
              --bs-list-group-active-bg: var(--bs-warning-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-warning-text-emphasis);
            }

            .list-group-item-danger {
              --bs-list-group-color: var(--bs-danger-text-emphasis);
              --bs-list-group-bg: var(--bs-danger-bg-subtle);
              --bs-list-group-border-color: var(--bs-danger-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-danger-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-danger-border-subtle);
              --bs-list-group-active-color: var(--bs-danger-bg-subtle);
              --bs-list-group-active-bg: var(--bs-danger-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-danger-text-emphasis);
            }

            .list-group-item-light {
              --bs-list-group-color: var(--bs-light-text-emphasis);
              --bs-list-group-bg: var(--bs-light-bg-subtle);
              --bs-list-group-border-color: var(--bs-light-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-light-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-light-border-subtle);
              --bs-list-group-active-color: var(--bs-light-bg-subtle);
              --bs-list-group-active-bg: var(--bs-light-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-light-text-emphasis);
            }

            .list-group-item-dark {
              --bs-list-group-color: var(--bs-dark-text-emphasis);
              --bs-list-group-bg: var(--bs-dark-bg-subtle);
              --bs-list-group-border-color: var(--bs-dark-border-subtle);
              --bs-list-group-action-hover-color: var(--bs-emphasis-color);
              --bs-list-group-action-hover-bg: var(--bs-dark-border-subtle);
              --bs-list-group-action-active-color: var(--bs-emphasis-color);
              --bs-list-group-action-active-bg: var(--bs-dark-border-subtle);
              --bs-list-group-active-color: var(--bs-dark-bg-subtle);
              --bs-list-group-active-bg: var(--bs-dark-text-emphasis);
              --bs-list-group-active-border-color: var(--bs-dark-text-emphasis);
            }

            .btn-close {
              --bs-btn-close-color: #000;
              --bs-btn-close-bg: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z'/%3e%3c/svg%3e");
              --bs-btn-close-opacity: 0.5;
              --bs-btn-close-hover-opacity: 0.75;
              --bs-btn-close-focus-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
              --bs-btn-close-focus-opacity: 1;
              --bs-btn-close-disabled-opacity: 0.25;
              --bs-btn-close-white-filter: invert(1) grayscale(100%) brightness(200%);
              box-sizing: content-box;
              width: 1em;
              height: 1em;
              padding: 0.25em 0.25em;
              color: var(--bs-btn-close-color);
              background: transparent var(--bs-btn-close-bg) center/1em auto no-repeat;
              border: 0;
              border-radius: 0.375rem;
              opacity: var(--bs-btn-close-opacity);
            }
            .btn-close:hover {
              color: var(--bs-btn-close-color);
              text-decoration: none;
              opacity: var(--bs-btn-close-hover-opacity);
            }
            .btn-close:focus {
              outline: 0;
              box-shadow: var(--bs-btn-close-focus-shadow);
              opacity: var(--bs-btn-close-focus-opacity);
            }
            .btn-close:disabled, .btn-close.disabled {
              pointer-events: none;
              -webkit-user-select: none;
              -moz-user-select: none;
              user-select: none;
              opacity: var(--bs-btn-close-disabled-opacity);
            }

            .btn-close-white {
              filter: var(--bs-btn-close-white-filter);
            }

            [data-bs-theme=dark] .btn-close {
              filter: var(--bs-btn-close-white-filter);
            }

            .toast {
              --bs-toast-zindex: 1090;
              --bs-toast-padding-x: 0.75rem;
              --bs-toast-padding-y: 0.5rem;
              --bs-toast-spacing: 1.5rem;
              --bs-toast-max-width: 350px;
              --bs-toast-font-size: 0.875rem;
              --bs-toast-color: ;
              --bs-toast-bg: rgba(var(--bs-body-bg-rgb), 0.85);
              --bs-toast-border-width: var(--bs-border-width);
              --bs-toast-border-color: var(--bs-border-color-translucent);
              --bs-toast-border-radius: var(--bs-border-radius);
              --bs-toast-box-shadow: var(--bs-box-shadow);
              --bs-toast-header-color: var(--bs-secondary-color);
              --bs-toast-header-bg: rgba(var(--bs-body-bg-rgb), 0.85);
              --bs-toast-header-border-color: var(--bs-border-color-translucent);
              width: var(--bs-toast-max-width);
              max-width: 100%;
              font-size: var(--bs-toast-font-size);
              color: var(--bs-toast-color);
              pointer-events: auto;
              background-color: var(--bs-toast-bg);
              background-clip: padding-box;
              border: var(--bs-toast-border-width) solid var(--bs-toast-border-color);
              box-shadow: var(--bs-toast-box-shadow);
              border-radius: var(--bs-toast-border-radius);
            }
            .toast.showing {
              opacity: 0;
            }
            .toast:not(.show) {
              display: none;
            }

            .toast-container {
              --bs-toast-zindex: 1090;
              position: absolute;
              z-index: var(--bs-toast-zindex);
              width: -webkit-max-content;
              width: -moz-max-content;
              width: max-content;
              max-width: 100%;
              pointer-events: none;
            }
            .toast-container > :not(:last-child) {
              margin-bottom: var(--bs-toast-spacing);
            }

            .toast-header {
              display: flex;
              align-items: center;
              padding: var(--bs-toast-padding-y) var(--bs-toast-padding-x);
              color: var(--bs-toast-header-color);
              background-color: var(--bs-toast-header-bg);
              background-clip: padding-box;
              border-bottom: var(--bs-toast-border-width) solid var(--bs-toast-header-border-color);
              border-top-left-radius: calc(var(--bs-toast-border-radius) - var(--bs-toast-border-width));
              border-top-right-radius: calc(var(--bs-toast-border-radius) - var(--bs-toast-border-width));
            }
            .toast-header .btn-close {
              margin-right: calc(-0.5 * var(--bs-toast-padding-x));
              margin-left: var(--bs-toast-padding-x);
            }

            .toast-body {
              padding: var(--bs-toast-padding-x);
              word-wrap: break-word;
            }

            .modal {
              --bs-modal-zindex: 1055;
              --bs-modal-width: 500px;
              --bs-modal-padding: 1rem;
              --bs-modal-margin: 0.5rem;
              --bs-modal-color: ;
              --bs-modal-bg: var(--bs-body-bg);
              --bs-modal-border-color: var(--bs-border-color-translucent);
              --bs-modal-border-width: var(--bs-border-width);
              --bs-modal-border-radius: var(--bs-border-radius-lg);
              --bs-modal-box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
              --bs-modal-inner-border-radius: calc(var(--bs-border-radius-lg) - (var(--bs-border-width)));
              --bs-modal-header-padding-x: 1rem;
              --bs-modal-header-padding-y: 1rem;
              --bs-modal-header-padding: 1rem 1rem;
              --bs-modal-header-border-color: var(--bs-border-color);
              --bs-modal-header-border-width: var(--bs-border-width);
              --bs-modal-title-line-height: 1.5;
              --bs-modal-footer-gap: 0.5rem;
              --bs-modal-footer-bg: ;
              --bs-modal-footer-border-color: var(--bs-border-color);
              --bs-modal-footer-border-width: var(--bs-border-width);
              position: fixed;
              top: 0;
              left: 0;
              z-index: var(--bs-modal-zindex);
              display: none;
              width: 100%;
              height: 100%;
              overflow-x: hidden;
              overflow-y: auto;
              outline: 0;
            }

            .modal-dialog {
              position: relative;
              width: auto;
              margin: var(--bs-modal-margin);
              pointer-events: none;
            }
            .modal.fade .modal-dialog {
              transition: transform 0.3s ease-out;
              transform: translate(0, -50px);
            }
            @media (prefers-reduced-motion: reduce) {
              .modal.fade .modal-dialog {
                transition: none;
              }
            }
            .modal.show .modal-dialog {
              transform: none;
            }
            .modal.modal-static .modal-dialog {
              transform: scale(1.02);
            }

            .modal-dialog-scrollable {
              height: calc(100% - var(--bs-modal-margin) * 2);
            }
            .modal-dialog-scrollable .modal-content {
              max-height: 100%;
              overflow: hidden;
            }
            .modal-dialog-scrollable .modal-body {
              overflow-y: auto;
            }

            .modal-dialog-centered {
              display: flex;
              align-items: center;
              min-height: calc(100% - var(--bs-modal-margin) * 2);
            }

            .modal-content {
              position: relative;
              display: flex;
              flex-direction: column;
              width: 100%;
              color: var(--bs-modal-color);
              pointer-events: auto;
              background-color: var(--bs-modal-bg);
              background-clip: padding-box;
              border: var(--bs-modal-border-width) solid var(--bs-modal-border-color);
              border-radius: var(--bs-modal-border-radius);
              outline: 0;
            }

            .modal-backdrop {
              --bs-backdrop-zindex: 1050;
              --bs-backdrop-bg: #000;
              --bs-backdrop-opacity: 0.5;
              position: fixed;
              top: 0;
              left: 0;
              z-index: var(--bs-backdrop-zindex);
              width: 100vw;
              height: 100vh;
              background-color: var(--bs-backdrop-bg);
            }
            .modal-backdrop.fade {
              opacity: 0;
            }
            .modal-backdrop.show {
              opacity: var(--bs-backdrop-opacity);
            }

            .modal-header {
              display: flex;
              flex-shrink: 0;
              align-items: center;
              justify-content: space-between;
              padding: var(--bs-modal-header-padding);
              border-bottom: var(--bs-modal-header-border-width) solid var(--bs-modal-header-border-color);
              border-top-left-radius: var(--bs-modal-inner-border-radius);
              border-top-right-radius: var(--bs-modal-inner-border-radius);
            }
            .modal-header .btn-close {
              padding: calc(var(--bs-modal-header-padding-y) * 0.5) calc(var(--bs-modal-header-padding-x) * 0.5);
              margin: calc(-0.5 * var(--bs-modal-header-padding-y)) calc(-0.5 * var(--bs-modal-header-padding-x)) calc(-0.5 * var(--bs-modal-header-padding-y)) auto;
            }

            .modal-title {
              margin-bottom: 0;
              line-height: var(--bs-modal-title-line-height);
            }

            .modal-body {
              position: relative;
              flex: 1 1 auto;
              padding: var(--bs-modal-padding);
            }

            .modal-footer {
              display: flex;
              flex-shrink: 0;
              flex-wrap: wrap;
              align-items: center;
              justify-content: flex-end;
              padding: calc(var(--bs-modal-padding) - var(--bs-modal-footer-gap) * 0.5);
              background-color: var(--bs-modal-footer-bg);
              border-top: var(--bs-modal-footer-border-width) solid var(--bs-modal-footer-border-color);
              border-bottom-right-radius: var(--bs-modal-inner-border-radius);
              border-bottom-left-radius: var(--bs-modal-inner-border-radius);
            }
            .modal-footer > * {
              margin: calc(var(--bs-modal-footer-gap) * 0.5);
            }

            @media (min-width: 576px) {
              .modal {
                --bs-modal-margin: 1.75rem;
                --bs-modal-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
              }
              .modal-dialog {
                max-width: var(--bs-modal-width);
                margin-right: auto;
                margin-left: auto;
              }
              .modal-sm {
                --bs-modal-width: 300px;
              }
            }
            @media (min-width: 992px) {
              .modal-lg,
              .modal-xl {
                --bs-modal-width: 800px;
              }
            }
            @media (min-width: 1200px) {
              .modal-xl {
                --bs-modal-width: 1140px;
              }
            }
            .modal-fullscreen {
              width: 100vw;
              max-width: none;
              height: 100%;
              margin: 0;
            }
            .modal-fullscreen .modal-content {
              height: 100%;
              border: 0;
              border-radius: 0;
            }
            .modal-fullscreen .modal-header,
            .modal-fullscreen .modal-footer {
              border-radius: 0;
            }
            .modal-fullscreen .modal-body {
              overflow-y: auto;
            }

            @media (max-width: 575.98px) {
              .modal-fullscreen-sm-down {
                width: 100vw;
                max-width: none;
                height: 100%;
                margin: 0;
              }
              .modal-fullscreen-sm-down .modal-content {
                height: 100%;
                border: 0;
                border-radius: 0;
              }
              .modal-fullscreen-sm-down .modal-header,
              .modal-fullscreen-sm-down .modal-footer {
                border-radius: 0;
              }
              .modal-fullscreen-sm-down .modal-body {
                overflow-y: auto;
              }
            }
            @media (max-width: 767.98px) {
              .modal-fullscreen-md-down {
                width: 100vw;
                max-width: none;
                height: 100%;
                margin: 0;
              }
              .modal-fullscreen-md-down .modal-content {
                height: 100%;
                border: 0;
                border-radius: 0;
              }
              .modal-fullscreen-md-down .modal-header,
              .modal-fullscreen-md-down .modal-footer {
                border-radius: 0;
              }
              .modal-fullscreen-md-down .modal-body {
                overflow-y: auto;
              }
            }
            @media (max-width: 991.98px) {
              .modal-fullscreen-lg-down {
                width: 100vw;
                max-width: none;
                height: 100%;
                margin: 0;
              }
              .modal-fullscreen-lg-down .modal-content {
                height: 100%;
                border: 0;
                border-radius: 0;
              }
              .modal-fullscreen-lg-down .modal-header,
              .modal-fullscreen-lg-down .modal-footer {
                border-radius: 0;
              }
              .modal-fullscreen-lg-down .modal-body {
                overflow-y: auto;
              }
            }
            @media (max-width: 1199.98px) {
              .modal-fullscreen-xl-down {
                width: 100vw;
                max-width: none;
                height: 100%;
                margin: 0;
              }
              .modal-fullscreen-xl-down .modal-content {
                height: 100%;
                border: 0;
                border-radius: 0;
              }
              .modal-fullscreen-xl-down .modal-header,
              .modal-fullscreen-xl-down .modal-footer {
                border-radius: 0;
              }
              .modal-fullscreen-xl-down .modal-body {
                overflow-y: auto;
              }
            }
            @media (max-width: 1399.98px) {
              .modal-fullscreen-xxl-down {
                width: 100vw;
                max-width: none;
                height: 100%;
                margin: 0;
              }
              .modal-fullscreen-xxl-down .modal-content {
                height: 100%;
                border: 0;
                border-radius: 0;
              }
              .modal-fullscreen-xxl-down .modal-header,
              .modal-fullscreen-xxl-down .modal-footer {
                border-radius: 0;
              }
              .modal-fullscreen-xxl-down .modal-body {
                overflow-y: auto;
              }
            }
            .tooltip {
              --bs-tooltip-zindex: 1080;
              --bs-tooltip-max-width: 200px;
              --bs-tooltip-padding-x: 0.5rem;
              --bs-tooltip-padding-y: 0.25rem;
              --bs-tooltip-margin: ;
              --bs-tooltip-font-size: 0.875rem;
              --bs-tooltip-color: var(--bs-body-bg);
              --bs-tooltip-bg: var(--bs-emphasis-color);
              --bs-tooltip-border-radius: var(--bs-border-radius);
              --bs-tooltip-opacity: 0.9;
              --bs-tooltip-arrow-width: 0.8rem;
              --bs-tooltip-arrow-height: 0.4rem;
              z-index: var(--bs-tooltip-zindex);
              display: block;
              padding: var(--bs-tooltip-arrow-height);
              margin: var(--bs-tooltip-margin);
              font-family: var(--bs-font-sans-serif);
              font-style: normal;
              font-weight: 400;
              line-height: 1.5;
              text-align: left;
              text-align: start;
              text-decoration: none;
              text-shadow: none;
              text-transform: none;
              letter-spacing: normal;
              word-break: normal;
              white-space: normal;
              word-spacing: normal;
              line-break: auto;
              font-size: var(--bs-tooltip-font-size);
              word-wrap: break-word;
              opacity: 0;
            }
            .tooltip.show {
              opacity: var(--bs-tooltip-opacity);
            }
            .tooltip .tooltip-arrow {
              display: block;
              width: var(--bs-tooltip-arrow-width);
              height: var(--bs-tooltip-arrow-height);
            }
            .tooltip .tooltip-arrow::before {
              position: absolute;
              content: "";
              border-color: transparent;
              border-style: solid;
            }

            .bs-tooltip-top .tooltip-arrow, .bs-tooltip-auto[data-popper-placement^=top] .tooltip-arrow {
              bottom: 0;
            }
            .bs-tooltip-top .tooltip-arrow::before, .bs-tooltip-auto[data-popper-placement^=top] .tooltip-arrow::before {
              top: -1px;
              border-width: var(--bs-tooltip-arrow-height) calc(var(--bs-tooltip-arrow-width) * 0.5) 0;
              border-top-color: var(--bs-tooltip-bg);
            }

            /* rtl:begin:ignore */
            .bs-tooltip-end .tooltip-arrow, .bs-tooltip-auto[data-popper-placement^=right] .tooltip-arrow {
              left: 0;
              width: var(--bs-tooltip-arrow-height);
              height: var(--bs-tooltip-arrow-width);
            }
            .bs-tooltip-end .tooltip-arrow::before, .bs-tooltip-auto[data-popper-placement^=right] .tooltip-arrow::before {
              right: -1px;
              border-width: calc(var(--bs-tooltip-arrow-width) * 0.5) var(--bs-tooltip-arrow-height) calc(var(--bs-tooltip-arrow-width) * 0.5) 0;
              border-right-color: var(--bs-tooltip-bg);
            }

            /* rtl:end:ignore */
            .bs-tooltip-bottom .tooltip-arrow, .bs-tooltip-auto[data-popper-placement^=bottom] .tooltip-arrow {
              top: 0;
            }
            .bs-tooltip-bottom .tooltip-arrow::before, .bs-tooltip-auto[data-popper-placement^=bottom] .tooltip-arrow::before {
              bottom: -1px;
              border-width: 0 calc(var(--bs-tooltip-arrow-width) * 0.5) var(--bs-tooltip-arrow-height);
              border-bottom-color: var(--bs-tooltip-bg);
            }

            /* rtl:begin:ignore */
            .bs-tooltip-start .tooltip-arrow, .bs-tooltip-auto[data-popper-placement^=left] .tooltip-arrow {
              right: 0;
              width: var(--bs-tooltip-arrow-height);
              height: var(--bs-tooltip-arrow-width);
            }
            .bs-tooltip-start .tooltip-arrow::before, .bs-tooltip-auto[data-popper-placement^=left] .tooltip-arrow::before {
              left: -1px;
              border-width: calc(var(--bs-tooltip-arrow-width) * 0.5) 0 calc(var(--bs-tooltip-arrow-width) * 0.5) var(--bs-tooltip-arrow-height);
              border-left-color: var(--bs-tooltip-bg);
            }

            /* rtl:end:ignore */
            .tooltip-inner {
              max-width: var(--bs-tooltip-max-width);
              padding: var(--bs-tooltip-padding-y) var(--bs-tooltip-padding-x);
              color: var(--bs-tooltip-color);
              text-align: center;
              background-color: var(--bs-tooltip-bg);
              border-radius: var(--bs-tooltip-border-radius);
            }

            .popover {
              --bs-popover-zindex: 1070;
              --bs-popover-max-width: 276px;
              --bs-popover-font-size: 0.875rem;
              --bs-popover-bg: var(--bs-body-bg);
              --bs-popover-border-width: var(--bs-border-width);
              --bs-popover-border-color: var(--bs-border-color-translucent);
              --bs-popover-border-radius: var(--bs-border-radius-lg);
              --bs-popover-inner-border-radius: calc(var(--bs-border-radius-lg) - var(--bs-border-width));
              --bs-popover-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
              --bs-popover-header-padding-x: 1rem;
              --bs-popover-header-padding-y: 0.5rem;
              --bs-popover-header-font-size: 1rem;
              --bs-popover-header-color: ;
              --bs-popover-header-bg: var(--bs-secondary-bg);
              --bs-popover-body-padding-x: 1rem;
              --bs-popover-body-padding-y: 1rem;
              --bs-popover-body-color: var(--bs-body-color);
              --bs-popover-arrow-width: 1rem;
              --bs-popover-arrow-height: 0.5rem;
              --bs-popover-arrow-border: var(--bs-popover-border-color);
              z-index: var(--bs-popover-zindex);
              display: block;
              max-width: var(--bs-popover-max-width);
              font-family: var(--bs-font-sans-serif);
              font-style: normal;
              font-weight: 400;
              line-height: 1.5;
              text-align: left;
              text-align: start;
              text-decoration: none;
              text-shadow: none;
              text-transform: none;
              letter-spacing: normal;
              word-break: normal;
              white-space: normal;
              word-spacing: normal;
              line-break: auto;
              font-size: var(--bs-popover-font-size);
              word-wrap: break-word;
              background-color: var(--bs-popover-bg);
              background-clip: padding-box;
              border: var(--bs-popover-border-width) solid var(--bs-popover-border-color);
              border-radius: var(--bs-popover-border-radius);
            }
            .popover .popover-arrow {
              display: block;
              width: var(--bs-popover-arrow-width);
              height: var(--bs-popover-arrow-height);
            }
            .popover .popover-arrow::before, .popover .popover-arrow::after {
              position: absolute;
              display: block;
              content: "";
              border-color: transparent;
              border-style: solid;
              border-width: 0;
            }

            .bs-popover-top > .popover-arrow, .bs-popover-auto[data-popper-placement^=top] > .popover-arrow {
              bottom: calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width));
            }
            .bs-popover-top > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=top] > .popover-arrow::before, .bs-popover-top > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=top] > .popover-arrow::after {
              border-width: var(--bs-popover-arrow-height) calc(var(--bs-popover-arrow-width) * 0.5) 0;
            }
            .bs-popover-top > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=top] > .popover-arrow::before {
              bottom: 0;
              border-top-color: var(--bs-popover-arrow-border);
            }
            .bs-popover-top > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=top] > .popover-arrow::after {
              bottom: var(--bs-popover-border-width);
              border-top-color: var(--bs-popover-bg);
            }

            /* rtl:begin:ignore */
            .bs-popover-end > .popover-arrow, .bs-popover-auto[data-popper-placement^=right] > .popover-arrow {
              left: calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width));
              width: var(--bs-popover-arrow-height);
              height: var(--bs-popover-arrow-width);
            }
            .bs-popover-end > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=right] > .popover-arrow::before, .bs-popover-end > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=right] > .popover-arrow::after {
              border-width: calc(var(--bs-popover-arrow-width) * 0.5) var(--bs-popover-arrow-height) calc(var(--bs-popover-arrow-width) * 0.5) 0;
            }
            .bs-popover-end > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=right] > .popover-arrow::before {
              left: 0;
              border-right-color: var(--bs-popover-arrow-border);
            }
            .bs-popover-end > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=right] > .popover-arrow::after {
              left: var(--bs-popover-border-width);
              border-right-color: var(--bs-popover-bg);
            }

            /* rtl:end:ignore */
            .bs-popover-bottom > .popover-arrow, .bs-popover-auto[data-popper-placement^=bottom] > .popover-arrow {
              top: calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width));
            }
            .bs-popover-bottom > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=bottom] > .popover-arrow::before, .bs-popover-bottom > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=bottom] > .popover-arrow::after {
              border-width: 0 calc(var(--bs-popover-arrow-width) * 0.5) var(--bs-popover-arrow-height);
            }
            .bs-popover-bottom > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=bottom] > .popover-arrow::before {
              top: 0;
              border-bottom-color: var(--bs-popover-arrow-border);
            }
            .bs-popover-bottom > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=bottom] > .popover-arrow::after {
              top: var(--bs-popover-border-width);
              border-bottom-color: var(--bs-popover-bg);
            }
            .bs-popover-bottom .popover-header::before, .bs-popover-auto[data-popper-placement^=bottom] .popover-header::before {
              position: absolute;
              top: 0;
              left: 50%;
              display: block;
              width: var(--bs-popover-arrow-width);
              margin-left: calc(-0.5 * var(--bs-popover-arrow-width));
              content: "";
              border-bottom: var(--bs-popover-border-width) solid var(--bs-popover-header-bg);
            }

            /* rtl:begin:ignore */
            .bs-popover-start > .popover-arrow, .bs-popover-auto[data-popper-placement^=left] > .popover-arrow {
              right: calc(-1 * (var(--bs-popover-arrow-height)) - var(--bs-popover-border-width));
              width: var(--bs-popover-arrow-height);
              height: var(--bs-popover-arrow-width);
            }
            .bs-popover-start > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=left] > .popover-arrow::before, .bs-popover-start > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=left] > .popover-arrow::after {
              border-width: calc(var(--bs-popover-arrow-width) * 0.5) 0 calc(var(--bs-popover-arrow-width) * 0.5) var(--bs-popover-arrow-height);
            }
            .bs-popover-start > .popover-arrow::before, .bs-popover-auto[data-popper-placement^=left] > .popover-arrow::before {
              right: 0;
              border-left-color: var(--bs-popover-arrow-border);
            }
            .bs-popover-start > .popover-arrow::after, .bs-popover-auto[data-popper-placement^=left] > .popover-arrow::after {
              right: var(--bs-popover-border-width);
              border-left-color: var(--bs-popover-bg);
            }

            /* rtl:end:ignore */
            .popover-header {
              padding: var(--bs-popover-header-padding-y) var(--bs-popover-header-padding-x);
              margin-bottom: 0;
              font-size: var(--bs-popover-header-font-size);
              color: var(--bs-popover-header-color);
              background-color: var(--bs-popover-header-bg);
              border-bottom: var(--bs-popover-border-width) solid var(--bs-popover-border-color);
              border-top-left-radius: var(--bs-popover-inner-border-radius);
              border-top-right-radius: var(--bs-popover-inner-border-radius);
            }
            .popover-header:empty {
              display: none;
            }

            .popover-body {
              padding: var(--bs-popover-body-padding-y) var(--bs-popover-body-padding-x);
              color: var(--bs-popover-body-color);
            }

            .carousel {
              position: relative;
            }

            .carousel.pointer-event {
              touch-action: pan-y;
            }

            .carousel-inner {
              position: relative;
              width: 100%;
              overflow: hidden;
            }
            .carousel-inner::after {
              display: block;
              clear: both;
              content: "";
            }

            .carousel-item {
              position: relative;
              display: none;
              float: left;
              width: 100%;
              margin-right: -100%;
              -webkit-backface-visibility: hidden;
              backface-visibility: hidden;
              transition: transform 0.6s ease-in-out;
            }
            @media (prefers-reduced-motion: reduce) {
              .carousel-item {
                transition: none;
              }
            }

            .carousel-item.active,
            .carousel-item-next,
            .carousel-item-prev {
              display: block;
            }

            .carousel-item-next:not(.carousel-item-start),
            .active.carousel-item-end {
              transform: translateX(100%);
            }

            .carousel-item-prev:not(.carousel-item-end),
            .active.carousel-item-start {
              transform: translateX(-100%);
            }

            .carousel-fade .carousel-item {
              opacity: 0;
              transition-property: opacity;
              transform: none;
            }
            .carousel-fade .carousel-item.active,
            .carousel-fade .carousel-item-next.carousel-item-start,
            .carousel-fade .carousel-item-prev.carousel-item-end {
              z-index: 1;
              opacity: 1;
            }
            .carousel-fade .active.carousel-item-start,
            .carousel-fade .active.carousel-item-end {
              z-index: 0;
              opacity: 0;
              transition: opacity 0s 0.6s;
            }
            @media (prefers-reduced-motion: reduce) {
              .carousel-fade .active.carousel-item-start,
              .carousel-fade .active.carousel-item-end {
                transition: none;
              }
            }

            .carousel-control-prev,
            .carousel-control-next {
              position: absolute;
              top: 0;
              bottom: 0;
              z-index: 1;
              display: flex;
              align-items: center;
              justify-content: center;
              width: 15%;
              padding: 0;
              color: #fff;
              text-align: center;
              background: none;
              border: 0;
              opacity: 0.5;
              transition: opacity 0.15s ease;
            }
            @media (prefers-reduced-motion: reduce) {
              .carousel-control-prev,
              .carousel-control-next {
                transition: none;
              }
            }
            .carousel-control-prev:hover, .carousel-control-prev:focus,
            .carousel-control-next:hover,
            .carousel-control-next:focus {
              color: #fff;
              text-decoration: none;
              outline: 0;
              opacity: 0.9;
            }

            .carousel-control-prev {
              left: 0;
            }

            .carousel-control-next {
              right: 0;
            }

            .carousel-control-prev-icon,
            .carousel-control-next-icon {
              display: inline-block;
              width: 2rem;
              height: 2rem;
              background-repeat: no-repeat;
              background-position: 50%;
              background-size: 100% 100%;
            }

            /* rtl:options: {
              "autoRename": true,
              "stringMap":[ {
                "name"    : "prev-next",
                "search"  : "prev",
                "replace" : "next"
              } ]
            } */
            .carousel-control-prev-icon {
              background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e");
            }

            .carousel-control-next-icon {
              background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
            }

            .carousel-indicators {
              position: absolute;
              right: 0;
              bottom: 0;
              left: 0;
              z-index: 2;
              display: flex;
              justify-content: center;
              padding: 0;
              margin-right: 15%;
              margin-bottom: 1rem;
              margin-left: 15%;
            }
            .carousel-indicators [data-bs-target] {
              box-sizing: content-box;
              flex: 0 1 auto;
              width: 30px;
              height: 3px;
              padding: 0;
              margin-right: 3px;
              margin-left: 3px;
              text-indent: -999px;
              cursor: pointer;
              background-color: #fff;
              background-clip: padding-box;
              border: 0;
              border-top: 10px solid transparent;
              border-bottom: 10px solid transparent;
              opacity: 0.5;
              transition: opacity 0.6s ease;
            }
            @media (prefers-reduced-motion: reduce) {
              .carousel-indicators [data-bs-target] {
                transition: none;
              }
            }
            .carousel-indicators .active {
              opacity: 1;
            }

            .carousel-caption {
              position: absolute;
              right: 15%;
              bottom: 1.25rem;
              left: 15%;
              padding-top: 1.25rem;
              padding-bottom: 1.25rem;
              color: #fff;
              text-align: center;
            }

            .carousel-dark .carousel-control-prev-icon,
            .carousel-dark .carousel-control-next-icon {
              filter: invert(1) grayscale(100);
            }
            .carousel-dark .carousel-indicators [data-bs-target] {
              background-color: #000;
            }
            .carousel-dark .carousel-caption {
              color: #000;
            }

            [data-bs-theme=dark] .carousel .carousel-control-prev-icon,
            [data-bs-theme=dark] .carousel .carousel-control-next-icon, [data-bs-theme=dark].carousel .carousel-control-prev-icon,
            [data-bs-theme=dark].carousel .carousel-control-next-icon {
              filter: invert(1) grayscale(100);
            }
            [data-bs-theme=dark] .carousel .carousel-indicators [data-bs-target], [data-bs-theme=dark].carousel .carousel-indicators [data-bs-target] {
              background-color: #000;
            }
            [data-bs-theme=dark] .carousel .carousel-caption, [data-bs-theme=dark].carousel .carousel-caption {
              color: #000;
            }

            .spinner-grow,
            .spinner-border {
              display: inline-block;
              width: var(--bs-spinner-width);
              height: var(--bs-spinner-height);
              vertical-align: var(--bs-spinner-vertical-align);
              border-radius: 50%;
              animation: var(--bs-spinner-animation-speed) linear infinite var(--bs-spinner-animation-name);
            }

            @keyframes spinner-border {
              to {
                transform: rotate(360deg) /* rtl:ignore */;
              }
            }
            .spinner-border {
              --bs-spinner-width: 2rem;
              --bs-spinner-height: 2rem;
              --bs-spinner-vertical-align: -0.125em;
              --bs-spinner-border-width: 0.25em;
              --bs-spinner-animation-speed: 0.75s;
              --bs-spinner-animation-name: spinner-border;
              border: var(--bs-spinner-border-width) solid currentcolor;
              border-right-color: transparent;
            }

            .spinner-border-sm {
              --bs-spinner-width: 1rem;
              --bs-spinner-height: 1rem;
              --bs-spinner-border-width: 0.2em;
            }

            @keyframes spinner-grow {
              0% {
                transform: scale(0);
              }
              50% {
                opacity: 1;
                transform: none;
              }
            }
            .spinner-grow {
              --bs-spinner-width: 2rem;
              --bs-spinner-height: 2rem;
              --bs-spinner-vertical-align: -0.125em;
              --bs-spinner-animation-speed: 0.75s;
              --bs-spinner-animation-name: spinner-grow;
              background-color: currentcolor;
              opacity: 0;
            }

            .spinner-grow-sm {
              --bs-spinner-width: 1rem;
              --bs-spinner-height: 1rem;
            }

            @media (prefers-reduced-motion: reduce) {
              .spinner-border,
              .spinner-grow {
                --bs-spinner-animation-speed: 1.5s;
              }
            }
            .offcanvas, .offcanvas-xxl, .offcanvas-xl, .offcanvas-lg, .offcanvas-md, .offcanvas-sm {
              --bs-offcanvas-zindex: 1045;
              --bs-offcanvas-width: 400px;
              --bs-offcanvas-height: 30vh;
              --bs-offcanvas-padding-x: 1rem;
              --bs-offcanvas-padding-y: 1rem;
              --bs-offcanvas-color: var(--bs-body-color);
              --bs-offcanvas-bg: var(--bs-body-bg);
              --bs-offcanvas-border-width: var(--bs-border-width);
              --bs-offcanvas-border-color: var(--bs-border-color-translucent);
              --bs-offcanvas-box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
              --bs-offcanvas-transition: transform 0.3s ease-in-out;
              --bs-offcanvas-title-line-height: 1.5;
            }

            @media (max-width: 575.98px) {
              .offcanvas-sm {
                position: fixed;
                bottom: 0;
                z-index: var(--bs-offcanvas-zindex);
                display: flex;
                flex-direction: column;
                max-width: 100%;
                color: var(--bs-offcanvas-color);
                visibility: hidden;
                background-color: var(--bs-offcanvas-bg);
                background-clip: padding-box;
                outline: 0;
                transition: var(--bs-offcanvas-transition);
              }
            }
            @media (max-width: 575.98px) and (prefers-reduced-motion: reduce) {
              .offcanvas-sm {
                transition: none;
              }
            }
            @media (max-width: 575.98px) {
              .offcanvas-sm.offcanvas-start {
                top: 0;
                left: 0;
                width: var(--bs-offcanvas-width);
                border-right: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(-100%);
              }
            }
            @media (max-width: 575.98px) {
              .offcanvas-sm.offcanvas-end {
                top: 0;
                right: 0;
                width: var(--bs-offcanvas-width);
                border-left: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(100%);
              }
            }
            @media (max-width: 575.98px) {
              .offcanvas-sm.offcanvas-top {
                top: 0;
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-bottom: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(-100%);
              }
            }
            @media (max-width: 575.98px) {
              .offcanvas-sm.offcanvas-bottom {
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-top: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(100%);
              }
            }
            @media (max-width: 575.98px) {
              .offcanvas-sm.showing, .offcanvas-sm.show:not(.hiding) {
                transform: none;
              }
            }
            @media (max-width: 575.98px) {
              .offcanvas-sm.showing, .offcanvas-sm.hiding, .offcanvas-sm.show {
                visibility: visible;
              }
            }
            @media (min-width: 576px) {
              .offcanvas-sm {
                --bs-offcanvas-height: auto;
                --bs-offcanvas-border-width: 0;
                background-color: transparent !important;
              }
              .offcanvas-sm .offcanvas-header {
                display: none;
              }
              .offcanvas-sm .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
                background-color: transparent !important;
              }
            }

            @media (max-width: 767.98px) {
              .offcanvas-md {
                position: fixed;
                bottom: 0;
                z-index: var(--bs-offcanvas-zindex);
                display: flex;
                flex-direction: column;
                max-width: 100%;
                color: var(--bs-offcanvas-color);
                visibility: hidden;
                background-color: var(--bs-offcanvas-bg);
                background-clip: padding-box;
                outline: 0;
                transition: var(--bs-offcanvas-transition);
              }
            }
            @media (max-width: 767.98px) and (prefers-reduced-motion: reduce) {
              .offcanvas-md {
                transition: none;
              }
            }
            @media (max-width: 767.98px) {
              .offcanvas-md.offcanvas-start {
                top: 0;
                left: 0;
                width: var(--bs-offcanvas-width);
                border-right: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(-100%);
              }
            }
            @media (max-width: 767.98px) {
              .offcanvas-md.offcanvas-end {
                top: 0;
                right: 0;
                width: var(--bs-offcanvas-width);
                border-left: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(100%);
              }
            }
            @media (max-width: 767.98px) {
              .offcanvas-md.offcanvas-top {
                top: 0;
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-bottom: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(-100%);
              }
            }
            @media (max-width: 767.98px) {
              .offcanvas-md.offcanvas-bottom {
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-top: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(100%);
              }
            }
            @media (max-width: 767.98px) {
              .offcanvas-md.showing, .offcanvas-md.show:not(.hiding) {
                transform: none;
              }
            }
            @media (max-width: 767.98px) {
              .offcanvas-md.showing, .offcanvas-md.hiding, .offcanvas-md.show {
                visibility: visible;
              }
            }
            @media (min-width: 768px) {
              .offcanvas-md {
                --bs-offcanvas-height: auto;
                --bs-offcanvas-border-width: 0;
                background-color: transparent !important;
              }
              .offcanvas-md .offcanvas-header {
                display: none;
              }
              .offcanvas-md .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
                background-color: transparent !important;
              }
            }

            @media (max-width: 991.98px) {
              .offcanvas-lg {
                position: fixed;
                bottom: 0;
                z-index: var(--bs-offcanvas-zindex);
                display: flex;
                flex-direction: column;
                max-width: 100%;
                color: var(--bs-offcanvas-color);
                visibility: hidden;
                background-color: var(--bs-offcanvas-bg);
                background-clip: padding-box;
                outline: 0;
                transition: var(--bs-offcanvas-transition);
              }
            }
            @media (max-width: 991.98px) and (prefers-reduced-motion: reduce) {
              .offcanvas-lg {
                transition: none;
              }
            }
            @media (max-width: 991.98px) {
              .offcanvas-lg.offcanvas-start {
                top: 0;
                left: 0;
                width: var(--bs-offcanvas-width);
                border-right: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(-100%);
              }
            }
            @media (max-width: 991.98px) {
              .offcanvas-lg.offcanvas-end {
                top: 0;
                right: 0;
                width: var(--bs-offcanvas-width);
                border-left: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(100%);
              }
            }
            @media (max-width: 991.98px) {
              .offcanvas-lg.offcanvas-top {
                top: 0;
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-bottom: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(-100%);
              }
            }
            @media (max-width: 991.98px) {
              .offcanvas-lg.offcanvas-bottom {
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-top: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(100%);
              }
            }
            @media (max-width: 991.98px) {
              .offcanvas-lg.showing, .offcanvas-lg.show:not(.hiding) {
                transform: none;
              }
            }
            @media (max-width: 991.98px) {
              .offcanvas-lg.showing, .offcanvas-lg.hiding, .offcanvas-lg.show {
                visibility: visible;
              }
            }
            @media (min-width: 992px) {
              .offcanvas-lg {
                --bs-offcanvas-height: auto;
                --bs-offcanvas-border-width: 0;
                background-color: transparent !important;
              }
              .offcanvas-lg .offcanvas-header {
                display: none;
              }
              .offcanvas-lg .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
                background-color: transparent !important;
              }
            }

            @media (max-width: 1199.98px) {
              .offcanvas-xl {
                position: fixed;
                bottom: 0;
                z-index: var(--bs-offcanvas-zindex);
                display: flex;
                flex-direction: column;
                max-width: 100%;
                color: var(--bs-offcanvas-color);
                visibility: hidden;
                background-color: var(--bs-offcanvas-bg);
                background-clip: padding-box;
                outline: 0;
                transition: var(--bs-offcanvas-transition);
              }
            }
            @media (max-width: 1199.98px) and (prefers-reduced-motion: reduce) {
              .offcanvas-xl {
                transition: none;
              }
            }
            @media (max-width: 1199.98px) {
              .offcanvas-xl.offcanvas-start {
                top: 0;
                left: 0;
                width: var(--bs-offcanvas-width);
                border-right: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(-100%);
              }
            }
            @media (max-width: 1199.98px) {
              .offcanvas-xl.offcanvas-end {
                top: 0;
                right: 0;
                width: var(--bs-offcanvas-width);
                border-left: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(100%);
              }
            }
            @media (max-width: 1199.98px) {
              .offcanvas-xl.offcanvas-top {
                top: 0;
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-bottom: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(-100%);
              }
            }
            @media (max-width: 1199.98px) {
              .offcanvas-xl.offcanvas-bottom {
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-top: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(100%);
              }
            }
            @media (max-width: 1199.98px) {
              .offcanvas-xl.showing, .offcanvas-xl.show:not(.hiding) {
                transform: none;
              }
            }
            @media (max-width: 1199.98px) {
              .offcanvas-xl.showing, .offcanvas-xl.hiding, .offcanvas-xl.show {
                visibility: visible;
              }
            }
            @media (min-width: 1200px) {
              .offcanvas-xl {
                --bs-offcanvas-height: auto;
                --bs-offcanvas-border-width: 0;
                background-color: transparent !important;
              }
              .offcanvas-xl .offcanvas-header {
                display: none;
              }
              .offcanvas-xl .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
                background-color: transparent !important;
              }
            }

            @media (max-width: 1399.98px) {
              .offcanvas-xxl {
                position: fixed;
                bottom: 0;
                z-index: var(--bs-offcanvas-zindex);
                display: flex;
                flex-direction: column;
                max-width: 100%;
                color: var(--bs-offcanvas-color);
                visibility: hidden;
                background-color: var(--bs-offcanvas-bg);
                background-clip: padding-box;
                outline: 0;
                transition: var(--bs-offcanvas-transition);
              }
            }
            @media (max-width: 1399.98px) and (prefers-reduced-motion: reduce) {
              .offcanvas-xxl {
                transition: none;
              }
            }
            @media (max-width: 1399.98px) {
              .offcanvas-xxl.offcanvas-start {
                top: 0;
                left: 0;
                width: var(--bs-offcanvas-width);
                border-right: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(-100%);
              }
            }
            @media (max-width: 1399.98px) {
              .offcanvas-xxl.offcanvas-end {
                top: 0;
                right: 0;
                width: var(--bs-offcanvas-width);
                border-left: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateX(100%);
              }
            }
            @media (max-width: 1399.98px) {
              .offcanvas-xxl.offcanvas-top {
                top: 0;
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-bottom: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(-100%);
              }
            }
            @media (max-width: 1399.98px) {
              .offcanvas-xxl.offcanvas-bottom {
                right: 0;
                left: 0;
                height: var(--bs-offcanvas-height);
                max-height: 100%;
                border-top: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
                transform: translateY(100%);
              }
            }
            @media (max-width: 1399.98px) {
              .offcanvas-xxl.showing, .offcanvas-xxl.show:not(.hiding) {
                transform: none;
              }
            }
            @media (max-width: 1399.98px) {
              .offcanvas-xxl.showing, .offcanvas-xxl.hiding, .offcanvas-xxl.show {
                visibility: visible;
              }
            }
            @media (min-width: 1400px) {
              .offcanvas-xxl {
                --bs-offcanvas-height: auto;
                --bs-offcanvas-border-width: 0;
                background-color: transparent !important;
              }
              .offcanvas-xxl .offcanvas-header {
                display: none;
              }
              .offcanvas-xxl .offcanvas-body {
                display: flex;
                flex-grow: 0;
                padding: 0;
                overflow-y: visible;
                background-color: transparent !important;
              }
            }

            .offcanvas {
              position: fixed;
              bottom: 0;
              z-index: var(--bs-offcanvas-zindex);
              display: flex;
              flex-direction: column;
              max-width: 100%;
              color: var(--bs-offcanvas-color);
              visibility: hidden;
              background-color: var(--bs-offcanvas-bg);
              background-clip: padding-box;
              outline: 0;
              transition: var(--bs-offcanvas-transition);
            }
            @media (prefers-reduced-motion: reduce) {
              .offcanvas {
                transition: none;
              }
            }
            .offcanvas.offcanvas-start {
              top: 0;
              left: 0;
              width: var(--bs-offcanvas-width);
              border-right: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
              transform: translateX(-100%);
            }
            .offcanvas.offcanvas-end {
              top: 0;
              right: 0;
              width: var(--bs-offcanvas-width);
              border-left: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
              transform: translateX(100%);
            }
            .offcanvas.offcanvas-top {
              top: 0;
              right: 0;
              left: 0;
              height: var(--bs-offcanvas-height);
              max-height: 100%;
              border-bottom: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
              transform: translateY(-100%);
            }
            .offcanvas.offcanvas-bottom {
              right: 0;
              left: 0;
              height: var(--bs-offcanvas-height);
              max-height: 100%;
              border-top: var(--bs-offcanvas-border-width) solid var(--bs-offcanvas-border-color);
              transform: translateY(100%);
            }
            .offcanvas.showing, .offcanvas.show:not(.hiding) {
              transform: none;
            }
            .offcanvas.showing, .offcanvas.hiding, .offcanvas.show {
              visibility: visible;
            }

            .offcanvas-backdrop {
              position: fixed;
              top: 0;
              left: 0;
              z-index: 1040;
              width: 100vw;
              height: 100vh;
              background-color: #000;
            }
            .offcanvas-backdrop.fade {
              opacity: 0;
            }
            .offcanvas-backdrop.show {
              opacity: 0.5;
            }

            .offcanvas-header {
              display: flex;
              align-items: center;
              justify-content: space-between;
              padding: var(--bs-offcanvas-padding-y) var(--bs-offcanvas-padding-x);
            }
            .offcanvas-header .btn-close {
              padding: calc(var(--bs-offcanvas-padding-y) * 0.5) calc(var(--bs-offcanvas-padding-x) * 0.5);
              margin-top: calc(-0.5 * var(--bs-offcanvas-padding-y));
              margin-right: calc(-0.5 * var(--bs-offcanvas-padding-x));
              margin-bottom: calc(-0.5 * var(--bs-offcanvas-padding-y));
            }

            .offcanvas-title {
              margin-bottom: 0;
              line-height: var(--bs-offcanvas-title-line-height);
            }

            .offcanvas-body {
              flex-grow: 1;
              padding: var(--bs-offcanvas-padding-y) var(--bs-offcanvas-padding-x);
              overflow-y: auto;
            }

            .placeholder {
              display: inline-block;
              min-height: 1em;
              vertical-align: middle;
              cursor: wait;
              background-color: currentcolor;
              opacity: 0.5;
            }
            .placeholder.btn::before {
              display: inline-block;
              content: "";
            }

            .placeholder-xs {
              min-height: 0.6em;
            }

            .placeholder-sm {
              min-height: 0.8em;
            }

            .placeholder-lg {
              min-height: 1.2em;
            }

            .placeholder-glow .placeholder {
              animation: placeholder-glow 2s ease-in-out infinite;
            }

            @keyframes placeholder-glow {
              50% {
                opacity: 0.2;
              }
            }
            .placeholder-wave {
              -webkit-mask-image: linear-gradient(130deg, #000 55%, rgba(0, 0, 0, 0.8) 75%, #000 95%);
              mask-image: linear-gradient(130deg, #000 55%, rgba(0, 0, 0, 0.8) 75%, #000 95%);
              -webkit-mask-size: 200% 100%;
              mask-size: 200% 100%;
              animation: placeholder-wave 2s linear infinite;
            }

            @keyframes placeholder-wave {
              100% {
                -webkit-mask-position: -200% 0%;
                mask-position: -200% 0%;
              }
            }
            .clearfix::after {
              display: block;
              clear: both;
              content: "";
            }

            .text-bg-primary {
              color: #fff !important;
              background-color: RGBA(13, 110, 253, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-secondary {
              color: #fff !important;
              background-color: RGBA(108, 117, 125, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-success {
              color: #fff !important;
              background-color: RGBA(25, 135, 84, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-info {
              color: #000 !important;
              background-color: RGBA(13, 202, 240, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-warning {
              color: #000 !important;
              background-color: RGBA(255, 193, 7, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-danger {
              color: #fff !important;
              background-color: RGBA(220, 53, 69, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-light {
              color: #000 !important;
              background-color: RGBA(248, 249, 250, var(--bs-bg-opacity, 1)) !important;
            }

            .text-bg-dark {
              color: #fff !important;
              background-color: RGBA(33, 37, 41, var(--bs-bg-opacity, 1)) !important;
            }

            .link-primary {
              color: RGBA(var(--bs-primary-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-primary-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-primary-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-primary:hover, .link-primary:focus {
              color: RGBA(10, 88, 202, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(10, 88, 202, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(10, 88, 202, var(--bs-link-underline-opacity, 1));
            }

            .link-secondary {
              color: RGBA(var(--bs-secondary-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-secondary-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-secondary-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-secondary:hover, .link-secondary:focus {
              color: RGBA(86, 94, 100, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(86, 94, 100, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(86, 94, 100, var(--bs-link-underline-opacity, 1));
            }

            .link-success {
              color: RGBA(var(--bs-success-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-success-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-success-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-success:hover, .link-success:focus {
              color: RGBA(20, 108, 67, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(20, 108, 67, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(20, 108, 67, var(--bs-link-underline-opacity, 1));
            }

            .link-info {
              color: RGBA(var(--bs-info-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-info-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-info-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-info:hover, .link-info:focus {
              color: RGBA(61, 213, 243, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(61, 213, 243, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(61, 213, 243, var(--bs-link-underline-opacity, 1));
            }

            .link-warning {
              color: RGBA(var(--bs-warning-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-warning-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-warning-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-warning:hover, .link-warning:focus {
              color: RGBA(255, 205, 57, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(255, 205, 57, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(255, 205, 57, var(--bs-link-underline-opacity, 1));
            }

            .link-danger {
              color: RGBA(var(--bs-danger-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-danger-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-danger-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-danger:hover, .link-danger:focus {
              color: RGBA(176, 42, 55, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(176, 42, 55, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(176, 42, 55, var(--bs-link-underline-opacity, 1));
            }

            .link-light {
              color: RGBA(var(--bs-light-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-light-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-light-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-light:hover, .link-light:focus {
              color: RGBA(249, 250, 251, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(249, 250, 251, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(249, 250, 251, var(--bs-link-underline-opacity, 1));
            }

            .link-dark {
              color: RGBA(var(--bs-dark-rgb, var(--bs-link-opacity, 1)));
              -webkit-text-decoration-color: RGBA(var(--bs-dark-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-dark-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-dark:hover, .link-dark:focus {
              color: RGBA(26, 30, 33, var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(26, 30, 33, var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(26, 30, 33, var(--bs-link-underline-opacity, 1));
            }

            .link-body-emphasis {
              color: RGBA(var(--bs-emphasis-color-rgb), var(--bs-link-opacity, 1));
              -webkit-text-decoration-color: RGBA(var(--bs-emphasis-color-rgb), var(--bs-link-underline-opacity, 1));
              text-decoration-color: RGBA(var(--bs-emphasis-color-rgb), var(--bs-link-underline-opacity, 1));
            }
            .link-body-emphasis:hover, .link-body-emphasis:focus {
              color: RGBA(var(--bs-emphasis-color-rgb), var(--bs-link-opacity, 0.75));
              -webkit-text-decoration-color: RGBA(var(--bs-emphasis-color-rgb), var(--bs-link-underline-opacity, 0.75));
              text-decoration-color: RGBA(var(--bs-emphasis-color-rgb), var(--bs-link-underline-opacity, 0.75));
            }

            .focus-ring:focus {
              outline: 0;
              box-shadow: var(--bs-focus-ring-x, 0) var(--bs-focus-ring-y, 0) var(--bs-focus-ring-blur, 0) var(--bs-focus-ring-width) var(--bs-focus-ring-color);
            }

            .icon-link {
              display: inline-flex;
              gap: 0.375rem;
              align-items: center;
              -webkit-text-decoration-color: rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 0.5));
              text-decoration-color: rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 0.5));
              text-underline-offset: 0.25em;
              -webkit-backface-visibility: hidden;
              backface-visibility: hidden;
            }
            .icon-link > .bi {
              flex-shrink: 0;
              width: 1em;
              height: 1em;
              fill: currentcolor;
              transition: 0.2s ease-in-out transform;
            }
            @media (prefers-reduced-motion: reduce) {
              .icon-link > .bi {
                transition: none;
              }
            }

            .icon-link-hover:hover > .bi, .icon-link-hover:focus-visible > .bi {
              transform: var(--bs-icon-link-transform, translate3d(0.25em, 0, 0));
            }

            .ratio {
              position: relative;
              width: 100%;
            }
            .ratio::before {
              display: block;
              padding-top: var(--bs-aspect-ratio);
              content: "";
            }
            .ratio > * {
              position: absolute;
              top: 0;
              left: 0;
              width: 100%;
              height: 100%;
            }

            .ratio-1x1 {
              --bs-aspect-ratio: 100%;
            }

            .ratio-4x3 {
              --bs-aspect-ratio: 75%;
            }

            .ratio-16x9 {
              --bs-aspect-ratio: 56.25%;
            }

            .ratio-21x9 {
              --bs-aspect-ratio: 42.8571428571%;
            }

            .fixed-top {
              position: fixed;
              top: 0;
              right: 0;
              left: 0;
              z-index: 1030;
            }

            .fixed-bottom {
              position: fixed;
              right: 0;
              bottom: 0;
              left: 0;
              z-index: 1030;
            }

            .sticky-top {
              position: -webkit-sticky;
              position: sticky;
              top: 0;
              z-index: 1020;
            }

            .sticky-bottom {
              position: -webkit-sticky;
              position: sticky;
              bottom: 0;
              z-index: 1020;
            }

            @media (min-width: 576px) {
              .sticky-sm-top {
                position: -webkit-sticky;
                position: sticky;
                top: 0;
                z-index: 1020;
              }
              .sticky-sm-bottom {
                position: -webkit-sticky;
                position: sticky;
                bottom: 0;
                z-index: 1020;
              }
            }
            @media (min-width: 768px) {
              .sticky-md-top {
                position: -webkit-sticky;
                position: sticky;
                top: 0;
                z-index: 1020;
              }
              .sticky-md-bottom {
                position: -webkit-sticky;
                position: sticky;
                bottom: 0;
                z-index: 1020;
              }
            }
            @media (min-width: 992px) {
              .sticky-lg-top {
                position: -webkit-sticky;
                position: sticky;
                top: 0;
                z-index: 1020;
              }
              .sticky-lg-bottom {
                position: -webkit-sticky;
                position: sticky;
                bottom: 0;
                z-index: 1020;
              }
            }
            @media (min-width: 1200px) {
              .sticky-xl-top {
                position: -webkit-sticky;
                position: sticky;
                top: 0;
                z-index: 1020;
              }
              .sticky-xl-bottom {
                position: -webkit-sticky;
                position: sticky;
                bottom: 0;
                z-index: 1020;
              }
            }
            @media (min-width: 1400px) {
              .sticky-xxl-top {
                position: -webkit-sticky;
                position: sticky;
                top: 0;
                z-index: 1020;
              }
              .sticky-xxl-bottom {
                position: -webkit-sticky;
                position: sticky;
                bottom: 0;
                z-index: 1020;
              }
            }
            .hstack {
              display: flex;
              flex-direction: row;
              align-items: center;
              align-self: stretch;
            }

            .vstack {
              display: flex;
              flex: 1 1 auto;
              flex-direction: column;
              align-self: stretch;
            }

            .visually-hidden,
            .visually-hidden-focusable:not(:focus):not(:focus-within) {
              width: 1px !important;
              height: 1px !important;
              padding: 0 !important;
              margin: -1px !important;
              overflow: hidden !important;
              clip: rect(0, 0, 0, 0) !important;
              white-space: nowrap !important;
              border: 0 !important;
            }
            .visually-hidden:not(caption),
            .visually-hidden-focusable:not(:focus):not(:focus-within):not(caption) {
              position: absolute !important;
            }

            .stretched-link::after {
              position: absolute;
              top: 0;
              right: 0;
              bottom: 0;
              left: 0;
              z-index: 1;
              content: "";
            }

            .text-truncate {
              overflow: hidden;
              text-overflow: ellipsis;
              white-space: nowrap;
            }

            .vr {
              display: inline-block;
              align-self: stretch;
              width: 1px;
              min-height: 1em;
              background-color: currentcolor;
              opacity: 0.25;
            }

            .align-baseline {
              vertical-align: baseline !important;
            }

            .align-top {
              vertical-align: top !important;
            }

            .align-middle {
              vertical-align: middle !important;
            }

            .align-bottom {
              vertical-align: bottom !important;
            }

            .align-text-bottom {
              vertical-align: text-bottom !important;
            }

            .align-text-top {
              vertical-align: text-top !important;
            }

            .float-start {
              float: left !important;
            }

            .float-end {
              float: right !important;
            }

            .float-none {
              float: none !important;
            }

            .object-fit-contain {
              -o-object-fit: contain !important;
              object-fit: contain !important;
            }

            .object-fit-cover {
              -o-object-fit: cover !important;
              object-fit: cover !important;
            }

            .object-fit-fill {
              -o-object-fit: fill !important;
              object-fit: fill !important;
            }

            .object-fit-scale {
              -o-object-fit: scale-down !important;
              object-fit: scale-down !important;
            }

            .object-fit-none {
              -o-object-fit: none !important;
              object-fit: none !important;
            }

            .opacity-0 {
              opacity: 0 !important;
            }

            .opacity-25 {
              opacity: 0.25 !important;
            }

            .opacity-50 {
              opacity: 0.5 !important;
            }

            .opacity-75 {
              opacity: 0.75 !important;
            }

            .opacity-100 {
              opacity: 1 !important;
            }

            .overflow-auto {
              overflow: auto !important;
            }

            .overflow-hidden {
              overflow: hidden !important;
            }

            .overflow-visible {
              overflow: visible !important;
            }

            .overflow-scroll {
              overflow: scroll !important;
            }

            .overflow-x-auto {
              overflow-x: auto !important;
            }

            .overflow-x-hidden {
              overflow-x: hidden !important;
            }

            .overflow-x-visible {
              overflow-x: visible !important;
            }

            .overflow-x-scroll {
              overflow-x: scroll !important;
            }

            .overflow-y-auto {
              overflow-y: auto !important;
            }

            .overflow-y-hidden {
              overflow-y: hidden !important;
            }

            .overflow-y-visible {
              overflow-y: visible !important;
            }

            .overflow-y-scroll {
              overflow-y: scroll !important;
            }

            .d-inline {
              display: inline !important;
            }

            .d-inline-block {
              display: inline-block !important;
            }

            .d-block {
              display: block !important;
            }

            .d-grid {
              display: grid !important;
            }

            .d-table {
              display: table !important;
            }

            .d-table-row {
              display: table-row !important;
            }

            .d-table-cell {
              display: table-cell !important;
            }

            .d-flex {
              display: flex !important;
            }

            .d-inline-flex {
              display: inline-flex !important;
            }

            .d-none {
              display: none !important;
            }

            .shadow {
              box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
            }

            .shadow-sm {
              box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important;
            }

            .shadow-lg {
              box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important;
            }

            .shadow-none {
              box-shadow: none !important;
            }

            .focus-ring-primary {
              --bs-focus-ring-color: rgba(var(--bs-primary-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-secondary {
              --bs-focus-ring-color: rgba(var(--bs-secondary-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-success {
              --bs-focus-ring-color: rgba(var(--bs-success-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-info {
              --bs-focus-ring-color: rgba(var(--bs-info-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-warning {
              --bs-focus-ring-color: rgba(var(--bs-warning-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-danger {
              --bs-focus-ring-color: rgba(var(--bs-danger-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-light {
              --bs-focus-ring-color: rgba(var(--bs-light-rgb), var(--bs-focus-ring-opacity));
            }

            .focus-ring-dark {
              --bs-focus-ring-color: rgba(var(--bs-dark-rgb), var(--bs-focus-ring-opacity));
            }

            .position-static {
              position: static !important;
            }

            .position-relative {
              position: relative !important;
            }

            .position-absolute {
              position: absolute !important;
            }

            .position-fixed {
              position: fixed !important;
            }

            .position-sticky {
              position: -webkit-sticky !important;
              position: sticky !important;
            }

            .top-0 {
              top: 0 !important;
            }

            .top-50 {
              top: 50% !important;
            }

            .top-100 {
              top: 100% !important;
            }

            .bottom-0 {
              bottom: 0 !important;
            }

            .bottom-50 {
              bottom: 50% !important;
            }

            .bottom-100 {
              bottom: 100% !important;
            }

            .start-0 {
              left: 0 !important;
            }

            .start-50 {
              left: 50% !important;
            }

            .start-100 {
              left: 100% !important;
            }

            .end-0 {
              right: 0 !important;
            }

            .end-50 {
              right: 50% !important;
            }

            .end-100 {
              right: 100% !important;
            }

            .translate-middle {
              transform: translate(-50%, -50%) !important;
            }

            .translate-middle-x {
              transform: translateX(-50%) !important;
            }

            .translate-middle-y {
              transform: translateY(-50%) !important;
            }

            .border {
              border: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
            }

            .border-0 {
              border: 0 !important;
            }

            .border-top {
              border-top: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
            }

            .border-top-0 {
              border-top: 0 !important;
            }

            .border-end {
              border-right: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
            }

            .border-end-0 {
              border-right: 0 !important;
            }

            .border-bottom {
              border-bottom: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
            }

            .border-bottom-0 {
              border-bottom: 0 !important;
            }

            .border-start {
              border-left: var(--bs-border-width) var(--bs-border-style) var(--bs-border-color) !important;
            }

            .border-start-0 {
              border-left: 0 !important;
            }

            .border-primary {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-primary-rgb), var(--bs-border-opacity)) !important;
            }

            .border-secondary {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-secondary-rgb), var(--bs-border-opacity)) !important;
            }

            .border-success {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-success-rgb), var(--bs-border-opacity)) !important;
            }

            .border-info {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-info-rgb), var(--bs-border-opacity)) !important;
            }

            .border-warning {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-warning-rgb), var(--bs-border-opacity)) !important;
            }

            .border-danger {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-danger-rgb), var(--bs-border-opacity)) !important;
            }

            .border-light {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-light-rgb), var(--bs-border-opacity)) !important;
            }

            .border-dark {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-dark-rgb), var(--bs-border-opacity)) !important;
            }

            .border-black {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-black-rgb), var(--bs-border-opacity)) !important;
            }

            .border-white {
              --bs-border-opacity: 1;
              border-color: rgba(var(--bs-white-rgb), var(--bs-border-opacity)) !important;
            }

            .border-primary-subtle {
              border-color: var(--bs-primary-border-subtle) !important;
            }

            .border-secondary-subtle {
              border-color: var(--bs-secondary-border-subtle) !important;
            }

            .border-success-subtle {
              border-color: var(--bs-success-border-subtle) !important;
            }

            .border-info-subtle {
              border-color: var(--bs-info-border-subtle) !important;
            }

            .border-warning-subtle {
              border-color: var(--bs-warning-border-subtle) !important;
            }

            .border-danger-subtle {
              border-color: var(--bs-danger-border-subtle) !important;
            }

            .border-light-subtle {
              border-color: var(--bs-light-border-subtle) !important;
            }

            .border-dark-subtle {
              border-color: var(--bs-dark-border-subtle) !important;
            }

            .border-1 {
              border-width: 1px !important;
            }

            .border-2 {
              border-width: 2px !important;
            }

            .border-3 {
              border-width: 3px !important;
            }

            .border-4 {
              border-width: 4px !important;
            }

            .border-5 {
              border-width: 5px !important;
            }

            .border-opacity-10 {
              --bs-border-opacity: 0.1;
            }

            .border-opacity-25 {
              --bs-border-opacity: 0.25;
            }

            .border-opacity-50 {
              --bs-border-opacity: 0.5;
            }

            .border-opacity-75 {
              --bs-border-opacity: 0.75;
            }

            .border-opacity-100 {
              --bs-border-opacity: 1;
            }

            .w-25 {
              width: 25% !important;
            }

            .w-50 {
              width: 50% !important;
            }

            .w-75 {
              width: 75% !important;
            }

            .w-100 {
              width: 100% !important;
            }

            .w-auto {
              width: auto !important;
            }

            .mw-100 {
              max-width: 100% !important;
            }

            .vw-100 {
              width: 100vw !important;
            }

            .min-vw-100 {
              min-width: 100vw !important;
            }

            .h-25 {
              height: 25% !important;
            }

            .h-50 {
              height: 50% !important;
            }

            .h-75 {
              height: 75% !important;
            }

            .h-100 {
              height: 100% !important;
            }

            .h-auto {
              height: auto !important;
            }

            .mh-100 {
              max-height: 100% !important;
            }

            .vh-100 {
              height: 100vh !important;
            }

            .min-vh-100 {
              min-height: 100vh !important;
            }

            .flex-fill {
              flex: 1 1 auto !important;
            }

            .flex-row {
              flex-direction: row !important;
            }

            .flex-column {
              flex-direction: column !important;
            }

            .flex-row-reverse {
              flex-direction: row-reverse !important;
            }

            .flex-column-reverse {
              flex-direction: column-reverse !important;
            }

            .flex-grow-0 {
              flex-grow: 0 !important;
            }

            .flex-grow-1 {
              flex-grow: 1 !important;
            }

            .flex-shrink-0 {
              flex-shrink: 0 !important;
            }

            .flex-shrink-1 {
              flex-shrink: 1 !important;
            }

            .flex-wrap {
              flex-wrap: wrap !important;
            }

            .flex-nowrap {
              flex-wrap: nowrap !important;
            }

            .flex-wrap-reverse {
              flex-wrap: wrap-reverse !important;
            }

            .justify-content-start {
              justify-content: flex-start !important;
            }

            .justify-content-end {
              justify-content: flex-end !important;
            }

            .justify-content-center {
              justify-content: center !important;
            }

            .justify-content-between {
              justify-content: space-between !important;
            }

            .justify-content-around {
              justify-content: space-around !important;
            }

            .justify-content-evenly {
              justify-content: space-evenly !important;
            }

            .align-items-start {
              align-items: flex-start !important;
            }

            .align-items-end {
              align-items: flex-end !important;
            }

            .align-items-center {
              align-items: center !important;
            }

            .align-items-baseline {
              align-items: baseline !important;
            }

            .align-items-stretch {
              align-items: stretch !important;
            }

            .align-content-start {
              align-content: flex-start !important;
            }

            .align-content-end {
              align-content: flex-end !important;
            }

            .align-content-center {
              align-content: center !important;
            }

            .align-content-between {
              align-content: space-between !important;
            }

            .align-content-around {
              align-content: space-around !important;
            }

            .align-content-stretch {
              align-content: stretch !important;
            }

            .align-self-auto {
              align-self: auto !important;
            }

            .align-self-start {
              align-self: flex-start !important;
            }

            .align-self-end {
              align-self: flex-end !important;
            }

            .align-self-center {
              align-self: center !important;
            }

            .align-self-baseline {
              align-self: baseline !important;
            }

            .align-self-stretch {
              align-self: stretch !important;
            }

            .order-first {
              order: -1 !important;
            }

            .order-0 {
              order: 0 !important;
            }

            .order-1 {
              order: 1 !important;
            }

            .order-2 {
              order: 2 !important;
            }

            .order-3 {
              order: 3 !important;
            }

            .order-4 {
              order: 4 !important;
            }

            .order-5 {
              order: 5 !important;
            }

            .order-last {
              order: 6 !important;
            }

            .m-0 {
              margin: 0 !important;
            }

            .m-1 {
              margin: 0.25rem !important;
            }

            .m-2 {
              margin: 0.5rem !important;
            }

            .m-3 {
              margin: 1rem !important;
            }

            .m-4 {
              margin: 1.5rem !important;
            }

            .m-5 {
              margin: 3rem !important;
            }

            .m-auto {
              margin: auto !important;
            }

            .mx-0 {
              margin-right: 0 !important;
              margin-left: 0 !important;
            }

            .mx-1 {
              margin-right: 0.25rem !important;
              margin-left: 0.25rem !important;
            }

            .mx-2 {
              margin-right: 0.5rem !important;
              margin-left: 0.5rem !important;
            }

            .mx-3 {
              margin-right: 1rem !important;
              margin-left: 1rem !important;
            }

            .mx-4 {
              margin-right: 1.5rem !important;
              margin-left: 1.5rem !important;
            }

            .mx-5 {
              margin-right: 3rem !important;
              margin-left: 3rem !important;
            }

            .mx-auto {
              margin-right: auto !important;
              margin-left: auto !important;
            }

            .my-0 {
              margin-top: 0 !important;
              margin-bottom: 0 !important;
            }

            .my-1 {
              margin-top: 0.25rem !important;
              margin-bottom: 0.25rem !important;
            }

            .my-2 {
              margin-top: 0.5rem !important;
              margin-bottom: 0.5rem !important;
            }

            .my-3 {
              margin-top: 1rem !important;
              margin-bottom: 1rem !important;
            }

            .my-4 {
              margin-top: 1.5rem !important;
              margin-bottom: 1.5rem !important;
            }

            .my-5 {
              margin-top: 3rem !important;
              margin-bottom: 3rem !important;
            }

            .my-auto {
              margin-top: auto !important;
              margin-bottom: auto !important;
            }

            .mt-0 {
              margin-top: 0 !important;
            }

            .mt-1 {
              margin-top: 0.25rem !important;
            }

            .mt-2 {
              margin-top: 0.5rem !important;
            }

            .mt-3 {
              margin-top: 1rem !important;
            }

            .mt-4 {
              margin-top: 1.5rem !important;
            }

            .mt-5 {
              margin-top: 3rem !important;
            }

            .mt-auto {
              margin-top: auto !important;
            }

            .me-0 {
              margin-right: 0 !important;
            }

            .me-1 {
              margin-right: 0.25rem !important;
            }

            .me-2 {
              margin-right: 0.5rem !important;
            }

            .me-3 {
              margin-right: 1rem !important;
            }

            .me-4 {
              margin-right: 1.5rem !important;
            }

            .me-5 {
              margin-right: 3rem !important;
            }

            .me-auto {
              margin-right: auto !important;
            }

            .mb-0 {
              margin-bottom: 0 !important;
            }

            .mb-1 {
              margin-bottom: 0.25rem !important;
            }

            .mb-2 {
              margin-bottom: 0.5rem !important;
            }

            .mb-3 {
              margin-bottom: 1rem !important;
            }

            .mb-4 {
              margin-bottom: 1.5rem !important;
            }

            .mb-5 {
              margin-bottom: 3rem !important;
            }

            .mb-auto {
              margin-bottom: auto !important;
            }

            .ms-0 {
              margin-left: 0 !important;
            }

            .ms-1 {
              margin-left: 0.25rem !important;
            }

            .ms-2 {
              margin-left: 0.5rem !important;
            }

            .ms-3 {
              margin-left: 1rem !important;
            }

            .ms-4 {
              margin-left: 1.5rem !important;
            }

            .ms-5 {
              margin-left: 3rem !important;
            }

            .ms-auto {
              margin-left: auto !important;
            }

            .p-0 {
              padding: 0 !important;
            }

            .p-1 {
              padding: 0.25rem !important;
            }

            .p-2 {
              padding: 0.5rem !important;
            }

            .p-3 {
              padding: 1rem !important;
            }

            .p-4 {
              padding: 1.5rem !important;
            }

            .p-5 {
              padding: 3rem !important;
            }

            .px-0 {
              padding-right: 0 !important;
              padding-left: 0 !important;
            }

            .px-1 {
              padding-right: 0.25rem !important;
              padding-left: 0.25rem !important;
            }

            .px-2 {
              padding-right: 0.5rem !important;
              padding-left: 0.5rem !important;
            }

            .px-3 {
              padding-right: 1rem !important;
              padding-left: 1rem !important;
            }

            .px-4 {
              padding-right: 1.5rem !important;
              padding-left: 1.5rem !important;
            }

            .px-5 {
              padding-right: 3rem !important;
              padding-left: 3rem !important;
            }

            .py-0 {
              padding-top: 0 !important;
              padding-bottom: 0 !important;
            }

            .py-1 {
              padding-top: 0.25rem !important;
              padding-bottom: 0.25rem !important;
            }

            .py-2 {
              padding-top: 0.5rem !important;
              padding-bottom: 0.5rem !important;
            }

            .py-3 {
              padding-top: 1rem !important;
              padding-bottom: 1rem !important;
            }

            .py-4 {
              padding-top: 1.5rem !important;
              padding-bottom: 1.5rem !important;
            }

            .py-5 {
              padding-top: 3rem !important;
              padding-bottom: 3rem !important;
            }

            .pt-0 {
              padding-top: 0 !important;
            }

            .pt-1 {
              padding-top: 0.25rem !important;
            }

            .pt-2 {
              padding-top: 0.5rem !important;
            }

            .pt-3 {
              padding-top: 1rem !important;
            }

            .pt-4 {
              padding-top: 1.5rem !important;
            }

            .pt-5 {
              padding-top: 3rem !important;
            }

            .pe-0 {
              padding-right: 0 !important;
            }

            .pe-1 {
              padding-right: 0.25rem !important;
            }

            .pe-2 {
              padding-right: 0.5rem !important;
            }

            .pe-3 {
              padding-right: 1rem !important;
            }

            .pe-4 {
              padding-right: 1.5rem !important;
            }

            .pe-5 {
              padding-right: 3rem !important;
            }

            .pb-0 {
              padding-bottom: 0 !important;
            }

            .pb-1 {
              padding-bottom: 0.25rem !important;
            }

            .pb-2 {
              padding-bottom: 0.5rem !important;
            }

            .pb-3 {
              padding-bottom: 1rem !important;
            }

            .pb-4 {
              padding-bottom: 1.5rem !important;
            }

            .pb-5 {
              padding-bottom: 3rem !important;
            }

            .ps-0 {
              padding-left: 0 !important;
            }

            .ps-1 {
              padding-left: 0.25rem !important;
            }

            .ps-2 {
              padding-left: 0.5rem !important;
            }

            .ps-3 {
              padding-left: 1rem !important;
            }

            .ps-4 {
              padding-left: 1.5rem !important;
            }

            .ps-5 {
              padding-left: 3rem !important;
            }

            .gap-0 {
              gap: 0 !important;
            }

            .gap-1 {
              gap: 0.25rem !important;
            }

            .gap-2 {
              gap: 0.5rem !important;
            }

            .gap-3 {
              gap: 1rem !important;
            }

            .gap-4 {
              gap: 1.5rem !important;
            }

            .gap-5 {
              gap: 3rem !important;
            }

            .row-gap-0 {
              row-gap: 0 !important;
            }

            .row-gap-1 {
              row-gap: 0.25rem !important;
            }

            .row-gap-2 {
              row-gap: 0.5rem !important;
            }

            .row-gap-3 {
              row-gap: 1rem !important;
            }

            .row-gap-4 {
              row-gap: 1.5rem !important;
            }

            .row-gap-5 {
              row-gap: 3rem !important;
            }

            .column-gap-0 {
              -moz-column-gap: 0 !important;
              column-gap: 0 !important;
            }

            .column-gap-1 {
              -moz-column-gap: 0.25rem !important;
              column-gap: 0.25rem !important;
            }

            .column-gap-2 {
              -moz-column-gap: 0.5rem !important;
              column-gap: 0.5rem !important;
            }

            .column-gap-3 {
              -moz-column-gap: 1rem !important;
              column-gap: 1rem !important;
            }

            .column-gap-4 {
              -moz-column-gap: 1.5rem !important;
              column-gap: 1.5rem !important;
            }

            .column-gap-5 {
              -moz-column-gap: 3rem !important;
              column-gap: 3rem !important;
            }

            .font-monospace {
              font-family: var(--bs-font-monospace) !important;
            }

            .fs-1 {
              font-size: calc(1.375rem + 1.5vw) !important;
            }

            .fs-2 {
              font-size: calc(1.325rem + 0.9vw) !important;
            }

            .fs-3 {
              font-size: calc(1.3rem + 0.6vw) !important;
            }

            .fs-4 {
              font-size: calc(1.275rem + 0.3vw) !important;
            }

            .fs-5 {
              font-size: 1.25rem !important;
            }

            .fs-6 {
              font-size: 1rem !important;
            }

            .fst-italic {
              font-style: italic !important;
            }

            .fst-normal {
              font-style: normal !important;
            }

            .fw-lighter {
              font-weight: lighter !important;
            }

            .fw-light {
              font-weight: 300 !important;
            }

            .fw-normal {
              font-weight: 400 !important;
            }

            .fw-medium {
              font-weight: 500 !important;
            }

            .fw-semibold {
              font-weight: 600 !important;
            }

            .fw-bold {
              font-weight: 700 !important;
            }

            .fw-bolder {
              font-weight: bolder !important;
            }

            .lh-1 {
              line-height: 1 !important;
            }

            .lh-sm {
              line-height: 1.25 !important;
            }

            .lh-base {
              line-height: 1.5 !important;
            }

            .lh-lg {
              line-height: 2 !important;
            }

            .text-start {
              text-align: left !important;
            }

            .text-end {
              text-align: right !important;
            }

            .text-center {
              text-align: center !important;
            }

            .text-decoration-none {
              text-decoration: none !important;
            }

            .text-decoration-underline {
              text-decoration: underline !important;
            }

            .text-decoration-line-through {
              text-decoration: line-through !important;
            }

            .text-lowercase {
              text-transform: lowercase !important;
            }

            .text-uppercase {
              text-transform: uppercase !important;
            }

            .text-capitalize {
              text-transform: capitalize !important;
            }

            .text-wrap {
              white-space: normal !important;
            }

            .text-nowrap {
              white-space: nowrap !important;
            }

            /* rtl:begin:remove */
            .text-break {
              word-wrap: break-word !important;
              word-break: break-word !important;
            }

            /* rtl:end:remove */
            .text-primary {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-primary-rgb), var(--bs-text-opacity)) !important;
            }

            .text-secondary {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-secondary-rgb), var(--bs-text-opacity)) !important;
            }

            .text-success {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-success-rgb), var(--bs-text-opacity)) !important;
            }

            .text-info {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-info-rgb), var(--bs-text-opacity)) !important;
            }

            .text-warning {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-warning-rgb), var(--bs-text-opacity)) !important;
            }

            .text-danger {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-danger-rgb), var(--bs-text-opacity)) !important;
            }

            .text-light {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-light-rgb), var(--bs-text-opacity)) !important;
            }

            .text-dark {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-dark-rgb), var(--bs-text-opacity)) !important;
            }

            .text-black {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-black-rgb), var(--bs-text-opacity)) !important;
            }

            .text-white {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-white-rgb), var(--bs-text-opacity)) !important;
            }

            .text-body {
              --bs-text-opacity: 1;
              color: rgba(var(--bs-body-color-rgb), var(--bs-text-opacity)) !important;
            }

            .text-muted {
              --bs-text-opacity: 1;
              color: var(--bs-secondary-color) !important;
            }

            .text-black-50 {
              --bs-text-opacity: 1;
              color: rgba(0, 0, 0, 0.5) !important;
            }

            .text-white-50 {
              --bs-text-opacity: 1;
              color: rgba(255, 255, 255, 0.5) !important;
            }

            .text-body-secondary {
              --bs-text-opacity: 1;
              color: var(--bs-secondary-color) !important;
            }

            .text-body-tertiary {
              --bs-text-opacity: 1;
              color: var(--bs-tertiary-color) !important;
            }

            .text-body-emphasis {
              --bs-text-opacity: 1;
              color: var(--bs-emphasis-color) !important;
            }

            .text-reset {
              --bs-text-opacity: 1;
              color: inherit !important;
            }

            .text-opacity-25 {
              --bs-text-opacity: 0.25;
            }

            .text-opacity-50 {
              --bs-text-opacity: 0.5;
            }

            .text-opacity-75 {
              --bs-text-opacity: 0.75;
            }

            .text-opacity-100 {
              --bs-text-opacity: 1;
            }

            .text-primary-emphasis {
              color: var(--bs-primary-text-emphasis) !important;
            }

            .text-secondary-emphasis {
              color: var(--bs-secondary-text-emphasis) !important;
            }

            .text-success-emphasis {
              color: var(--bs-success-text-emphasis) !important;
            }

            .text-info-emphasis {
              color: var(--bs-info-text-emphasis) !important;
            }

            .text-warning-emphasis {
              color: var(--bs-warning-text-emphasis) !important;
            }

            .text-danger-emphasis {
              color: var(--bs-danger-text-emphasis) !important;
            }

            .text-light-emphasis {
              color: var(--bs-light-text-emphasis) !important;
            }

            .text-dark-emphasis {
              color: var(--bs-dark-text-emphasis) !important;
            }

            .link-opacity-10 {
              --bs-link-opacity: 0.1;
            }

            .link-opacity-10-hover:hover {
              --bs-link-opacity: 0.1;
            }

            .link-opacity-25 {
              --bs-link-opacity: 0.25;
            }

            .link-opacity-25-hover:hover {
              --bs-link-opacity: 0.25;
            }

            .link-opacity-50 {
              --bs-link-opacity: 0.5;
            }

            .link-opacity-50-hover:hover {
              --bs-link-opacity: 0.5;
            }

            .link-opacity-75 {
              --bs-link-opacity: 0.75;
            }

            .link-opacity-75-hover:hover {
              --bs-link-opacity: 0.75;
            }

            .link-opacity-100 {
              --bs-link-opacity: 1;
            }

            .link-opacity-100-hover:hover {
              --bs-link-opacity: 1;
            }

            .link-offset-1 {
              text-underline-offset: 0.125em !important;
            }

            .link-offset-1-hover:hover {
              text-underline-offset: 0.125em !important;
            }

            .link-offset-2 {
              text-underline-offset: 0.25em !important;
            }

            .link-offset-2-hover:hover {
              text-underline-offset: 0.25em !important;
            }

            .link-offset-3 {
              text-underline-offset: 0.375em !important;
            }

            .link-offset-3-hover:hover {
              text-underline-offset: 0.375em !important;
            }

            .link-underline-primary {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-primary-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-primary-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-secondary {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-secondary-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-secondary-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-success {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-success-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-success-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-info {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-info-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-info-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-warning {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-warning-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-warning-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-danger {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-danger-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-danger-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-light {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-light-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-light-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline-dark {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-dark-rgb), var(--bs-link-underline-opacity)) !important;
              text-decoration-color: rgba(var(--bs-dark-rgb), var(--bs-link-underline-opacity)) !important;
            }

            .link-underline {
              --bs-link-underline-opacity: 1;
              -webkit-text-decoration-color: rgba(var(--bs-link-color-rgb), var(--bs-link-underline-opacity, 1)) !important;
              text-decoration-color: rgba(var(--bs-link-color-rgb), var(--bs-link-underline-opacity, 1)) !important;
            }

            .link-underline-opacity-0 {
              --bs-link-underline-opacity: 0;
            }

            .link-underline-opacity-0-hover:hover {
              --bs-link-underline-opacity: 0;
            }

            .link-underline-opacity-10 {
              --bs-link-underline-opacity: 0.1;
            }

            .link-underline-opacity-10-hover:hover {
              --bs-link-underline-opacity: 0.1;
            }

            .link-underline-opacity-25 {
              --bs-link-underline-opacity: 0.25;
            }

            .link-underline-opacity-25-hover:hover {
              --bs-link-underline-opacity: 0.25;
            }

            .link-underline-opacity-50 {
              --bs-link-underline-opacity: 0.5;
            }

            .link-underline-opacity-50-hover:hover {
              --bs-link-underline-opacity: 0.5;
            }

            .link-underline-opacity-75 {
              --bs-link-underline-opacity: 0.75;
            }

            .link-underline-opacity-75-hover:hover {
              --bs-link-underline-opacity: 0.75;
            }

            .link-underline-opacity-100 {
              --bs-link-underline-opacity: 1;
            }

            .link-underline-opacity-100-hover:hover {
              --bs-link-underline-opacity: 1;
            }

            .bg-primary {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-primary-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-secondary {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-secondary-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-success {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-success-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-info {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-info-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-warning {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-warning-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-danger {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-danger-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-light {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-light-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-dark {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-dark-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-black {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-black-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-white {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-white-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-body {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-body-bg-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-transparent {
              --bs-bg-opacity: 1;
              background-color: transparent !important;
            }

            .bg-body-secondary {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-secondary-bg-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-body-tertiary {
              --bs-bg-opacity: 1;
              background-color: rgba(var(--bs-tertiary-bg-rgb), var(--bs-bg-opacity)) !important;
            }

            .bg-opacity-10 {
              --bs-bg-opacity: 0.1;
            }

            .bg-opacity-25 {
              --bs-bg-opacity: 0.25;
            }

            .bg-opacity-50 {
              --bs-bg-opacity: 0.5;
            }

            .bg-opacity-75 {
              --bs-bg-opacity: 0.75;
            }

            .bg-opacity-100 {
              --bs-bg-opacity: 1;
            }

            .bg-primary-subtle {
              background-color: var(--bs-primary-bg-subtle) !important;
            }

            .bg-secondary-subtle {
              background-color: var(--bs-secondary-bg-subtle) !important;
            }

            .bg-success-subtle {
              background-color: var(--bs-success-bg-subtle) !important;
            }

            .bg-info-subtle {
              background-color: var(--bs-info-bg-subtle) !important;
            }

            .bg-warning-subtle {
              background-color: var(--bs-warning-bg-subtle) !important;
            }

            .bg-danger-subtle {
              background-color: var(--bs-danger-bg-subtle) !important;
            }

            .bg-light-subtle {
              background-color: var(--bs-light-bg-subtle) !important;
            }

            .bg-dark-subtle {
              background-color: var(--bs-dark-bg-subtle) !important;
            }

            .bg-gradient {
              background-image: var(--bs-gradient) !important;
            }

            .user-select-all {
              -webkit-user-select: all !important;
              -moz-user-select: all !important;
              user-select: all !important;
            }

            .user-select-auto {
              -webkit-user-select: auto !important;
              -moz-user-select: auto !important;
              user-select: auto !important;
            }

            .user-select-none {
              -webkit-user-select: none !important;
              -moz-user-select: none !important;
              user-select: none !important;
            }

            .pe-none {
              pointer-events: none !important;
            }

            .pe-auto {
              pointer-events: auto !important;
            }

            .rounded {
              border-radius: var(--bs-border-radius) !important;
            }

            .rounded-0 {
              border-radius: 0 !important;
            }

            .rounded-1 {
              border-radius: var(--bs-border-radius-sm) !important;
            }

            .rounded-2 {
              border-radius: var(--bs-border-radius) !important;
            }

            .rounded-3 {
              border-radius: var(--bs-border-radius-lg) !important;
            }

            .rounded-4 {
              border-radius: var(--bs-border-radius-xl) !important;
            }

            .rounded-5 {
              border-radius: var(--bs-border-radius-xxl) !important;
            }

            .rounded-circle {
              border-radius: 50% !important;
            }

            .rounded-pill {
              border-radius: var(--bs-border-radius-pill) !important;
            }

            .rounded-top {
              border-top-left-radius: var(--bs-border-radius) !important;
              border-top-right-radius: var(--bs-border-radius) !important;
            }

            .rounded-top-0 {
              border-top-left-radius: 0 !important;
              border-top-right-radius: 0 !important;
            }

            .rounded-top-1 {
              border-top-left-radius: var(--bs-border-radius-sm) !important;
              border-top-right-radius: var(--bs-border-radius-sm) !important;
            }

            .rounded-top-2 {
              border-top-left-radius: var(--bs-border-radius) !important;
              border-top-right-radius: var(--bs-border-radius) !important;
            }

            .rounded-top-3 {
              border-top-left-radius: var(--bs-border-radius-lg) !important;
              border-top-right-radius: var(--bs-border-radius-lg) !important;
            }

            .rounded-top-4 {
              border-top-left-radius: var(--bs-border-radius-xl) !important;
              border-top-right-radius: var(--bs-border-radius-xl) !important;
            }

            .rounded-top-5 {
              border-top-left-radius: var(--bs-border-radius-xxl) !important;
              border-top-right-radius: var(--bs-border-radius-xxl) !important;
            }

            .rounded-top-circle {
              border-top-left-radius: 50% !important;
              border-top-right-radius: 50% !important;
            }

            .rounded-top-pill {
              border-top-left-radius: var(--bs-border-radius-pill) !important;
              border-top-right-radius: var(--bs-border-radius-pill) !important;
            }

            .rounded-end {
              border-top-right-radius: var(--bs-border-radius) !important;
              border-bottom-right-radius: var(--bs-border-radius) !important;
            }

            .rounded-end-0 {
              border-top-right-radius: 0 !important;
              border-bottom-right-radius: 0 !important;
            }

            .rounded-end-1 {
              border-top-right-radius: var(--bs-border-radius-sm) !important;
              border-bottom-right-radius: var(--bs-border-radius-sm) !important;
            }

            .rounded-end-2 {
              border-top-right-radius: var(--bs-border-radius) !important;
              border-bottom-right-radius: var(--bs-border-radius) !important;
            }

            .rounded-end-3 {
              border-top-right-radius: var(--bs-border-radius-lg) !important;
              border-bottom-right-radius: var(--bs-border-radius-lg) !important;
            }

            .rounded-end-4 {
              border-top-right-radius: var(--bs-border-radius-xl) !important;
              border-bottom-right-radius: var(--bs-border-radius-xl) !important;
            }

            .rounded-end-5 {
              border-top-right-radius: var(--bs-border-radius-xxl) !important;
              border-bottom-right-radius: var(--bs-border-radius-xxl) !important;
            }

            .rounded-end-circle {
              border-top-right-radius: 50% !important;
              border-bottom-right-radius: 50% !important;
            }

            .rounded-end-pill {
              border-top-right-radius: var(--bs-border-radius-pill) !important;
              border-bottom-right-radius: var(--bs-border-radius-pill) !important;
            }

            .rounded-bottom {
              border-bottom-right-radius: var(--bs-border-radius) !important;
              border-bottom-left-radius: var(--bs-border-radius) !important;
            }

            .rounded-bottom-0 {
              border-bottom-right-radius: 0 !important;
              border-bottom-left-radius: 0 !important;
            }

            .rounded-bottom-1 {
              border-bottom-right-radius: var(--bs-border-radius-sm) !important;
              border-bottom-left-radius: var(--bs-border-radius-sm) !important;
            }

            .rounded-bottom-2 {
              border-bottom-right-radius: var(--bs-border-radius) !important;
              border-bottom-left-radius: var(--bs-border-radius) !important;
            }

            .rounded-bottom-3 {
              border-bottom-right-radius: var(--bs-border-radius-lg) !important;
              border-bottom-left-radius: var(--bs-border-radius-lg) !important;
            }

            .rounded-bottom-4 {
              border-bottom-right-radius: var(--bs-border-radius-xl) !important;
              border-bottom-left-radius: var(--bs-border-radius-xl) !important;
            }

            .rounded-bottom-5 {
              border-bottom-right-radius: var(--bs-border-radius-xxl) !important;
              border-bottom-left-radius: var(--bs-border-radius-xxl) !important;
            }

            .rounded-bottom-circle {
              border-bottom-right-radius: 50% !important;
              border-bottom-left-radius: 50% !important;
            }

            .rounded-bottom-pill {
              border-bottom-right-radius: var(--bs-border-radius-pill) !important;
              border-bottom-left-radius: var(--bs-border-radius-pill) !important;
            }

            .rounded-start {
              border-bottom-left-radius: var(--bs-border-radius) !important;
              border-top-left-radius: var(--bs-border-radius) !important;
            }

            .rounded-start-0 {
              border-bottom-left-radius: 0 !important;
              border-top-left-radius: 0 !important;
            }

            .rounded-start-1 {
              border-bottom-left-radius: var(--bs-border-radius-sm) !important;
              border-top-left-radius: var(--bs-border-radius-sm) !important;
            }

            .rounded-start-2 {
              border-bottom-left-radius: var(--bs-border-radius) !important;
              border-top-left-radius: var(--bs-border-radius) !important;
            }

            .rounded-start-3 {
              border-bottom-left-radius: var(--bs-border-radius-lg) !important;
              border-top-left-radius: var(--bs-border-radius-lg) !important;
            }

            .rounded-start-4 {
              border-bottom-left-radius: var(--bs-border-radius-xl) !important;
              border-top-left-radius: var(--bs-border-radius-xl) !important;
            }

            .rounded-start-5 {
              border-bottom-left-radius: var(--bs-border-radius-xxl) !important;
              border-top-left-radius: var(--bs-border-radius-xxl) !important;
            }

            .rounded-start-circle {
              border-bottom-left-radius: 50% !important;
              border-top-left-radius: 50% !important;
            }

            .rounded-start-pill {
              border-bottom-left-radius: var(--bs-border-radius-pill) !important;
              border-top-left-radius: var(--bs-border-radius-pill) !important;
            }

            .visible {
              visibility: visible !important;
            }

            .invisible {
              visibility: hidden !important;
            }

            .z-n1 {
              z-index: -1 !important;
            }

            .z-0 {
              z-index: 0 !important;
            }

            .z-1 {
              z-index: 1 !important;
            }

            .z-2 {
              z-index: 2 !important;
            }

            .z-3 {
              z-index: 3 !important;
            }

            @media (min-width: 576px) {
              .float-sm-start {
                float: left !important;
              }
              .float-sm-end {
                float: right !important;
              }
              .float-sm-none {
                float: none !important;
              }
              .object-fit-sm-contain {
                -o-object-fit: contain !important;
                object-fit: contain !important;
              }
              .object-fit-sm-cover {
                -o-object-fit: cover !important;
                object-fit: cover !important;
              }
              .object-fit-sm-fill {
                -o-object-fit: fill !important;
                object-fit: fill !important;
              }
              .object-fit-sm-scale {
                -o-object-fit: scale-down !important;
                object-fit: scale-down !important;
              }
              .object-fit-sm-none {
                -o-object-fit: none !important;
                object-fit: none !important;
              }
              .d-sm-inline {
                display: inline !important;
              }
              .d-sm-inline-block {
                display: inline-block !important;
              }
              .d-sm-block {
                display: block !important;
              }
              .d-sm-grid {
                display: grid !important;
              }
              .d-sm-table {
                display: table !important;
              }
              .d-sm-table-row {
                display: table-row !important;
              }
              .d-sm-table-cell {
                display: table-cell !important;
              }
              .d-sm-flex {
                display: flex !important;
              }
              .d-sm-inline-flex {
                display: inline-flex !important;
              }
              .d-sm-none {
                display: none !important;
              }
              .flex-sm-fill {
                flex: 1 1 auto !important;
              }
              .flex-sm-row {
                flex-direction: row !important;
              }
              .flex-sm-column {
                flex-direction: column !important;
              }
              .flex-sm-row-reverse {
                flex-direction: row-reverse !important;
              }
              .flex-sm-column-reverse {
                flex-direction: column-reverse !important;
              }
              .flex-sm-grow-0 {
                flex-grow: 0 !important;
              }
              .flex-sm-grow-1 {
                flex-grow: 1 !important;
              }
              .flex-sm-shrink-0 {
                flex-shrink: 0 !important;
              }
              .flex-sm-shrink-1 {
                flex-shrink: 1 !important;
              }
              .flex-sm-wrap {
                flex-wrap: wrap !important;
              }
              .flex-sm-nowrap {
                flex-wrap: nowrap !important;
              }
              .flex-sm-wrap-reverse {
                flex-wrap: wrap-reverse !important;
              }
              .justify-content-sm-start {
                justify-content: flex-start !important;
              }
              .justify-content-sm-end {
                justify-content: flex-end !important;
              }
              .justify-content-sm-center {
                justify-content: center !important;
              }
              .justify-content-sm-between {
                justify-content: space-between !important;
              }
              .justify-content-sm-around {
                justify-content: space-around !important;
              }
              .justify-content-sm-evenly {
                justify-content: space-evenly !important;
              }
              .align-items-sm-start {
                align-items: flex-start !important;
              }
              .align-items-sm-end {
                align-items: flex-end !important;
              }
              .align-items-sm-center {
                align-items: center !important;
              }
              .align-items-sm-baseline {
                align-items: baseline !important;
              }
              .align-items-sm-stretch {
                align-items: stretch !important;
              }
              .align-content-sm-start {
                align-content: flex-start !important;
              }
              .align-content-sm-end {
                align-content: flex-end !important;
              }
              .align-content-sm-center {
                align-content: center !important;
              }
              .align-content-sm-between {
                align-content: space-between !important;
              }
              .align-content-sm-around {
                align-content: space-around !important;
              }
              .align-content-sm-stretch {
                align-content: stretch !important;
              }
              .align-self-sm-auto {
                align-self: auto !important;
              }
              .align-self-sm-start {
                align-self: flex-start !important;
              }
              .align-self-sm-end {
                align-self: flex-end !important;
              }
              .align-self-sm-center {
                align-self: center !important;
              }
              .align-self-sm-baseline {
                align-self: baseline !important;
              }
              .align-self-sm-stretch {
                align-self: stretch !important;
              }
              .order-sm-first {
                order: -1 !important;
              }
              .order-sm-0 {
                order: 0 !important;
              }
              .order-sm-1 {
                order: 1 !important;
              }
              .order-sm-2 {
                order: 2 !important;
              }
              .order-sm-3 {
                order: 3 !important;
              }
              .order-sm-4 {
                order: 4 !important;
              }
              .order-sm-5 {
                order: 5 !important;
              }
              .order-sm-last {
                order: 6 !important;
              }
              .m-sm-0 {
                margin: 0 !important;
              }
              .m-sm-1 {
                margin: 0.25rem !important;
              }
              .m-sm-2 {
                margin: 0.5rem !important;
              }
              .m-sm-3 {
                margin: 1rem !important;
              }
              .m-sm-4 {
                margin: 1.5rem !important;
              }
              .m-sm-5 {
                margin: 3rem !important;
              }
              .m-sm-auto {
                margin: auto !important;
              }
              .mx-sm-0 {
                margin-right: 0 !important;
                margin-left: 0 !important;
              }
              .mx-sm-1 {
                margin-right: 0.25rem !important;
                margin-left: 0.25rem !important;
              }
              .mx-sm-2 {
                margin-right: 0.5rem !important;
                margin-left: 0.5rem !important;
              }
              .mx-sm-3 {
                margin-right: 1rem !important;
                margin-left: 1rem !important;
              }
              .mx-sm-4 {
                margin-right: 1.5rem !important;
                margin-left: 1.5rem !important;
              }
              .mx-sm-5 {
                margin-right: 3rem !important;
                margin-left: 3rem !important;
              }
              .mx-sm-auto {
                margin-right: auto !important;
                margin-left: auto !important;
              }
              .my-sm-0 {
                margin-top: 0 !important;
                margin-bottom: 0 !important;
              }
              .my-sm-1 {
                margin-top: 0.25rem !important;
                margin-bottom: 0.25rem !important;
              }
              .my-sm-2 {
                margin-top: 0.5rem !important;
                margin-bottom: 0.5rem !important;
              }
              .my-sm-3 {
                margin-top: 1rem !important;
                margin-bottom: 1rem !important;
              }
              .my-sm-4 {
                margin-top: 1.5rem !important;
                margin-bottom: 1.5rem !important;
              }
              .my-sm-5 {
                margin-top: 3rem !important;
                margin-bottom: 3rem !important;
              }
              .my-sm-auto {
                margin-top: auto !important;
                margin-bottom: auto !important;
              }
              .mt-sm-0 {
                margin-top: 0 !important;
              }
              .mt-sm-1 {
                margin-top: 0.25rem !important;
              }
              .mt-sm-2 {
                margin-top: 0.5rem !important;
              }
              .mt-sm-3 {
                margin-top: 1rem !important;
              }
              .mt-sm-4 {
                margin-top: 1.5rem !important;
              }
              .mt-sm-5 {
                margin-top: 3rem !important;
              }
              .mt-sm-auto {
                margin-top: auto !important;
              }
              .me-sm-0 {
                margin-right: 0 !important;
              }
              .me-sm-1 {
                margin-right: 0.25rem !important;
              }
              .me-sm-2 {
                margin-right: 0.5rem !important;
              }
              .me-sm-3 {
                margin-right: 1rem !important;
              }
              .me-sm-4 {
                margin-right: 1.5rem !important;
              }
              .me-sm-5 {
                margin-right: 3rem !important;
              }
              .me-sm-auto {
                margin-right: auto !important;
              }
              .mb-sm-0 {
                margin-bottom: 0 !important;
              }
              .mb-sm-1 {
                margin-bottom: 0.25rem !important;
              }
              .mb-sm-2 {
                margin-bottom: 0.5rem !important;
              }
              .mb-sm-3 {
                margin-bottom: 1rem !important;
              }
              .mb-sm-4 {
                margin-bottom: 1.5rem !important;
              }
              .mb-sm-5 {
                margin-bottom: 3rem !important;
              }
              .mb-sm-auto {
                margin-bottom: auto !important;
              }
              .ms-sm-0 {
                margin-left: 0 !important;
              }
              .ms-sm-1 {
                margin-left: 0.25rem !important;
              }
              .ms-sm-2 {
                margin-left: 0.5rem !important;
              }
              .ms-sm-3 {
                margin-left: 1rem !important;
              }
              .ms-sm-4 {
                margin-left: 1.5rem !important;
              }
              .ms-sm-5 {
                margin-left: 3rem !important;
              }
              .ms-sm-auto {
                margin-left: auto !important;
              }
              .p-sm-0 {
                padding: 0 !important;
              }
              .p-sm-1 {
                padding: 0.25rem !important;
              }
              .p-sm-2 {
                padding: 0.5rem !important;
              }
              .p-sm-3 {
                padding: 1rem !important;
              }
              .p-sm-4 {
                padding: 1.5rem !important;
              }
              .p-sm-5 {
                padding: 3rem !important;
              }
              .px-sm-0 {
                padding-right: 0 !important;
                padding-left: 0 !important;
              }
              .px-sm-1 {
                padding-right: 0.25rem !important;
                padding-left: 0.25rem !important;
              }
              .px-sm-2 {
                padding-right: 0.5rem !important;
                padding-left: 0.5rem !important;
              }
              .px-sm-3 {
                padding-right: 1rem !important;
                padding-left: 1rem !important;
              }
              .px-sm-4 {
                padding-right: 1.5rem !important;
                padding-left: 1.5rem !important;
              }
              .px-sm-5 {
                padding-right: 3rem !important;
                padding-left: 3rem !important;
              }
              .py-sm-0 {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
              }
              .py-sm-1 {
                padding-top: 0.25rem !important;
                padding-bottom: 0.25rem !important;
              }
              .py-sm-2 {
                padding-top: 0.5rem !important;
                padding-bottom: 0.5rem !important;
              }
              .py-sm-3 {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
              }
              .py-sm-4 {
                padding-top: 1.5rem !important;
                padding-bottom: 1.5rem !important;
              }
              .py-sm-5 {
                padding-top: 3rem !important;
                padding-bottom: 3rem !important;
              }
              .pt-sm-0 {
                padding-top: 0 !important;
              }
              .pt-sm-1 {
                padding-top: 0.25rem !important;
              }
              .pt-sm-2 {
                padding-top: 0.5rem !important;
              }
              .pt-sm-3 {
                padding-top: 1rem !important;
              }
              .pt-sm-4 {
                padding-top: 1.5rem !important;
              }
              .pt-sm-5 {
                padding-top: 3rem !important;
              }
              .pe-sm-0 {
                padding-right: 0 !important;
              }
              .pe-sm-1 {
                padding-right: 0.25rem !important;
              }
              .pe-sm-2 {
                padding-right: 0.5rem !important;
              }
              .pe-sm-3 {
                padding-right: 1rem !important;
              }
              .pe-sm-4 {
                padding-right: 1.5rem !important;
              }
              .pe-sm-5 {
                padding-right: 3rem !important;
              }
              .pb-sm-0 {
                padding-bottom: 0 !important;
              }
              .pb-sm-1 {
                padding-bottom: 0.25rem !important;
              }
              .pb-sm-2 {
                padding-bottom: 0.5rem !important;
              }
              .pb-sm-3 {
                padding-bottom: 1rem !important;
              }
              .pb-sm-4 {
                padding-bottom: 1.5rem !important;
              }
              .pb-sm-5 {
                padding-bottom: 3rem !important;
              }
              .ps-sm-0 {
                padding-left: 0 !important;
              }
              .ps-sm-1 {
                padding-left: 0.25rem !important;
              }
              .ps-sm-2 {
                padding-left: 0.5rem !important;
              }
              .ps-sm-3 {
                padding-left: 1rem !important;
              }
              .ps-sm-4 {
                padding-left: 1.5rem !important;
              }
              .ps-sm-5 {
                padding-left: 3rem !important;
              }
              .gap-sm-0 {
                gap: 0 !important;
              }
              .gap-sm-1 {
                gap: 0.25rem !important;
              }
              .gap-sm-2 {
                gap: 0.5rem !important;
              }
              .gap-sm-3 {
                gap: 1rem !important;
              }
              .gap-sm-4 {
                gap: 1.5rem !important;
              }
              .gap-sm-5 {
                gap: 3rem !important;
              }
              .row-gap-sm-0 {
                row-gap: 0 !important;
              }
              .row-gap-sm-1 {
                row-gap: 0.25rem !important;
              }
              .row-gap-sm-2 {
                row-gap: 0.5rem !important;
              }
              .row-gap-sm-3 {
                row-gap: 1rem !important;
              }
              .row-gap-sm-4 {
                row-gap: 1.5rem !important;
              }
              .row-gap-sm-5 {
                row-gap: 3rem !important;
              }
              .column-gap-sm-0 {
                -moz-column-gap: 0 !important;
                column-gap: 0 !important;
              }
              .column-gap-sm-1 {
                -moz-column-gap: 0.25rem !important;
                column-gap: 0.25rem !important;
              }
              .column-gap-sm-2 {
                -moz-column-gap: 0.5rem !important;
                column-gap: 0.5rem !important;
              }
              .column-gap-sm-3 {
                -moz-column-gap: 1rem !important;
                column-gap: 1rem !important;
              }
              .column-gap-sm-4 {
                -moz-column-gap: 1.5rem !important;
                column-gap: 1.5rem !important;
              }
              .column-gap-sm-5 {
                -moz-column-gap: 3rem !important;
                column-gap: 3rem !important;
              }
              .text-sm-start {
                text-align: left !important;
              }
              .text-sm-end {
                text-align: right !important;
              }
              .text-sm-center {
                text-align: center !important;
              }
            }
            @media (min-width: 768px) {
              .float-md-start {
                float: left !important;
              }
              .float-md-end {
                float: right !important;
              }
              .float-md-none {
                float: none !important;
              }
              .object-fit-md-contain {
                -o-object-fit: contain !important;
                object-fit: contain !important;
              }
              .object-fit-md-cover {
                -o-object-fit: cover !important;
                object-fit: cover !important;
              }
              .object-fit-md-fill {
                -o-object-fit: fill !important;
                object-fit: fill !important;
              }
              .object-fit-md-scale {
                -o-object-fit: scale-down !important;
                object-fit: scale-down !important;
              }
              .object-fit-md-none {
                -o-object-fit: none !important;
                object-fit: none !important;
              }
              .d-md-inline {
                display: inline !important;
              }
              .d-md-inline-block {
                display: inline-block !important;
              }
              .d-md-block {
                display: block !important;
              }
              .d-md-grid {
                display: grid !important;
              }
              .d-md-table {
                display: table !important;
              }
              .d-md-table-row {
                display: table-row !important;
              }
              .d-md-table-cell {
                display: table-cell !important;
              }
              .d-md-flex {
                display: flex !important;
              }
              .d-md-inline-flex {
                display: inline-flex !important;
              }
              .d-md-none {
                display: none !important;
              }
              .flex-md-fill {
                flex: 1 1 auto !important;
              }
              .flex-md-row {
                flex-direction: row !important;
              }
              .flex-md-column {
                flex-direction: column !important;
              }
              .flex-md-row-reverse {
                flex-direction: row-reverse !important;
              }
              .flex-md-column-reverse {
                flex-direction: column-reverse !important;
              }
              .flex-md-grow-0 {
                flex-grow: 0 !important;
              }
              .flex-md-grow-1 {
                flex-grow: 1 !important;
              }
              .flex-md-shrink-0 {
                flex-shrink: 0 !important;
              }
              .flex-md-shrink-1 {
                flex-shrink: 1 !important;
              }
              .flex-md-wrap {
                flex-wrap: wrap !important;
              }
              .flex-md-nowrap {
                flex-wrap: nowrap !important;
              }
              .flex-md-wrap-reverse {
                flex-wrap: wrap-reverse !important;
              }
              .justify-content-md-start {
                justify-content: flex-start !important;
              }
              .justify-content-md-end {
                justify-content: flex-end !important;
              }
              .justify-content-md-center {
                justify-content: center !important;
              }
              .justify-content-md-between {
                justify-content: space-between !important;
              }
              .justify-content-md-around {
                justify-content: space-around !important;
              }
              .justify-content-md-evenly {
                justify-content: space-evenly !important;
              }
              .align-items-md-start {
                align-items: flex-start !important;
              }
              .align-items-md-end {
                align-items: flex-end !important;
              }
              .align-items-md-center {
                align-items: center !important;
              }
              .align-items-md-baseline {
                align-items: baseline !important;
              }
              .align-items-md-stretch {
                align-items: stretch !important;
              }
              .align-content-md-start {
                align-content: flex-start !important;
              }
              .align-content-md-end {
                align-content: flex-end !important;
              }
              .align-content-md-center {
                align-content: center !important;
              }
              .align-content-md-between {
                align-content: space-between !important;
              }
              .align-content-md-around {
                align-content: space-around !important;
              }
              .align-content-md-stretch {
                align-content: stretch !important;
              }
              .align-self-md-auto {
                align-self: auto !important;
              }
              .align-self-md-start {
                align-self: flex-start !important;
              }
              .align-self-md-end {
                align-self: flex-end !important;
              }
              .align-self-md-center {
                align-self: center !important;
              }
              .align-self-md-baseline {
                align-self: baseline !important;
              }
              .align-self-md-stretch {
                align-self: stretch !important;
              }
              .order-md-first {
                order: -1 !important;
              }
              .order-md-0 {
                order: 0 !important;
              }
              .order-md-1 {
                order: 1 !important;
              }
              .order-md-2 {
                order: 2 !important;
              }
              .order-md-3 {
                order: 3 !important;
              }
              .order-md-4 {
                order: 4 !important;
              }
              .order-md-5 {
                order: 5 !important;
              }
              .order-md-last {
                order: 6 !important;
              }
              .m-md-0 {
                margin: 0 !important;
              }
              .m-md-1 {
                margin: 0.25rem !important;
              }
              .m-md-2 {
                margin: 0.5rem !important;
              }
              .m-md-3 {
                margin: 1rem !important;
              }
              .m-md-4 {
                margin: 1.5rem !important;
              }
              .m-md-5 {
                margin: 3rem !important;
              }
              .m-md-auto {
                margin: auto !important;
              }
              .mx-md-0 {
                margin-right: 0 !important;
                margin-left: 0 !important;
              }
              .mx-md-1 {
                margin-right: 0.25rem !important;
                margin-left: 0.25rem !important;
              }
              .mx-md-2 {
                margin-right: 0.5rem !important;
                margin-left: 0.5rem !important;
              }
              .mx-md-3 {
                margin-right: 1rem !important;
                margin-left: 1rem !important;
              }
              .mx-md-4 {
                margin-right: 1.5rem !important;
                margin-left: 1.5rem !important;
              }
              .mx-md-5 {
                margin-right: 3rem !important;
                margin-left: 3rem !important;
              }
              .mx-md-auto {
                margin-right: auto !important;
                margin-left: auto !important;
              }
              .my-md-0 {
                margin-top: 0 !important;
                margin-bottom: 0 !important;
              }
              .my-md-1 {
                margin-top: 0.25rem !important;
                margin-bottom: 0.25rem !important;
              }
              .my-md-2 {
                margin-top: 0.5rem !important;
                margin-bottom: 0.5rem !important;
              }
              .my-md-3 {
                margin-top: 1rem !important;
                margin-bottom: 1rem !important;
              }
              .my-md-4 {
                margin-top: 1.5rem !important;
                margin-bottom: 1.5rem !important;
              }
              .my-md-5 {
                margin-top: 3rem !important;
                margin-bottom: 3rem !important;
              }
              .my-md-auto {
                margin-top: auto !important;
                margin-bottom: auto !important;
              }
              .mt-md-0 {
                margin-top: 0 !important;
              }
              .mt-md-1 {
                margin-top: 0.25rem !important;
              }
              .mt-md-2 {
                margin-top: 0.5rem !important;
              }
              .mt-md-3 {
                margin-top: 1rem !important;
              }
              .mt-md-4 {
                margin-top: 1.5rem !important;
              }
              .mt-md-5 {
                margin-top: 3rem !important;
              }
              .mt-md-auto {
                margin-top: auto !important;
              }
              .me-md-0 {
                margin-right: 0 !important;
              }
              .me-md-1 {
                margin-right: 0.25rem !important;
              }
              .me-md-2 {
                margin-right: 0.5rem !important;
              }
              .me-md-3 {
                margin-right: 1rem !important;
              }
              .me-md-4 {
                margin-right: 1.5rem !important;
              }
              .me-md-5 {
                margin-right: 3rem !important;
              }
              .me-md-auto {
                margin-right: auto !important;
              }
              .mb-md-0 {
                margin-bottom: 0 !important;
              }
              .mb-md-1 {
                margin-bottom: 0.25rem !important;
              }
              .mb-md-2 {
                margin-bottom: 0.5rem !important;
              }
              .mb-md-3 {
                margin-bottom: 1rem !important;
              }
              .mb-md-4 {
                margin-bottom: 1.5rem !important;
              }
              .mb-md-5 {
                margin-bottom: 3rem !important;
              }
              .mb-md-auto {
                margin-bottom: auto !important;
              }
              .ms-md-0 {
                margin-left: 0 !important;
              }
              .ms-md-1 {
                margin-left: 0.25rem !important;
              }
              .ms-md-2 {
                margin-left: 0.5rem !important;
              }
              .ms-md-3 {
                margin-left: 1rem !important;
              }
              .ms-md-4 {
                margin-left: 1.5rem !important;
              }
              .ms-md-5 {
                margin-left: 3rem !important;
              }
              .ms-md-auto {
                margin-left: auto !important;
              }
              .p-md-0 {
                padding: 0 !important;
              }
              .p-md-1 {
                padding: 0.25rem !important;
              }
              .p-md-2 {
                padding: 0.5rem !important;
              }
              .p-md-3 {
                padding: 1rem !important;
              }
              .p-md-4 {
                padding: 1.5rem !important;
              }
              .p-md-5 {
                padding: 3rem !important;
              }
              .px-md-0 {
                padding-right: 0 !important;
                padding-left: 0 !important;
              }
              .px-md-1 {
                padding-right: 0.25rem !important;
                padding-left: 0.25rem !important;
              }
              .px-md-2 {
                padding-right: 0.5rem !important;
                padding-left: 0.5rem !important;
              }
              .px-md-3 {
                padding-right: 1rem !important;
                padding-left: 1rem !important;
              }
              .px-md-4 {
                padding-right: 1.5rem !important;
                padding-left: 1.5rem !important;
              }
              .px-md-5 {
                padding-right: 3rem !important;
                padding-left: 3rem !important;
              }
              .py-md-0 {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
              }
              .py-md-1 {
                padding-top: 0.25rem !important;
                padding-bottom: 0.25rem !important;
              }
              .py-md-2 {
                padding-top: 0.5rem !important;
                padding-bottom: 0.5rem !important;
              }
              .py-md-3 {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
              }
              .py-md-4 {
                padding-top: 1.5rem !important;
                padding-bottom: 1.5rem !important;
              }
              .py-md-5 {
                padding-top: 3rem !important;
                padding-bottom: 3rem !important;
              }
              .pt-md-0 {
                padding-top: 0 !important;
              }
              .pt-md-1 {
                padding-top: 0.25rem !important;
              }
              .pt-md-2 {
                padding-top: 0.5rem !important;
              }
              .pt-md-3 {
                padding-top: 1rem !important;
              }
              .pt-md-4 {
                padding-top: 1.5rem !important;
              }
              .pt-md-5 {
                padding-top: 3rem !important;
              }
              .pe-md-0 {
                padding-right: 0 !important;
              }
              .pe-md-1 {
                padding-right: 0.25rem !important;
              }
              .pe-md-2 {
                padding-right: 0.5rem !important;
              }
              .pe-md-3 {
                padding-right: 1rem !important;
              }
              .pe-md-4 {
                padding-right: 1.5rem !important;
              }
              .pe-md-5 {
                padding-right: 3rem !important;
              }
              .pb-md-0 {
                padding-bottom: 0 !important;
              }
              .pb-md-1 {
                padding-bottom: 0.25rem !important;
              }
              .pb-md-2 {
                padding-bottom: 0.5rem !important;
              }
              .pb-md-3 {
                padding-bottom: 1rem !important;
              }
              .pb-md-4 {
                padding-bottom: 1.5rem !important;
              }
              .pb-md-5 {
                padding-bottom: 3rem !important;
              }
              .ps-md-0 {
                padding-left: 0 !important;
              }
              .ps-md-1 {
                padding-left: 0.25rem !important;
              }
              .ps-md-2 {
                padding-left: 0.5rem !important;
              }
              .ps-md-3 {
                padding-left: 1rem !important;
              }
              .ps-md-4 {
                padding-left: 1.5rem !important;
              }
              .ps-md-5 {
                padding-left: 3rem !important;
              }
              .gap-md-0 {
                gap: 0 !important;
              }
              .gap-md-1 {
                gap: 0.25rem !important;
              }
              .gap-md-2 {
                gap: 0.5rem !important;
              }
              .gap-md-3 {
                gap: 1rem !important;
              }
              .gap-md-4 {
                gap: 1.5rem !important;
              }
              .gap-md-5 {
                gap: 3rem !important;
              }
              .row-gap-md-0 {
                row-gap: 0 !important;
              }
              .row-gap-md-1 {
                row-gap: 0.25rem !important;
              }
              .row-gap-md-2 {
                row-gap: 0.5rem !important;
              }
              .row-gap-md-3 {
                row-gap: 1rem !important;
              }
              .row-gap-md-4 {
                row-gap: 1.5rem !important;
              }
              .row-gap-md-5 {
                row-gap: 3rem !important;
              }
              .column-gap-md-0 {
                -moz-column-gap: 0 !important;
                column-gap: 0 !important;
              }
              .column-gap-md-1 {
                -moz-column-gap: 0.25rem !important;
                column-gap: 0.25rem !important;
              }
              .column-gap-md-2 {
                -moz-column-gap: 0.5rem !important;
                column-gap: 0.5rem !important;
              }
              .column-gap-md-3 {
                -moz-column-gap: 1rem !important;
                column-gap: 1rem !important;
              }
              .column-gap-md-4 {
                -moz-column-gap: 1.5rem !important;
                column-gap: 1.5rem !important;
              }
              .column-gap-md-5 {
                -moz-column-gap: 3rem !important;
                column-gap: 3rem !important;
              }
              .text-md-start {
                text-align: left !important;
              }
              .text-md-end {
                text-align: right !important;
              }
              .text-md-center {
                text-align: center !important;
              }
            }
            @media (min-width: 992px) {
              .float-lg-start {
                float: left !important;
              }
              .float-lg-end {
                float: right !important;
              }
              .float-lg-none {
                float: none !important;
              }
              .object-fit-lg-contain {
                -o-object-fit: contain !important;
                object-fit: contain !important;
              }
              .object-fit-lg-cover {
                -o-object-fit: cover !important;
                object-fit: cover !important;
              }
              .object-fit-lg-fill {
                -o-object-fit: fill !important;
                object-fit: fill !important;
              }
              .object-fit-lg-scale {
                -o-object-fit: scale-down !important;
                object-fit: scale-down !important;
              }
              .object-fit-lg-none {
                -o-object-fit: none !important;
                object-fit: none !important;
              }
              .d-lg-inline {
                display: inline !important;
              }
              .d-lg-inline-block {
                display: inline-block !important;
              }
              .d-lg-block {
                display: block !important;
              }
              .d-lg-grid {
                display: grid !important;
              }
              .d-lg-table {
                display: table !important;
              }
              .d-lg-table-row {
                display: table-row !important;
              }
              .d-lg-table-cell {
                display: table-cell !important;
              }
              .d-lg-flex {
                display: flex !important;
              }
              .d-lg-inline-flex {
                display: inline-flex !important;
              }
              .d-lg-none {
                display: none !important;
              }
              .flex-lg-fill {
                flex: 1 1 auto !important;
              }
              .flex-lg-row {
                flex-direction: row !important;
              }
              .flex-lg-column {
                flex-direction: column !important;
              }
              .flex-lg-row-reverse {
                flex-direction: row-reverse !important;
              }
              .flex-lg-column-reverse {
                flex-direction: column-reverse !important;
              }
              .flex-lg-grow-0 {
                flex-grow: 0 !important;
              }
              .flex-lg-grow-1 {
                flex-grow: 1 !important;
              }
              .flex-lg-shrink-0 {
                flex-shrink: 0 !important;
              }
              .flex-lg-shrink-1 {
                flex-shrink: 1 !important;
              }
              .flex-lg-wrap {
                flex-wrap: wrap !important;
              }
              .flex-lg-nowrap {
                flex-wrap: nowrap !important;
              }
              .flex-lg-wrap-reverse {
                flex-wrap: wrap-reverse !important;
              }
              .justify-content-lg-start {
                justify-content: flex-start !important;
              }
              .justify-content-lg-end {
                justify-content: flex-end !important;
              }
              .justify-content-lg-center {
                justify-content: center !important;
              }
              .justify-content-lg-between {
                justify-content: space-between !important;
              }
              .justify-content-lg-around {
                justify-content: space-around !important;
              }
              .justify-content-lg-evenly {
                justify-content: space-evenly !important;
              }
              .align-items-lg-start {
                align-items: flex-start !important;
              }
              .align-items-lg-end {
                align-items: flex-end !important;
              }
              .align-items-lg-center {
                align-items: center !important;
              }
              .align-items-lg-baseline {
                align-items: baseline !important;
              }
              .align-items-lg-stretch {
                align-items: stretch !important;
              }
              .align-content-lg-start {
                align-content: flex-start !important;
              }
              .align-content-lg-end {
                align-content: flex-end !important;
              }
              .align-content-lg-center {
                align-content: center !important;
              }
              .align-content-lg-between {
                align-content: space-between !important;
              }
              .align-content-lg-around {
                align-content: space-around !important;
              }
              .align-content-lg-stretch {
                align-content: stretch !important;
              }
              .align-self-lg-auto {
                align-self: auto !important;
              }
              .align-self-lg-start {
                align-self: flex-start !important;
              }
              .align-self-lg-end {
                align-self: flex-end !important;
              }
              .align-self-lg-center {
                align-self: center !important;
              }
              .align-self-lg-baseline {
                align-self: baseline !important;
              }
              .align-self-lg-stretch {
                align-self: stretch !important;
              }
              .order-lg-first {
                order: -1 !important;
              }
              .order-lg-0 {
                order: 0 !important;
              }
              .order-lg-1 {
                order: 1 !important;
              }
              .order-lg-2 {
                order: 2 !important;
              }
              .order-lg-3 {
                order: 3 !important;
              }
              .order-lg-4 {
                order: 4 !important;
              }
              .order-lg-5 {
                order: 5 !important;
              }
              .order-lg-last {
                order: 6 !important;
              }
              .m-lg-0 {
                margin: 0 !important;
              }
              .m-lg-1 {
                margin: 0.25rem !important;
              }
              .m-lg-2 {
                margin: 0.5rem !important;
              }
              .m-lg-3 {
                margin: 1rem !important;
              }
              .m-lg-4 {
                margin: 1.5rem !important;
              }
              .m-lg-5 {
                margin: 3rem !important;
              }
              .m-lg-auto {
                margin: auto !important;
              }
              .mx-lg-0 {
                margin-right: 0 !important;
                margin-left: 0 !important;
              }
              .mx-lg-1 {
                margin-right: 0.25rem !important;
                margin-left: 0.25rem !important;
              }
              .mx-lg-2 {
                margin-right: 0.5rem !important;
                margin-left: 0.5rem !important;
              }
              .mx-lg-3 {
                margin-right: 1rem !important;
                margin-left: 1rem !important;
              }
              .mx-lg-4 {
                margin-right: 1.5rem !important;
                margin-left: 1.5rem !important;
              }
              .mx-lg-5 {
                margin-right: 3rem !important;
                margin-left: 3rem !important;
              }
              .mx-lg-auto {
                margin-right: auto !important;
                margin-left: auto !important;
              }
              .my-lg-0 {
                margin-top: 0 !important;
                margin-bottom: 0 !important;
              }
              .my-lg-1 {
                margin-top: 0.25rem !important;
                margin-bottom: 0.25rem !important;
              }
              .my-lg-2 {
                margin-top: 0.5rem !important;
                margin-bottom: 0.5rem !important;
              }
              .my-lg-3 {
                margin-top: 1rem !important;
                margin-bottom: 1rem !important;
              }
              .my-lg-4 {
                margin-top: 1.5rem !important;
                margin-bottom: 1.5rem !important;
              }
              .my-lg-5 {
                margin-top: 3rem !important;
                margin-bottom: 3rem !important;
              }
              .my-lg-auto {
                margin-top: auto !important;
                margin-bottom: auto !important;
              }
              .mt-lg-0 {
                margin-top: 0 !important;
              }
              .mt-lg-1 {
                margin-top: 0.25rem !important;
              }
              .mt-lg-2 {
                margin-top: 0.5rem !important;
              }
              .mt-lg-3 {
                margin-top: 1rem !important;
              }
              .mt-lg-4 {
                margin-top: 1.5rem !important;
              }
              .mt-lg-5 {
                margin-top: 3rem !important;
              }
              .mt-lg-auto {
                margin-top: auto !important;
              }
              .me-lg-0 {
                margin-right: 0 !important;
              }
              .me-lg-1 {
                margin-right: 0.25rem !important;
              }
              .me-lg-2 {
                margin-right: 0.5rem !important;
              }
              .me-lg-3 {
                margin-right: 1rem !important;
              }
              .me-lg-4 {
                margin-right: 1.5rem !important;
              }
              .me-lg-5 {
                margin-right: 3rem !important;
              }
              .me-lg-auto {
                margin-right: auto !important;
              }
              .mb-lg-0 {
                margin-bottom: 0 !important;
              }
              .mb-lg-1 {
                margin-bottom: 0.25rem !important;
              }
              .mb-lg-2 {
                margin-bottom: 0.5rem !important;
              }
              .mb-lg-3 {
                margin-bottom: 1rem !important;
              }
              .mb-lg-4 {
                margin-bottom: 1.5rem !important;
              }
              .mb-lg-5 {
                margin-bottom: 3rem !important;
              }
              .mb-lg-auto {
                margin-bottom: auto !important;
              }
              .ms-lg-0 {
                margin-left: 0 !important;
              }
              .ms-lg-1 {
                margin-left: 0.25rem !important;
              }
              .ms-lg-2 {
                margin-left: 0.5rem !important;
              }
              .ms-lg-3 {
                margin-left: 1rem !important;
              }
              .ms-lg-4 {
                margin-left: 1.5rem !important;
              }
              .ms-lg-5 {
                margin-left: 3rem !important;
              }
              .ms-lg-auto {
                margin-left: auto !important;
              }
              .p-lg-0 {
                padding: 0 !important;
              }
              .p-lg-1 {
                padding: 0.25rem !important;
              }
              .p-lg-2 {
                padding: 0.5rem !important;
              }
              .p-lg-3 {
                padding: 1rem !important;
              }
              .p-lg-4 {
                padding: 1.5rem !important;
              }
              .p-lg-5 {
                padding: 3rem !important;
              }
              .px-lg-0 {
                padding-right: 0 !important;
                padding-left: 0 !important;
              }
              .px-lg-1 {
                padding-right: 0.25rem !important;
                padding-left: 0.25rem !important;
              }
              .px-lg-2 {
                padding-right: 0.5rem !important;
                padding-left: 0.5rem !important;
              }
              .px-lg-3 {
                padding-right: 1rem !important;
                padding-left: 1rem !important;
              }
              .px-lg-4 {
                padding-right: 1.5rem !important;
                padding-left: 1.5rem !important;
              }
              .px-lg-5 {
                padding-right: 3rem !important;
                padding-left: 3rem !important;
              }
              .py-lg-0 {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
              }
              .py-lg-1 {
                padding-top: 0.25rem !important;
                padding-bottom: 0.25rem !important;
              }
              .py-lg-2 {
                padding-top: 0.5rem !important;
                padding-bottom: 0.5rem !important;
              }
              .py-lg-3 {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
              }
              .py-lg-4 {
                padding-top: 1.5rem !important;
                padding-bottom: 1.5rem !important;
              }
              .py-lg-5 {
                padding-top: 3rem !important;
                padding-bottom: 3rem !important;
              }
              .pt-lg-0 {
                padding-top: 0 !important;
              }
              .pt-lg-1 {
                padding-top: 0.25rem !important;
              }
              .pt-lg-2 {
                padding-top: 0.5rem !important;
              }
              .pt-lg-3 {
                padding-top: 1rem !important;
              }
              .pt-lg-4 {
                padding-top: 1.5rem !important;
              }
              .pt-lg-5 {
                padding-top: 3rem !important;
              }
              .pe-lg-0 {
                padding-right: 0 !important;
              }
              .pe-lg-1 {
                padding-right: 0.25rem !important;
              }
              .pe-lg-2 {
                padding-right: 0.5rem !important;
              }
              .pe-lg-3 {
                padding-right: 1rem !important;
              }
              .pe-lg-4 {
                padding-right: 1.5rem !important;
              }
              .pe-lg-5 {
                padding-right: 3rem !important;
              }
              .pb-lg-0 {
                padding-bottom: 0 !important;
              }
              .pb-lg-1 {
                padding-bottom: 0.25rem !important;
              }
              .pb-lg-2 {
                padding-bottom: 0.5rem !important;
              }
              .pb-lg-3 {
                padding-bottom: 1rem !important;
              }
              .pb-lg-4 {
                padding-bottom: 1.5rem !important;
              }
              .pb-lg-5 {
                padding-bottom: 3rem !important;
              }
              .ps-lg-0 {
                padding-left: 0 !important;
              }
              .ps-lg-1 {
                padding-left: 0.25rem !important;
              }
              .ps-lg-2 {
                padding-left: 0.5rem !important;
              }
              .ps-lg-3 {
                padding-left: 1rem !important;
              }
              .ps-lg-4 {
                padding-left: 1.5rem !important;
              }
              .ps-lg-5 {
                padding-left: 3rem !important;
              }
              .gap-lg-0 {
                gap: 0 !important;
              }
              .gap-lg-1 {
                gap: 0.25rem !important;
              }
              .gap-lg-2 {
                gap: 0.5rem !important;
              }
              .gap-lg-3 {
                gap: 1rem !important;
              }
              .gap-lg-4 {
                gap: 1.5rem !important;
              }
              .gap-lg-5 {
                gap: 3rem !important;
              }
              .row-gap-lg-0 {
                row-gap: 0 !important;
              }
              .row-gap-lg-1 {
                row-gap: 0.25rem !important;
              }
              .row-gap-lg-2 {
                row-gap: 0.5rem !important;
              }
              .row-gap-lg-3 {
                row-gap: 1rem !important;
              }
              .row-gap-lg-4 {
                row-gap: 1.5rem !important;
              }
              .row-gap-lg-5 {
                row-gap: 3rem !important;
              }
              .column-gap-lg-0 {
                -moz-column-gap: 0 !important;
                column-gap: 0 !important;
              }
              .column-gap-lg-1 {
                -moz-column-gap: 0.25rem !important;
                column-gap: 0.25rem !important;
              }
              .column-gap-lg-2 {
                -moz-column-gap: 0.5rem !important;
                column-gap: 0.5rem !important;
              }
              .column-gap-lg-3 {
                -moz-column-gap: 1rem !important;
                column-gap: 1rem !important;
              }
              .column-gap-lg-4 {
                -moz-column-gap: 1.5rem !important;
                column-gap: 1.5rem !important;
              }
              .column-gap-lg-5 {
                -moz-column-gap: 3rem !important;
                column-gap: 3rem !important;
              }
              .text-lg-start {
                text-align: left !important;
              }
              .text-lg-end {
                text-align: right !important;
              }
              .text-lg-center {
                text-align: center !important;
              }
            }
            @media (min-width: 1200px) {
              .float-xl-start {
                float: left !important;
              }
              .float-xl-end {
                float: right !important;
              }
              .float-xl-none {
                float: none !important;
              }
              .object-fit-xl-contain {
                -o-object-fit: contain !important;
                object-fit: contain !important;
              }
              .object-fit-xl-cover {
                -o-object-fit: cover !important;
                object-fit: cover !important;
              }
              .object-fit-xl-fill {
                -o-object-fit: fill !important;
                object-fit: fill !important;
              }
              .object-fit-xl-scale {
                -o-object-fit: scale-down !important;
                object-fit: scale-down !important;
              }
              .object-fit-xl-none {
                -o-object-fit: none !important;
                object-fit: none !important;
              }
              .d-xl-inline {
                display: inline !important;
              }
              .d-xl-inline-block {
                display: inline-block !important;
              }
              .d-xl-block {
                display: block !important;
              }
              .d-xl-grid {
                display: grid !important;
              }
              .d-xl-table {
                display: table !important;
              }
              .d-xl-table-row {
                display: table-row !important;
              }
              .d-xl-table-cell {
                display: table-cell !important;
              }
              .d-xl-flex {
                display: flex !important;
              }
              .d-xl-inline-flex {
                display: inline-flex !important;
              }
              .d-xl-none {
                display: none !important;
              }
              .flex-xl-fill {
                flex: 1 1 auto !important;
              }
              .flex-xl-row {
                flex-direction: row !important;
              }
              .flex-xl-column {
                flex-direction: column !important;
              }
              .flex-xl-row-reverse {
                flex-direction: row-reverse !important;
              }
              .flex-xl-column-reverse {
                flex-direction: column-reverse !important;
              }
              .flex-xl-grow-0 {
                flex-grow: 0 !important;
              }
              .flex-xl-grow-1 {
                flex-grow: 1 !important;
              }
              .flex-xl-shrink-0 {
                flex-shrink: 0 !important;
              }
              .flex-xl-shrink-1 {
                flex-shrink: 1 !important;
              }
              .flex-xl-wrap {
                flex-wrap: wrap !important;
              }
              .flex-xl-nowrap {
                flex-wrap: nowrap !important;
              }
              .flex-xl-wrap-reverse {
                flex-wrap: wrap-reverse !important;
              }
              .justify-content-xl-start {
                justify-content: flex-start !important;
              }
              .justify-content-xl-end {
                justify-content: flex-end !important;
              }
              .justify-content-xl-center {
                justify-content: center !important;
              }
              .justify-content-xl-between {
                justify-content: space-between !important;
              }
              .justify-content-xl-around {
                justify-content: space-around !important;
              }
              .justify-content-xl-evenly {
                justify-content: space-evenly !important;
              }
              .align-items-xl-start {
                align-items: flex-start !important;
              }
              .align-items-xl-end {
                align-items: flex-end !important;
              }
              .align-items-xl-center {
                align-items: center !important;
              }
              .align-items-xl-baseline {
                align-items: baseline !important;
              }
              .align-items-xl-stretch {
                align-items: stretch !important;
              }
              .align-content-xl-start {
                align-content: flex-start !important;
              }
              .align-content-xl-end {
                align-content: flex-end !important;
              }
              .align-content-xl-center {
                align-content: center !important;
              }
              .align-content-xl-between {
                align-content: space-between !important;
              }
              .align-content-xl-around {
                align-content: space-around !important;
              }
              .align-content-xl-stretch {
                align-content: stretch !important;
              }
              .align-self-xl-auto {
                align-self: auto !important;
              }
              .align-self-xl-start {
                align-self: flex-start !important;
              }
              .align-self-xl-end {
                align-self: flex-end !important;
              }
              .align-self-xl-center {
                align-self: center !important;
              }
              .align-self-xl-baseline {
                align-self: baseline !important;
              }
              .align-self-xl-stretch {
                align-self: stretch !important;
              }
              .order-xl-first {
                order: -1 !important;
              }
              .order-xl-0 {
                order: 0 !important;
              }
              .order-xl-1 {
                order: 1 !important;
              }
              .order-xl-2 {
                order: 2 !important;
              }
              .order-xl-3 {
                order: 3 !important;
              }
              .order-xl-4 {
                order: 4 !important;
              }
              .order-xl-5 {
                order: 5 !important;
              }
              .order-xl-last {
                order: 6 !important;
              }
              .m-xl-0 {
                margin: 0 !important;
              }
              .m-xl-1 {
                margin: 0.25rem !important;
              }
              .m-xl-2 {
                margin: 0.5rem !important;
              }
              .m-xl-3 {
                margin: 1rem !important;
              }
              .m-xl-4 {
                margin: 1.5rem !important;
              }
              .m-xl-5 {
                margin: 3rem !important;
              }
              .m-xl-auto {
                margin: auto !important;
              }
              .mx-xl-0 {
                margin-right: 0 !important;
                margin-left: 0 !important;
              }
              .mx-xl-1 {
                margin-right: 0.25rem !important;
                margin-left: 0.25rem !important;
              }
              .mx-xl-2 {
                margin-right: 0.5rem !important;
                margin-left: 0.5rem !important;
              }
              .mx-xl-3 {
                margin-right: 1rem !important;
                margin-left: 1rem !important;
              }
              .mx-xl-4 {
                margin-right: 1.5rem !important;
                margin-left: 1.5rem !important;
              }
              .mx-xl-5 {
                margin-right: 3rem !important;
                margin-left: 3rem !important;
              }
              .mx-xl-auto {
                margin-right: auto !important;
                margin-left: auto !important;
              }
              .my-xl-0 {
                margin-top: 0 !important;
                margin-bottom: 0 !important;
              }
              .my-xl-1 {
                margin-top: 0.25rem !important;
                margin-bottom: 0.25rem !important;
              }
              .my-xl-2 {
                margin-top: 0.5rem !important;
                margin-bottom: 0.5rem !important;
              }
              .my-xl-3 {
                margin-top: 1rem !important;
                margin-bottom: 1rem !important;
              }
              .my-xl-4 {
                margin-top: 1.5rem !important;
                margin-bottom: 1.5rem !important;
              }
              .my-xl-5 {
                margin-top: 3rem !important;
                margin-bottom: 3rem !important;
              }
              .my-xl-auto {
                margin-top: auto !important;
                margin-bottom: auto !important;
              }
              .mt-xl-0 {
                margin-top: 0 !important;
              }
              .mt-xl-1 {
                margin-top: 0.25rem !important;
              }
              .mt-xl-2 {
                margin-top: 0.5rem !important;
              }
              .mt-xl-3 {
                margin-top: 1rem !important;
              }
              .mt-xl-4 {
                margin-top: 1.5rem !important;
              }
              .mt-xl-5 {
                margin-top: 3rem !important;
              }
              .mt-xl-auto {
                margin-top: auto !important;
              }
              .me-xl-0 {
                margin-right: 0 !important;
              }
              .me-xl-1 {
                margin-right: 0.25rem !important;
              }
              .me-xl-2 {
                margin-right: 0.5rem !important;
              }
              .me-xl-3 {
                margin-right: 1rem !important;
              }
              .me-xl-4 {
                margin-right: 1.5rem !important;
              }
              .me-xl-5 {
                margin-right: 3rem !important;
              }
              .me-xl-auto {
                margin-right: auto !important;
              }
              .mb-xl-0 {
                margin-bottom: 0 !important;
              }
              .mb-xl-1 {
                margin-bottom: 0.25rem !important;
              }
              .mb-xl-2 {
                margin-bottom: 0.5rem !important;
              }
              .mb-xl-3 {
                margin-bottom: 1rem !important;
              }
              .mb-xl-4 {
                margin-bottom: 1.5rem !important;
              }
              .mb-xl-5 {
                margin-bottom: 3rem !important;
              }
              .mb-xl-auto {
                margin-bottom: auto !important;
              }
              .ms-xl-0 {
                margin-left: 0 !important;
              }
              .ms-xl-1 {
                margin-left: 0.25rem !important;
              }
              .ms-xl-2 {
                margin-left: 0.5rem !important;
              }
              .ms-xl-3 {
                margin-left: 1rem !important;
              }
              .ms-xl-4 {
                margin-left: 1.5rem !important;
              }
              .ms-xl-5 {
                margin-left: 3rem !important;
              }
              .ms-xl-auto {
                margin-left: auto !important;
              }
              .p-xl-0 {
                padding: 0 !important;
              }
              .p-xl-1 {
                padding: 0.25rem !important;
              }
              .p-xl-2 {
                padding: 0.5rem !important;
              }
              .p-xl-3 {
                padding: 1rem !important;
              }
              .p-xl-4 {
                padding: 1.5rem !important;
              }
              .p-xl-5 {
                padding: 3rem !important;
              }
              .px-xl-0 {
                padding-right: 0 !important;
                padding-left: 0 !important;
              }
              .px-xl-1 {
                padding-right: 0.25rem !important;
                padding-left: 0.25rem !important;
              }
              .px-xl-2 {
                padding-right: 0.5rem !important;
                padding-left: 0.5rem !important;
              }
              .px-xl-3 {
                padding-right: 1rem !important;
                padding-left: 1rem !important;
              }
              .px-xl-4 {
                padding-right: 1.5rem !important;
                padding-left: 1.5rem !important;
              }
              .px-xl-5 {
                padding-right: 3rem !important;
                padding-left: 3rem !important;
              }
              .py-xl-0 {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
              }
              .py-xl-1 {
                padding-top: 0.25rem !important;
                padding-bottom: 0.25rem !important;
              }
              .py-xl-2 {
                padding-top: 0.5rem !important;
                padding-bottom: 0.5rem !important;
              }
              .py-xl-3 {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
              }
              .py-xl-4 {
                padding-top: 1.5rem !important;
                padding-bottom: 1.5rem !important;
              }
              .py-xl-5 {
                padding-top: 3rem !important;
                padding-bottom: 3rem !important;
              }
              .pt-xl-0 {
                padding-top: 0 !important;
              }
              .pt-xl-1 {
                padding-top: 0.25rem !important;
              }
              .pt-xl-2 {
                padding-top: 0.5rem !important;
              }
              .pt-xl-3 {
                padding-top: 1rem !important;
              }
              .pt-xl-4 {
                padding-top: 1.5rem !important;
              }
              .pt-xl-5 {
                padding-top: 3rem !important;
              }
              .pe-xl-0 {
                padding-right: 0 !important;
              }
              .pe-xl-1 {
                padding-right: 0.25rem !important;
              }
              .pe-xl-2 {
                padding-right: 0.5rem !important;
              }
              .pe-xl-3 {
                padding-right: 1rem !important;
              }
              .pe-xl-4 {
                padding-right: 1.5rem !important;
              }
              .pe-xl-5 {
                padding-right: 3rem !important;
              }
              .pb-xl-0 {
                padding-bottom: 0 !important;
              }
              .pb-xl-1 {
                padding-bottom: 0.25rem !important;
              }
              .pb-xl-2 {
                padding-bottom: 0.5rem !important;
              }
              .pb-xl-3 {
                padding-bottom: 1rem !important;
              }
              .pb-xl-4 {
                padding-bottom: 1.5rem !important;
              }
              .pb-xl-5 {
                padding-bottom: 3rem !important;
              }
              .ps-xl-0 {
                padding-left: 0 !important;
              }
              .ps-xl-1 {
                padding-left: 0.25rem !important;
              }
              .ps-xl-2 {
                padding-left: 0.5rem !important;
              }
              .ps-xl-3 {
                padding-left: 1rem !important;
              }
              .ps-xl-4 {
                padding-left: 1.5rem !important;
              }
              .ps-xl-5 {
                padding-left: 3rem !important;
              }
              .gap-xl-0 {
                gap: 0 !important;
              }
              .gap-xl-1 {
                gap: 0.25rem !important;
              }
              .gap-xl-2 {
                gap: 0.5rem !important;
              }
              .gap-xl-3 {
                gap: 1rem !important;
              }
              .gap-xl-4 {
                gap: 1.5rem !important;
              }
              .gap-xl-5 {
                gap: 3rem !important;
              }
              .row-gap-xl-0 {
                row-gap: 0 !important;
              }
              .row-gap-xl-1 {
                row-gap: 0.25rem !important;
              }
              .row-gap-xl-2 {
                row-gap: 0.5rem !important;
              }
              .row-gap-xl-3 {
                row-gap: 1rem !important;
              }
              .row-gap-xl-4 {
                row-gap: 1.5rem !important;
              }
              .row-gap-xl-5 {
                row-gap: 3rem !important;
              }
              .column-gap-xl-0 {
                -moz-column-gap: 0 !important;
                column-gap: 0 !important;
              }
              .column-gap-xl-1 {
                -moz-column-gap: 0.25rem !important;
                column-gap: 0.25rem !important;
              }
              .column-gap-xl-2 {
                -moz-column-gap: 0.5rem !important;
                column-gap: 0.5rem !important;
              }
              .column-gap-xl-3 {
                -moz-column-gap: 1rem !important;
                column-gap: 1rem !important;
              }
              .column-gap-xl-4 {
                -moz-column-gap: 1.5rem !important;
                column-gap: 1.5rem !important;
              }
              .column-gap-xl-5 {
                -moz-column-gap: 3rem !important;
                column-gap: 3rem !important;
              }
              .text-xl-start {
                text-align: left !important;
              }
              .text-xl-end {
                text-align: right !important;
              }
              .text-xl-center {
                text-align: center !important;
              }
            }
            @media (min-width: 1400px) {
              .float-xxl-start {
                float: left !important;
              }
              .float-xxl-end {
                float: right !important;
              }
              .float-xxl-none {
                float: none !important;
              }
              .object-fit-xxl-contain {
                -o-object-fit: contain !important;
                object-fit: contain !important;
              }
              .object-fit-xxl-cover {
                -o-object-fit: cover !important;
                object-fit: cover !important;
              }
              .object-fit-xxl-fill {
                -o-object-fit: fill !important;
                object-fit: fill !important;
              }
              .object-fit-xxl-scale {
                -o-object-fit: scale-down !important;
                object-fit: scale-down !important;
              }
              .object-fit-xxl-none {
                -o-object-fit: none !important;
                object-fit: none !important;
              }
              .d-xxl-inline {
                display: inline !important;
              }
              .d-xxl-inline-block {
                display: inline-block !important;
              }
              .d-xxl-block {
                display: block !important;
              }
              .d-xxl-grid {
                display: grid !important;
              }
              .d-xxl-table {
                display: table !important;
              }
              .d-xxl-table-row {
                display: table-row !important;
              }
              .d-xxl-table-cell {
                display: table-cell !important;
              }
              .d-xxl-flex {
                display: flex !important;
              }
              .d-xxl-inline-flex {
                display: inline-flex !important;
              }
              .d-xxl-none {
                display: none !important;
              }
              .flex-xxl-fill {
                flex: 1 1 auto !important;
              }
              .flex-xxl-row {
                flex-direction: row !important;
              }
              .flex-xxl-column {
                flex-direction: column !important;
              }
              .flex-xxl-row-reverse {
                flex-direction: row-reverse !important;
              }
              .flex-xxl-column-reverse {
                flex-direction: column-reverse !important;
              }
              .flex-xxl-grow-0 {
                flex-grow: 0 !important;
              }
              .flex-xxl-grow-1 {
                flex-grow: 1 !important;
              }
              .flex-xxl-shrink-0 {
                flex-shrink: 0 !important;
              }
              .flex-xxl-shrink-1 {
                flex-shrink: 1 !important;
              }
              .flex-xxl-wrap {
                flex-wrap: wrap !important;
              }
              .flex-xxl-nowrap {
                flex-wrap: nowrap !important;
              }
              .flex-xxl-wrap-reverse {
                flex-wrap: wrap-reverse !important;
              }
              .justify-content-xxl-start {
                justify-content: flex-start !important;
              }
              .justify-content-xxl-end {
                justify-content: flex-end !important;
              }
              .justify-content-xxl-center {
                justify-content: center !important;
              }
              .justify-content-xxl-between {
                justify-content: space-between !important;
              }
              .justify-content-xxl-around {
                justify-content: space-around !important;
              }
              .justify-content-xxl-evenly {
                justify-content: space-evenly !important;
              }
              .align-items-xxl-start {
                align-items: flex-start !important;
              }
              .align-items-xxl-end {
                align-items: flex-end !important;
              }
              .align-items-xxl-center {
                align-items: center !important;
              }
              .align-items-xxl-baseline {
                align-items: baseline !important;
              }
              .align-items-xxl-stretch {
                align-items: stretch !important;
              }
              .align-content-xxl-start {
                align-content: flex-start !important;
              }
              .align-content-xxl-end {
                align-content: flex-end !important;
              }
              .align-content-xxl-center {
                align-content: center !important;
              }
              .align-content-xxl-between {
                align-content: space-between !important;
              }
              .align-content-xxl-around {
                align-content: space-around !important;
              }
              .align-content-xxl-stretch {
                align-content: stretch !important;
              }
              .align-self-xxl-auto {
                align-self: auto !important;
              }
              .align-self-xxl-start {
                align-self: flex-start !important;
              }
              .align-self-xxl-end {
                align-self: flex-end !important;
              }
              .align-self-xxl-center {
                align-self: center !important;
              }
              .align-self-xxl-baseline {
                align-self: baseline !important;
              }
              .align-self-xxl-stretch {
                align-self: stretch !important;
              }
              .order-xxl-first {
                order: -1 !important;
              }
              .order-xxl-0 {
                order: 0 !important;
              }
              .order-xxl-1 {
                order: 1 !important;
              }
              .order-xxl-2 {
                order: 2 !important;
              }
              .order-xxl-3 {
                order: 3 !important;
              }
              .order-xxl-4 {
                order: 4 !important;
              }
              .order-xxl-5 {
                order: 5 !important;
              }
              .order-xxl-last {
                order: 6 !important;
              }
              .m-xxl-0 {
                margin: 0 !important;
              }
              .m-xxl-1 {
                margin: 0.25rem !important;
              }
              .m-xxl-2 {
                margin: 0.5rem !important;
              }
              .m-xxl-3 {
                margin: 1rem !important;
              }
              .m-xxl-4 {
                margin: 1.5rem !important;
              }
              .m-xxl-5 {
                margin: 3rem !important;
              }
              .m-xxl-auto {
                margin: auto !important;
              }
              .mx-xxl-0 {
                margin-right: 0 !important;
                margin-left: 0 !important;
              }
              .mx-xxl-1 {
                margin-right: 0.25rem !important;
                margin-left: 0.25rem !important;
              }
              .mx-xxl-2 {
                margin-right: 0.5rem !important;
                margin-left: 0.5rem !important;
              }
              .mx-xxl-3 {
                margin-right: 1rem !important;
                margin-left: 1rem !important;
              }
              .mx-xxl-4 {
                margin-right: 1.5rem !important;
                margin-left: 1.5rem !important;
              }
              .mx-xxl-5 {
                margin-right: 3rem !important;
                margin-left: 3rem !important;
              }
              .mx-xxl-auto {
                margin-right: auto !important;
                margin-left: auto !important;
              }
              .my-xxl-0 {
                margin-top: 0 !important;
                margin-bottom: 0 !important;
              }
              .my-xxl-1 {
                margin-top: 0.25rem !important;
                margin-bottom: 0.25rem !important;
              }
              .my-xxl-2 {
                margin-top: 0.5rem !important;
                margin-bottom: 0.5rem !important;
              }
              .my-xxl-3 {
                margin-top: 1rem !important;
                margin-bottom: 1rem !important;
              }
              .my-xxl-4 {
                margin-top: 1.5rem !important;
                margin-bottom: 1.5rem !important;
              }
              .my-xxl-5 {
                margin-top: 3rem !important;
                margin-bottom: 3rem !important;
              }
              .my-xxl-auto {
                margin-top: auto !important;
                margin-bottom: auto !important;
              }
              .mt-xxl-0 {
                margin-top: 0 !important;
              }
              .mt-xxl-1 {
                margin-top: 0.25rem !important;
              }
              .mt-xxl-2 {
                margin-top: 0.5rem !important;
              }
              .mt-xxl-3 {
                margin-top: 1rem !important;
              }
              .mt-xxl-4 {
                margin-top: 1.5rem !important;
              }
              .mt-xxl-5 {
                margin-top: 3rem !important;
              }
              .mt-xxl-auto {
                margin-top: auto !important;
              }
              .me-xxl-0 {
                margin-right: 0 !important;
              }
              .me-xxl-1 {
                margin-right: 0.25rem !important;
              }
              .me-xxl-2 {
                margin-right: 0.5rem !important;
              }
              .me-xxl-3 {
                margin-right: 1rem !important;
              }
              .me-xxl-4 {
                margin-right: 1.5rem !important;
              }
              .me-xxl-5 {
                margin-right: 3rem !important;
              }
              .me-xxl-auto {
                margin-right: auto !important;
              }
              .mb-xxl-0 {
                margin-bottom: 0 !important;
              }
              .mb-xxl-1 {
                margin-bottom: 0.25rem !important;
              }
              .mb-xxl-2 {
                margin-bottom: 0.5rem !important;
              }
              .mb-xxl-3 {
                margin-bottom: 1rem !important;
              }
              .mb-xxl-4 {
                margin-bottom: 1.5rem !important;
              }
              .mb-xxl-5 {
                margin-bottom: 3rem !important;
              }
              .mb-xxl-auto {
                margin-bottom: auto !important;
              }
              .ms-xxl-0 {
                margin-left: 0 !important;
              }
              .ms-xxl-1 {
                margin-left: 0.25rem !important;
              }
              .ms-xxl-2 {
                margin-left: 0.5rem !important;
              }
              .ms-xxl-3 {
                margin-left: 1rem !important;
              }
              .ms-xxl-4 {
                margin-left: 1.5rem !important;
              }
              .ms-xxl-5 {
                margin-left: 3rem !important;
              }
              .ms-xxl-auto {
                margin-left: auto !important;
              }
              .p-xxl-0 {
                padding: 0 !important;
              }
              .p-xxl-1 {
                padding: 0.25rem !important;
              }
              .p-xxl-2 {
                padding: 0.5rem !important;
              }
              .p-xxl-3 {
                padding: 1rem !important;
              }
              .p-xxl-4 {
                padding: 1.5rem !important;
              }
              .p-xxl-5 {
                padding: 3rem !important;
              }
              .px-xxl-0 {
                padding-right: 0 !important;
                padding-left: 0 !important;
              }
              .px-xxl-1 {
                padding-right: 0.25rem !important;
                padding-left: 0.25rem !important;
              }
              .px-xxl-2 {
                padding-right: 0.5rem !important;
                padding-left: 0.5rem !important;
              }
              .px-xxl-3 {
                padding-right: 1rem !important;
                padding-left: 1rem !important;
              }
              .px-xxl-4 {
                padding-right: 1.5rem !important;
                padding-left: 1.5rem !important;
              }
              .px-xxl-5 {
                padding-right: 3rem !important;
                padding-left: 3rem !important;
              }
              .py-xxl-0 {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
              }
              .py-xxl-1 {
                padding-top: 0.25rem !important;
                padding-bottom: 0.25rem !important;
              }
              .py-xxl-2 {
                padding-top: 0.5rem !important;
                padding-bottom: 0.5rem !important;
              }
              .py-xxl-3 {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
              }
              .py-xxl-4 {
                padding-top: 1.5rem !important;
                padding-bottom: 1.5rem !important;
              }
              .py-xxl-5 {
                padding-top: 3rem !important;
                padding-bottom: 3rem !important;
              }
              .pt-xxl-0 {
                padding-top: 0 !important;
              }
              .pt-xxl-1 {
                padding-top: 0.25rem !important;
              }
              .pt-xxl-2 {
                padding-top: 0.5rem !important;
              }
              .pt-xxl-3 {
                padding-top: 1rem !important;
              }
              .pt-xxl-4 {
                padding-top: 1.5rem !important;
              }
              .pt-xxl-5 {
                padding-top: 3rem !important;
              }
              .pe-xxl-0 {
                padding-right: 0 !important;
              }
              .pe-xxl-1 {
                padding-right: 0.25rem !important;
              }
              .pe-xxl-2 {
                padding-right: 0.5rem !important;
              }
              .pe-xxl-3 {
                padding-right: 1rem !important;
              }
              .pe-xxl-4 {
                padding-right: 1.5rem !important;
              }
              .pe-xxl-5 {
                padding-right: 3rem !important;
              }
              .pb-xxl-0 {
                padding-bottom: 0 !important;
              }
              .pb-xxl-1 {
                padding-bottom: 0.25rem !important;
              }
              .pb-xxl-2 {
                padding-bottom: 0.5rem !important;
              }
              .pb-xxl-3 {
                padding-bottom: 1rem !important;
              }
              .pb-xxl-4 {
                padding-bottom: 1.5rem !important;
              }
              .pb-xxl-5 {
                padding-bottom: 3rem !important;
              }
              .ps-xxl-0 {
                padding-left: 0 !important;
              }
              .ps-xxl-1 {
                padding-left: 0.25rem !important;
              }
              .ps-xxl-2 {
                padding-left: 0.5rem !important;
              }
              .ps-xxl-3 {
                padding-left: 1rem !important;
              }
              .ps-xxl-4 {
                padding-left: 1.5rem !important;
              }
              .ps-xxl-5 {
                padding-left: 3rem !important;
              }
              .gap-xxl-0 {
                gap: 0 !important;
              }
              .gap-xxl-1 {
                gap: 0.25rem !important;
              }
              .gap-xxl-2 {
                gap: 0.5rem !important;
              }
              .gap-xxl-3 {
                gap: 1rem !important;
              }
              .gap-xxl-4 {
                gap: 1.5rem !important;
              }
              .gap-xxl-5 {
                gap: 3rem !important;
              }
              .row-gap-xxl-0 {
                row-gap: 0 !important;
              }
              .row-gap-xxl-1 {
                row-gap: 0.25rem !important;
              }
              .row-gap-xxl-2 {
                row-gap: 0.5rem !important;
              }
              .row-gap-xxl-3 {
                row-gap: 1rem !important;
              }
              .row-gap-xxl-4 {
                row-gap: 1.5rem !important;
              }
              .row-gap-xxl-5 {
                row-gap: 3rem !important;
              }
              .column-gap-xxl-0 {
                -moz-column-gap: 0 !important;
                column-gap: 0 !important;
              }
              .column-gap-xxl-1 {
                -moz-column-gap: 0.25rem !important;
                column-gap: 0.25rem !important;
              }
              .column-gap-xxl-2 {
                -moz-column-gap: 0.5rem !important;
                column-gap: 0.5rem !important;
              }
              .column-gap-xxl-3 {
                -moz-column-gap: 1rem !important;
                column-gap: 1rem !important;
              }
              .column-gap-xxl-4 {
                -moz-column-gap: 1.5rem !important;
                column-gap: 1.5rem !important;
              }
              .column-gap-xxl-5 {
                -moz-column-gap: 3rem !important;
                column-gap: 3rem !important;
              }
              .text-xxl-start {
                text-align: left !important;
              }
              .text-xxl-end {
                text-align: right !important;
              }
              .text-xxl-center {
                text-align: center !important;
              }
            }
            @media (min-width: 1200px) {
              .fs-1 {
                font-size: 2.5rem !important;
              }
              .fs-2 {
                font-size: 2rem !important;
              }
              .fs-3 {
                font-size: 1.75rem !important;
              }
              .fs-4 {
                font-size: 1.5rem !important;
              }
            }
            @media print {
              .d-print-inline {
                display: inline !important;
              }
              .d-print-inline-block {
                display: inline-block !important;
              }
              .d-print-block {
                display: block !important;
              }
              .d-print-grid {
                display: grid !important;
              }
              .d-print-table {
                display: table !important;
              }
              .d-print-table-row {
                display: table-row !important;
              }
              .d-print-table-cell {
                display: table-cell !important;
              }
              .d-print-flex {
                display: flex !important;
              }
              .d-print-inline-flex {
                display: inline-flex !important;
              }
              .d-print-none {
                display: none !important;
              }
            }

            /*# sourceMappingURL=bootstrap.css.map */
        </style>
        """
    st.markdown(boostrap_css, unsafe_allow_html=True)

    boostrap_js = """
    <script type='text/javascript'>
        /*!
          * Bootstrap v5.3.0-alpha2 (https://getbootstrap.com/)
          * Copyright 2011-2023 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
          * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
          */
        (function (global, factory) {
          typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory(require('@popperjs/core')) :
          typeof define === 'function' && define.amd ? define(['@popperjs/core'], factory) :
          (global = typeof globalThis !== 'undefined' ? globalThis : global || self, global.bootstrap = factory(global.Popper));
        })(this, (function (Popper) { 'use strict';

          function _interopNamespaceDefault(e) {
            const n = Object.create(null, { [Symbol.toStringTag]: { value: 'Module' } });
            if (e) {
              for (const k in e) {
                if (k !== 'default') {
                  const d = Object.getOwnPropertyDescriptor(e, k);
                  Object.defineProperty(n, k, d.get ? d : {
                    enumerable: true,
                    get: () => e[k]
                  });
                }
              }
            }
            n.default = e;
            return Object.freeze(n);
          }

          const Popper__namespace = /*#__PURE__*/_interopNamespaceDefault(Popper);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/index.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          const MAX_UID = 1000000;
          const MILLISECONDS_MULTIPLIER = 1000;
          const TRANSITION_END = 'transitionend';

          /**
           * Properly escape IDs selectors to handle weird IDs
           * @param {string} selector
           * @returns {string}
           */
          const parseSelector = selector => {
            if (selector && window.CSS && window.CSS.escape) {
              // document.querySelector needs escaping to handle IDs (html5+) containing for instance /
              selector = selector.replace(/#([^\s"#']+)/g, (match, id) => `#${CSS.escape(id)}`);
            }
            return selector;
          };

          // Shout-out Angus Croll (https://goo.gl/pxwQGp)
          const toType = object => {
            if (object === null || object === undefined) {
              return `${object}`;
            }
            return Object.prototype.toString.call(object).match(/\s([a-z]+)/i)[1].toLowerCase();
          };

          /**
           * Public Util API
           */

          const getUID = prefix => {
            do {
              prefix += Math.floor(Math.random() * MAX_UID);
            } while (document.getElementById(prefix));
            return prefix;
          };
          const getTransitionDurationFromElement = element => {
            if (!element) {
              return 0;
            }

            // Get transition-duration of the element
            let {
              transitionDuration,
              transitionDelay
            } = window.getComputedStyle(element);
            const floatTransitionDuration = Number.parseFloat(transitionDuration);
            const floatTransitionDelay = Number.parseFloat(transitionDelay);

            // Return 0 if element or transition duration is not found
            if (!floatTransitionDuration && !floatTransitionDelay) {
              return 0;
            }

            // If multiple durations are defined, take the first
            transitionDuration = transitionDuration.split(',')[0];
            transitionDelay = transitionDelay.split(',')[0];
            return (Number.parseFloat(transitionDuration) + Number.parseFloat(transitionDelay)) * MILLISECONDS_MULTIPLIER;
          };
          const triggerTransitionEnd = element => {
            element.dispatchEvent(new Event(TRANSITION_END));
          };
          const isElement = object => {
            if (!object || typeof object !== 'object') {
              return false;
            }
            if (typeof object.jquery !== 'undefined') {
              object = object[0];
            }
            return typeof object.nodeType !== 'undefined';
          };
          const getElement = object => {
            // it's a jQuery object or a node element
            if (isElement(object)) {
              return object.jquery ? object[0] : object;
            }
            if (typeof object === 'string' && object.length > 0) {
              return document.querySelector(parseSelector(object));
            }
            return null;
          };
          const isVisible = element => {
            if (!isElement(element) || element.getClientRects().length === 0) {
              return false;
            }
            const elementIsVisible = getComputedStyle(element).getPropertyValue('visibility') === 'visible';
            // Handle `details` element as its content may falsie appear visible when it is closed
            const closedDetails = element.closest('details:not([open])');
            if (!closedDetails) {
              return elementIsVisible;
            }
            if (closedDetails !== element) {
              const summary = element.closest('summary');
              if (summary && summary.parentNode !== closedDetails) {
                return false;
              }
              if (summary === null) {
                return false;
              }
            }
            return elementIsVisible;
          };
          const isDisabled = element => {
            if (!element || element.nodeType !== Node.ELEMENT_NODE) {
              return true;
            }
            if (element.classList.contains('disabled')) {
              return true;
            }
            if (typeof element.disabled !== 'undefined') {
              return element.disabled;
            }
            return element.hasAttribute('disabled') && element.getAttribute('disabled') !== 'false';
          };
          const findShadowRoot = element => {
            if (!document.documentElement.attachShadow) {
              return null;
            }

            // Can find the shadow root otherwise it'll return the document
            if (typeof element.getRootNode === 'function') {
              const root = element.getRootNode();
              return root instanceof ShadowRoot ? root : null;
            }
            if (element instanceof ShadowRoot) {
              return element;
            }

            // when we don't find a shadow root
            if (!element.parentNode) {
              return null;
            }
            return findShadowRoot(element.parentNode);
          };
          const noop = () => {};

          /**
           * Trick to restart an element's animation
           *
           * @param {HTMLElement} element
           * @return void
           *
           * @see https://www.charistheo.io/blog/2021/02/restart-a-css-animation-with-javascript/#restarting-a-css-animation
           */
          const reflow = element => {
            element.offsetHeight; // eslint-disable-line no-unused-expressions
          };

          const getjQuery = () => {
            if (window.jQuery && !document.body.hasAttribute('data-bs-no-jquery')) {
              return window.jQuery;
            }
            return null;
          };
          const DOMContentLoadedCallbacks = [];
          const onDOMContentLoaded = callback => {
            if (document.readyState === 'loading') {
              // add listener on the first call when the document is in loading state
              if (!DOMContentLoadedCallbacks.length) {
                document.addEventListener('DOMContentLoaded', () => {
                  for (const callback of DOMContentLoadedCallbacks) {
                    callback();
                  }
                });
              }
              DOMContentLoadedCallbacks.push(callback);
            } else {
              callback();
            }
          };
          const isRTL = () => document.documentElement.dir === 'rtl';
          const defineJQueryPlugin = plugin => {
            onDOMContentLoaded(() => {
              const $ = getjQuery();
              /* istanbul ignore if */
              if ($) {
                const name = plugin.NAME;
                const JQUERY_NO_CONFLICT = $.fn[name];
                $.fn[name] = plugin.jQueryInterface;
                $.fn[name].Constructor = plugin;
                $.fn[name].noConflict = () => {
                  $.fn[name] = JQUERY_NO_CONFLICT;
                  return plugin.jQueryInterface;
                };
              }
            });
          };
          const execute = (possibleCallback, args = [], defaultValue = possibleCallback) => {
            return typeof possibleCallback === 'function' ? possibleCallback(...args) : defaultValue;
          };
          const executeAfterTransition = (callback, transitionElement, waitForTransition = true) => {
            if (!waitForTransition) {
              execute(callback);
              return;
            }
            const durationPadding = 5;
            const emulatedDuration = getTransitionDurationFromElement(transitionElement) + durationPadding;
            let called = false;
            const handler = ({
              target
            }) => {
              if (target !== transitionElement) {
                return;
              }
              called = true;
              transitionElement.removeEventListener(TRANSITION_END, handler);
              execute(callback);
            };
            transitionElement.addEventListener(TRANSITION_END, handler);
            setTimeout(() => {
              if (!called) {
                triggerTransitionEnd(transitionElement);
              }
            }, emulatedDuration);
          };

          /**
           * Return the previous/next element of a list.
           *
           * @param {array} list    The list of elements
           * @param activeElement   The active element
           * @param shouldGetNext   Choose to get next or previous element
           * @param isCycleAllowed
           * @return {Element|elem} The proper element
           */
          const getNextActiveElement = (list, activeElement, shouldGetNext, isCycleAllowed) => {
            const listLength = list.length;
            let index = list.indexOf(activeElement);

            // if the element does not exist in the list return an element
            // depending on the direction and if cycle is allowed
            if (index === -1) {
              return !shouldGetNext && isCycleAllowed ? list[listLength - 1] : list[0];
            }
            index += shouldGetNext ? 1 : -1;
            if (isCycleAllowed) {
              index = (index + listLength) % listLength;
            }
            return list[Math.max(0, Math.min(index, listLength - 1))];
          };

          /**
           * --------------------------------------------------------------------------
           * Bootstrap dom/event-handler.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const namespaceRegex = /[^.]*(?=\..*)\.|.*/;
          const stripNameRegex = /\..*/;
          const stripUidRegex = /::\d+$/;
          const eventRegistry = {}; // Events storage
          let uidEvent = 1;
          const customEvents = {
            mouseenter: 'mouseover',
            mouseleave: 'mouseout'
          };
          const nativeEvents = new Set(['click', 'dblclick', 'mouseup', 'mousedown', 'contextmenu', 'mousewheel', 'DOMMouseScroll', 'mouseover', 'mouseout', 'mousemove', 'selectstart', 'selectend', 'keydown', 'keypress', 'keyup', 'orientationchange', 'touchstart', 'touchmove', 'touchend', 'touchcancel', 'pointerdown', 'pointermove', 'pointerup', 'pointerleave', 'pointercancel', 'gesturestart', 'gesturechange', 'gestureend', 'focus', 'blur', 'change', 'reset', 'select', 'submit', 'focusin', 'focusout', 'load', 'unload', 'beforeunload', 'resize', 'move', 'DOMContentLoaded', 'readystatechange', 'error', 'abort', 'scroll']);

          /**
           * Private methods
           */

          function makeEventUid(element, uid) {
            return uid && `${uid}::${uidEvent++}` || element.uidEvent || uidEvent++;
          }
          function getElementEvents(element) {
            const uid = makeEventUid(element);
            element.uidEvent = uid;
            eventRegistry[uid] = eventRegistry[uid] || {};
            return eventRegistry[uid];
          }
          function bootstrapHandler(element, fn) {
            return function handler(event) {
              hydrateObj(event, {
                delegateTarget: element
              });
              if (handler.oneOff) {
                EventHandler.off(element, event.type, fn);
              }
              return fn.apply(element, [event]);
            };
          }
          function bootstrapDelegationHandler(element, selector, fn) {
            return function handler(event) {
              const domElements = element.querySelectorAll(selector);
              for (let {
                target
              } = event; target && target !== this; target = target.parentNode) {
                for (const domElement of domElements) {
                  if (domElement !== target) {
                    continue;
                  }
                  hydrateObj(event, {
                    delegateTarget: target
                  });
                  if (handler.oneOff) {
                    EventHandler.off(element, event.type, selector, fn);
                  }
                  return fn.apply(target, [event]);
                }
              }
            };
          }
          function findHandler(events, callable, delegationSelector = null) {
            return Object.values(events).find(event => event.callable === callable && event.delegationSelector === delegationSelector);
          }
          function normalizeParameters(originalTypeEvent, handler, delegationFunction) {
            const isDelegated = typeof handler === 'string';
            // todo: tooltip passes `false` instead of selector, so we need to check
            const callable = isDelegated ? delegationFunction : handler || delegationFunction;
            let typeEvent = getTypeEvent(originalTypeEvent);
            if (!nativeEvents.has(typeEvent)) {
              typeEvent = originalTypeEvent;
            }
            return [isDelegated, callable, typeEvent];
          }
          function addHandler(element, originalTypeEvent, handler, delegationFunction, oneOff) {
            if (typeof originalTypeEvent !== 'string' || !element) {
              return;
            }
            let [isDelegated, callable, typeEvent] = normalizeParameters(originalTypeEvent, handler, delegationFunction);

            // in case of mouseenter or mouseleave wrap the handler within a function that checks for its DOM position
            // this prevents the handler from being dispatched the same way as mouseover or mouseout does
            if (originalTypeEvent in customEvents) {
              const wrapFunction = fn => {
                return function (event) {
                  if (!event.relatedTarget || event.relatedTarget !== event.delegateTarget && !event.delegateTarget.contains(event.relatedTarget)) {
                    return fn.call(this, event);
                  }
                };
              };
              callable = wrapFunction(callable);
            }
            const events = getElementEvents(element);
            const handlers = events[typeEvent] || (events[typeEvent] = {});
            const previousFunction = findHandler(handlers, callable, isDelegated ? handler : null);
            if (previousFunction) {
              previousFunction.oneOff = previousFunction.oneOff && oneOff;
              return;
            }
            const uid = makeEventUid(callable, originalTypeEvent.replace(namespaceRegex, ''));
            const fn = isDelegated ? bootstrapDelegationHandler(element, handler, callable) : bootstrapHandler(element, callable);
            fn.delegationSelector = isDelegated ? handler : null;
            fn.callable = callable;
            fn.oneOff = oneOff;
            fn.uidEvent = uid;
            handlers[uid] = fn;
            element.addEventListener(typeEvent, fn, isDelegated);
          }
          function removeHandler(element, events, typeEvent, handler, delegationSelector) {
            const fn = findHandler(events[typeEvent], handler, delegationSelector);
            if (!fn) {
              return;
            }
            element.removeEventListener(typeEvent, fn, Boolean(delegationSelector));
            delete events[typeEvent][fn.uidEvent];
          }
          function removeNamespacedHandlers(element, events, typeEvent, namespace) {
            const storeElementEvent = events[typeEvent] || {};
            for (const [handlerKey, event] of Object.entries(storeElementEvent)) {
              if (handlerKey.includes(namespace)) {
                removeHandler(element, events, typeEvent, event.callable, event.delegationSelector);
              }
            }
          }
          function getTypeEvent(event) {
            // allow to get the native events from namespaced events ('click.bs.button' --> 'click')
            event = event.replace(stripNameRegex, '');
            return customEvents[event] || event;
          }
          const EventHandler = {
            on(element, event, handler, delegationFunction) {
              addHandler(element, event, handler, delegationFunction, false);
            },
            one(element, event, handler, delegationFunction) {
              addHandler(element, event, handler, delegationFunction, true);
            },
            off(element, originalTypeEvent, handler, delegationFunction) {
              if (typeof originalTypeEvent !== 'string' || !element) {
                return;
              }
              const [isDelegated, callable, typeEvent] = normalizeParameters(originalTypeEvent, handler, delegationFunction);
              const inNamespace = typeEvent !== originalTypeEvent;
              const events = getElementEvents(element);
              const storeElementEvent = events[typeEvent] || {};
              const isNamespace = originalTypeEvent.startsWith('.');
              if (typeof callable !== 'undefined') {
                // Simplest case: handler is passed, remove that listener ONLY.
                if (!Object.keys(storeElementEvent).length) {
                  return;
                }
                removeHandler(element, events, typeEvent, callable, isDelegated ? handler : null);
                return;
              }
              if (isNamespace) {
                for (const elementEvent of Object.keys(events)) {
                  removeNamespacedHandlers(element, events, elementEvent, originalTypeEvent.slice(1));
                }
              }
              for (const [keyHandlers, event] of Object.entries(storeElementEvent)) {
                const handlerKey = keyHandlers.replace(stripUidRegex, '');
                if (!inNamespace || originalTypeEvent.includes(handlerKey)) {
                  removeHandler(element, events, typeEvent, event.callable, event.delegationSelector);
                }
              }
            },
            trigger(element, event, args) {
              if (typeof event !== 'string' || !element) {
                return null;
              }
              const $ = getjQuery();
              const typeEvent = getTypeEvent(event);
              const inNamespace = event !== typeEvent;
              let jQueryEvent = null;
              let bubbles = true;
              let nativeDispatch = true;
              let defaultPrevented = false;
              if (inNamespace && $) {
                jQueryEvent = $.Event(event, args);
                $(element).trigger(jQueryEvent);
                bubbles = !jQueryEvent.isPropagationStopped();
                nativeDispatch = !jQueryEvent.isImmediatePropagationStopped();
                defaultPrevented = jQueryEvent.isDefaultPrevented();
              }
              let evt = new Event(event, {
                bubbles,
                cancelable: true
              });
              evt = hydrateObj(evt, args);
              if (defaultPrevented) {
                evt.preventDefault();
              }
              if (nativeDispatch) {
                element.dispatchEvent(evt);
              }
              if (evt.defaultPrevented && jQueryEvent) {
                jQueryEvent.preventDefault();
              }
              return evt;
            }
          };
          function hydrateObj(obj, meta = {}) {
            for (const [key, value] of Object.entries(meta)) {
              try {
                obj[key] = value;
              } catch (_unused) {
                Object.defineProperty(obj, key, {
                  configurable: true,
                  get() {
                    return value;
                  }
                });
              }
            }
            return obj;
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap dom/data.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const elementMap = new Map();
          const Data = {
            set(element, key, instance) {
              if (!elementMap.has(element)) {
                elementMap.set(element, new Map());
              }
              const instanceMap = elementMap.get(element);

              // make it clear we only want one instance per element
              // can be removed later when multiple key/instances are fine to be used
              if (!instanceMap.has(key) && instanceMap.size !== 0) {
                // eslint-disable-next-line no-console
                console.error(`Bootstrap doesn't allow more than one instance per element. Bound instance: ${Array.from(instanceMap.keys())[0]}.`);
                return;
              }
              instanceMap.set(key, instance);
            },
            get(element, key) {
              if (elementMap.has(element)) {
                return elementMap.get(element).get(key) || null;
              }
              return null;
            },
            remove(element, key) {
              if (!elementMap.has(element)) {
                return;
              }
              const instanceMap = elementMap.get(element);
              instanceMap.delete(key);

              // free up element references if there are no instances left for an element
              if (instanceMap.size === 0) {
                elementMap.delete(element);
              }
            }
          };

          /**
           * --------------------------------------------------------------------------
           * Bootstrap dom/manipulator.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          function normalizeData(value) {
            if (value === 'true') {
              return true;
            }
            if (value === 'false') {
              return false;
            }
            if (value === Number(value).toString()) {
              return Number(value);
            }
            if (value === '' || value === 'null') {
              return null;
            }
            if (typeof value !== 'string') {
              return value;
            }
            try {
              return JSON.parse(decodeURIComponent(value));
            } catch (_unused) {
              return value;
            }
          }
          function normalizeDataKey(key) {
            return key.replace(/[A-Z]/g, chr => `-${chr.toLowerCase()}`);
          }
          const Manipulator = {
            setDataAttribute(element, key, value) {
              element.setAttribute(`data-bs-${normalizeDataKey(key)}`, value);
            },
            removeDataAttribute(element, key) {
              element.removeAttribute(`data-bs-${normalizeDataKey(key)}`);
            },
            getDataAttributes(element) {
              if (!element) {
                return {};
              }
              const attributes = {};
              const bsKeys = Object.keys(element.dataset).filter(key => key.startsWith('bs') && !key.startsWith('bsConfig'));
              for (const key of bsKeys) {
                let pureKey = key.replace(/^bs/, '');
                pureKey = pureKey.charAt(0).toLowerCase() + pureKey.slice(1, pureKey.length);
                attributes[pureKey] = normalizeData(element.dataset[key]);
              }
              return attributes;
            },
            getDataAttribute(element, key) {
              return normalizeData(element.getAttribute(`data-bs-${normalizeDataKey(key)}`));
            }
          };

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/config.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Class definition
           */

          class Config {
            // Getters
            static get Default() {
              return {};
            }
            static get DefaultType() {
              return {};
            }
            static get NAME() {
              throw new Error('You have to implement the static method "NAME", for each component!');
            }
            _getConfig(config) {
              config = this._mergeConfigObj(config);
              config = this._configAfterMerge(config);
              this._typeCheckConfig(config);
              return config;
            }
            _configAfterMerge(config) {
              return config;
            }
            _mergeConfigObj(config, element) {
              const jsonConfig = isElement(element) ? Manipulator.getDataAttribute(element, 'config') : {}; // try to parse

              return {
                ...this.constructor.Default,
                ...(typeof jsonConfig === 'object' ? jsonConfig : {}),
                ...(isElement(element) ? Manipulator.getDataAttributes(element) : {}),
                ...(typeof config === 'object' ? config : {})
              };
            }
            _typeCheckConfig(config, configTypes = this.constructor.DefaultType) {
              for (const [property, expectedTypes] of Object.entries(configTypes)) {
                const value = config[property];
                const valueType = isElement(value) ? 'element' : toType(value);
                if (!new RegExp(expectedTypes).test(valueType)) {
                  throw new TypeError(`${this.constructor.NAME.toUpperCase()}: Option "${property}" provided type "${valueType}" but expected type "${expectedTypes}".`);
                }
              }
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap base-component.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const VERSION = '5.3.0-alpha2';

          /**
           * Class definition
           */

          class BaseComponent extends Config {
            constructor(element, config) {
              super();
              element = getElement(element);
              if (!element) {
                return;
              }
              this._element = element;
              this._config = this._getConfig(config);
              Data.set(this._element, this.constructor.DATA_KEY, this);
            }

            // Public
            dispose() {
              Data.remove(this._element, this.constructor.DATA_KEY);
              EventHandler.off(this._element, this.constructor.EVENT_KEY);
              for (const propertyName of Object.getOwnPropertyNames(this)) {
                this[propertyName] = null;
              }
            }
            _queueCallback(callback, element, isAnimated = true) {
              executeAfterTransition(callback, element, isAnimated);
            }
            _getConfig(config) {
              config = this._mergeConfigObj(config, this._element);
              config = this._configAfterMerge(config);
              this._typeCheckConfig(config);
              return config;
            }

            // Static
            static getInstance(element) {
              return Data.get(getElement(element), this.DATA_KEY);
            }
            static getOrCreateInstance(element, config = {}) {
              return this.getInstance(element) || new this(element, typeof config === 'object' ? config : null);
            }
            static get VERSION() {
              return VERSION;
            }
            static get DATA_KEY() {
              return `bs.${this.NAME}`;
            }
            static get EVENT_KEY() {
              return `.${this.DATA_KEY}`;
            }
            static eventName(name) {
              return `${name}${this.EVENT_KEY}`;
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap dom/selector-engine.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */
          const getSelector = element => {
            let selector = element.getAttribute('data-bs-target');
            if (!selector || selector === '#') {
              let hrefAttribute = element.getAttribute('href');

              // The only valid content that could double as a selector are IDs or classes,
              // so everything starting with `#` or `.`. If a "real" URL is used as the selector,
              // `document.querySelector` will rightfully complain it is invalid.
              // See https://github.com/twbs/bootstrap/issues/32273
              if (!hrefAttribute || !hrefAttribute.includes('#') && !hrefAttribute.startsWith('.')) {
                return null;
              }

              // Just in case some CMS puts out a full URL with the anchor appended
              if (hrefAttribute.includes('#') && !hrefAttribute.startsWith('#')) {
                hrefAttribute = `#${hrefAttribute.split('#')[1]}`;
              }
              selector = hrefAttribute && hrefAttribute !== '#' ? hrefAttribute.trim() : null;
            }
            return parseSelector(selector);
          };
          const SelectorEngine = {
            find(selector, element = document.documentElement) {
              return [].concat(...Element.prototype.querySelectorAll.call(element, selector));
            },
            findOne(selector, element = document.documentElement) {
              return Element.prototype.querySelector.call(element, selector);
            },
            children(element, selector) {
              return [].concat(...element.children).filter(child => child.matches(selector));
            },
            parents(element, selector) {
              const parents = [];
              let ancestor = element.parentNode.closest(selector);
              while (ancestor) {
                parents.push(ancestor);
                ancestor = ancestor.parentNode.closest(selector);
              }
              return parents;
            },
            prev(element, selector) {
              let previous = element.previousElementSibling;
              while (previous) {
                if (previous.matches(selector)) {
                  return [previous];
                }
                previous = previous.previousElementSibling;
              }
              return [];
            },
            // TODO: this is now unused; remove later along with prev()
            next(element, selector) {
              let next = element.nextElementSibling;
              while (next) {
                if (next.matches(selector)) {
                  return [next];
                }
                next = next.nextElementSibling;
              }
              return [];
            },
            focusableChildren(element) {
              const focusables = ['a', 'button', 'input', 'textarea', 'select', 'details', '[tabindex]', '[contenteditable="true"]'].map(selector => `${selector}:not([tabindex^="-"])`).join(',');
              return this.find(focusables, element).filter(el => !isDisabled(el) && isVisible(el));
            },
            getSelectorFromElement(element) {
              const selector = getSelector(element);
              if (selector) {
                return SelectorEngine.findOne(selector) ? selector : null;
              }
              return null;
            },
            getElementFromSelector(element) {
              const selector = getSelector(element);
              return selector ? SelectorEngine.findOne(selector) : null;
            },
            getMultipleElementsFromSelector(element) {
              const selector = getSelector(element);
              return selector ? SelectorEngine.find(selector) : [];
            }
          };

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/component-functions.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */
          const enableDismissTrigger = (component, method = 'hide') => {
            const clickEvent = `click.dismiss${component.EVENT_KEY}`;
            const name = component.NAME;
            EventHandler.on(document, clickEvent, `[data-bs-dismiss="${name}"]`, function (event) {
              if (['A', 'AREA'].includes(this.tagName)) {
                event.preventDefault();
              }
              if (isDisabled(this)) {
                return;
              }
              const target = SelectorEngine.getElementFromSelector(this) || this.closest(`.${name}`);
              const instance = component.getOrCreateInstance(target);

              // Method argument is left, for Alert and only, as it doesn't implement the 'hide' method
              instance[method]();
            });
          };

          /**
           * --------------------------------------------------------------------------
           * Bootstrap alert.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$f = 'alert';
          const DATA_KEY$a = 'bs.alert';
          const EVENT_KEY$b = `.${DATA_KEY$a}`;
          const EVENT_CLOSE = `close${EVENT_KEY$b}`;
          const EVENT_CLOSED = `closed${EVENT_KEY$b}`;
          const CLASS_NAME_FADE$5 = 'fade';
          const CLASS_NAME_SHOW$8 = 'show';

          /**
           * Class definition
           */

          class Alert extends BaseComponent {
            // Getters
            static get NAME() {
              return NAME$f;
            }

            // Public
            close() {
              const closeEvent = EventHandler.trigger(this._element, EVENT_CLOSE);
              if (closeEvent.defaultPrevented) {
                return;
              }
              this._element.classList.remove(CLASS_NAME_SHOW$8);
              const isAnimated = this._element.classList.contains(CLASS_NAME_FADE$5);
              this._queueCallback(() => this._destroyElement(), this._element, isAnimated);
            }

            // Private
            _destroyElement() {
              this._element.remove();
              EventHandler.trigger(this._element, EVENT_CLOSED);
              this.dispose();
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Alert.getOrCreateInstance(this);
                if (typeof config !== 'string') {
                  return;
                }
                if (data[config] === undefined || config.startsWith('_') || config === 'constructor') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config](this);
              });
            }
          }

          /**
           * Data API implementation
           */

          enableDismissTrigger(Alert, 'close');

          /**
           * jQuery
           */

          defineJQueryPlugin(Alert);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap button.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$e = 'button';
          const DATA_KEY$9 = 'bs.button';
          const EVENT_KEY$a = `.${DATA_KEY$9}`;
          const DATA_API_KEY$6 = '.data-api';
          const CLASS_NAME_ACTIVE$3 = 'active';
          const SELECTOR_DATA_TOGGLE$5 = '[data-bs-toggle="button"]';
          const EVENT_CLICK_DATA_API$6 = `click${EVENT_KEY$a}${DATA_API_KEY$6}`;

          /**
           * Class definition
           */

          class Button extends BaseComponent {
            // Getters
            static get NAME() {
              return NAME$e;
            }

            // Public
            toggle() {
              // Toggle class and sync the `aria-pressed` attribute with the return value of the `.toggle()` method
              this._element.setAttribute('aria-pressed', this._element.classList.toggle(CLASS_NAME_ACTIVE$3));
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Button.getOrCreateInstance(this);
                if (config === 'toggle') {
                  data[config]();
                }
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_CLICK_DATA_API$6, SELECTOR_DATA_TOGGLE$5, event => {
            event.preventDefault();
            const button = event.target.closest(SELECTOR_DATA_TOGGLE$5);
            const data = Button.getOrCreateInstance(button);
            data.toggle();
          });

          /**
           * jQuery
           */

          defineJQueryPlugin(Button);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/swipe.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$d = 'swipe';
          const EVENT_KEY$9 = '.bs.swipe';
          const EVENT_TOUCHSTART = `touchstart${EVENT_KEY$9}`;
          const EVENT_TOUCHMOVE = `touchmove${EVENT_KEY$9}`;
          const EVENT_TOUCHEND = `touchend${EVENT_KEY$9}`;
          const EVENT_POINTERDOWN = `pointerdown${EVENT_KEY$9}`;
          const EVENT_POINTERUP = `pointerup${EVENT_KEY$9}`;
          const POINTER_TYPE_TOUCH = 'touch';
          const POINTER_TYPE_PEN = 'pen';
          const CLASS_NAME_POINTER_EVENT = 'pointer-event';
          const SWIPE_THRESHOLD = 40;
          const Default$c = {
            endCallback: null,
            leftCallback: null,
            rightCallback: null
          };
          const DefaultType$c = {
            endCallback: '(function|null)',
            leftCallback: '(function|null)',
            rightCallback: '(function|null)'
          };

          /**
           * Class definition
           */

          class Swipe extends Config {
            constructor(element, config) {
              super();
              this._element = element;
              if (!element || !Swipe.isSupported()) {
                return;
              }
              this._config = this._getConfig(config);
              this._deltaX = 0;
              this._supportPointerEvents = Boolean(window.PointerEvent);
              this._initEvents();
            }

            // Getters
            static get Default() {
              return Default$c;
            }
            static get DefaultType() {
              return DefaultType$c;
            }
            static get NAME() {
              return NAME$d;
            }

            // Public
            dispose() {
              EventHandler.off(this._element, EVENT_KEY$9);
            }

            // Private
            _start(event) {
              if (!this._supportPointerEvents) {
                this._deltaX = event.touches[0].clientX;
                return;
              }
              if (this._eventIsPointerPenTouch(event)) {
                this._deltaX = event.clientX;
              }
            }
            _end(event) {
              if (this._eventIsPointerPenTouch(event)) {
                this._deltaX = event.clientX - this._deltaX;
              }
              this._handleSwipe();
              execute(this._config.endCallback);
            }
            _move(event) {
              this._deltaX = event.touches && event.touches.length > 1 ? 0 : event.touches[0].clientX - this._deltaX;
            }
            _handleSwipe() {
              const absDeltaX = Math.abs(this._deltaX);
              if (absDeltaX <= SWIPE_THRESHOLD) {
                return;
              }
              const direction = absDeltaX / this._deltaX;
              this._deltaX = 0;
              if (!direction) {
                return;
              }
              execute(direction > 0 ? this._config.rightCallback : this._config.leftCallback);
            }
            _initEvents() {
              if (this._supportPointerEvents) {
                EventHandler.on(this._element, EVENT_POINTERDOWN, event => this._start(event));
                EventHandler.on(this._element, EVENT_POINTERUP, event => this._end(event));
                this._element.classList.add(CLASS_NAME_POINTER_EVENT);
              } else {
                EventHandler.on(this._element, EVENT_TOUCHSTART, event => this._start(event));
                EventHandler.on(this._element, EVENT_TOUCHMOVE, event => this._move(event));
                EventHandler.on(this._element, EVENT_TOUCHEND, event => this._end(event));
              }
            }
            _eventIsPointerPenTouch(event) {
              return this._supportPointerEvents && (event.pointerType === POINTER_TYPE_PEN || event.pointerType === POINTER_TYPE_TOUCH);
            }

            // Static
            static isSupported() {
              return 'ontouchstart' in document.documentElement || navigator.maxTouchPoints > 0;
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap carousel.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$c = 'carousel';
          const DATA_KEY$8 = 'bs.carousel';
          const EVENT_KEY$8 = `.${DATA_KEY$8}`;
          const DATA_API_KEY$5 = '.data-api';
          const ARROW_LEFT_KEY$1 = 'ArrowLeft';
          const ARROW_RIGHT_KEY$1 = 'ArrowRight';
          const TOUCHEVENT_COMPAT_WAIT = 500; // Time for mouse compat events to fire after touch

          const ORDER_NEXT = 'next';
          const ORDER_PREV = 'prev';
          const DIRECTION_LEFT = 'left';
          const DIRECTION_RIGHT = 'right';
          const EVENT_SLIDE = `slide${EVENT_KEY$8}`;
          const EVENT_SLID = `slid${EVENT_KEY$8}`;
          const EVENT_KEYDOWN$1 = `keydown${EVENT_KEY$8}`;
          const EVENT_MOUSEENTER$1 = `mouseenter${EVENT_KEY$8}`;
          const EVENT_MOUSELEAVE$1 = `mouseleave${EVENT_KEY$8}`;
          const EVENT_DRAG_START = `dragstart${EVENT_KEY$8}`;
          const EVENT_LOAD_DATA_API$3 = `load${EVENT_KEY$8}${DATA_API_KEY$5}`;
          const EVENT_CLICK_DATA_API$5 = `click${EVENT_KEY$8}${DATA_API_KEY$5}`;
          const CLASS_NAME_CAROUSEL = 'carousel';
          const CLASS_NAME_ACTIVE$2 = 'active';
          const CLASS_NAME_SLIDE = 'slide';
          const CLASS_NAME_END = 'carousel-item-end';
          const CLASS_NAME_START = 'carousel-item-start';
          const CLASS_NAME_NEXT = 'carousel-item-next';
          const CLASS_NAME_PREV = 'carousel-item-prev';
          const SELECTOR_ACTIVE = '.active';
          const SELECTOR_ITEM = '.carousel-item';
          const SELECTOR_ACTIVE_ITEM = SELECTOR_ACTIVE + SELECTOR_ITEM;
          const SELECTOR_ITEM_IMG = '.carousel-item img';
          const SELECTOR_INDICATORS = '.carousel-indicators';
          const SELECTOR_DATA_SLIDE = '[data-bs-slide], [data-bs-slide-to]';
          const SELECTOR_DATA_RIDE = '[data-bs-ride="carousel"]';
          const KEY_TO_DIRECTION = {
            [ARROW_LEFT_KEY$1]: DIRECTION_RIGHT,
            [ARROW_RIGHT_KEY$1]: DIRECTION_LEFT
          };
          const Default$b = {
            interval: 5000,
            keyboard: true,
            pause: 'hover',
            ride: false,
            touch: true,
            wrap: true
          };
          const DefaultType$b = {
            interval: '(number|boolean)',
            // TODO:v6 remove boolean support
            keyboard: 'boolean',
            pause: '(string|boolean)',
            ride: '(boolean|string)',
            touch: 'boolean',
            wrap: 'boolean'
          };

          /**
           * Class definition
           */

          class Carousel extends BaseComponent {
            constructor(element, config) {
              super(element, config);
              this._interval = null;
              this._activeElement = null;
              this._isSliding = false;
              this.touchTimeout = null;
              this._swipeHelper = null;
              this._indicatorsElement = SelectorEngine.findOne(SELECTOR_INDICATORS, this._element);
              this._addEventListeners();
              if (this._config.ride === CLASS_NAME_CAROUSEL) {
                this.cycle();
              }
            }

            // Getters
            static get Default() {
              return Default$b;
            }
            static get DefaultType() {
              return DefaultType$b;
            }
            static get NAME() {
              return NAME$c;
            }

            // Public
            next() {
              this._slide(ORDER_NEXT);
            }
            nextWhenVisible() {
              // FIXME TODO use `document.visibilityState`
              // Don't call next when the page isn't visible
              // or the carousel or its parent isn't visible
              if (!document.hidden && isVisible(this._element)) {
                this.next();
              }
            }
            prev() {
              this._slide(ORDER_PREV);
            }
            pause() {
              if (this._isSliding) {
                triggerTransitionEnd(this._element);
              }
              this._clearInterval();
            }
            cycle() {
              this._clearInterval();
              this._updateInterval();
              this._interval = setInterval(() => this.nextWhenVisible(), this._config.interval);
            }
            _maybeEnableCycle() {
              if (!this._config.ride) {
                return;
              }
              if (this._isSliding) {
                EventHandler.one(this._element, EVENT_SLID, () => this.cycle());
                return;
              }
              this.cycle();
            }
            to(index) {
              const items = this._getItems();
              if (index > items.length - 1 || index < 0) {
                return;
              }
              if (this._isSliding) {
                EventHandler.one(this._element, EVENT_SLID, () => this.to(index));
                return;
              }
              const activeIndex = this._getItemIndex(this._getActive());
              if (activeIndex === index) {
                return;
              }
              const order = index > activeIndex ? ORDER_NEXT : ORDER_PREV;
              this._slide(order, items[index]);
            }
            dispose() {
              if (this._swipeHelper) {
                this._swipeHelper.dispose();
              }
              super.dispose();
            }

            // Private
            _configAfterMerge(config) {
              config.defaultInterval = config.interval;
              return config;
            }
            _addEventListeners() {
              if (this._config.keyboard) {
                EventHandler.on(this._element, EVENT_KEYDOWN$1, event => this._keydown(event));
              }
              if (this._config.pause === 'hover') {
                EventHandler.on(this._element, EVENT_MOUSEENTER$1, () => this.pause());
                EventHandler.on(this._element, EVENT_MOUSELEAVE$1, () => this._maybeEnableCycle());
              }
              if (this._config.touch && Swipe.isSupported()) {
                this._addTouchEventListeners();
              }
            }
            _addTouchEventListeners() {
              for (const img of SelectorEngine.find(SELECTOR_ITEM_IMG, this._element)) {
                EventHandler.on(img, EVENT_DRAG_START, event => event.preventDefault());
              }
              const endCallBack = () => {
                if (this._config.pause !== 'hover') {
                  return;
                }

                // If it's a touch-enabled device, mouseenter/leave are fired as
                // part of the mouse compatibility events on first tap - the carousel
                // would stop cycling until user tapped out of it;
                // here, we listen for touchend, explicitly pause the carousel
                // (as if it's the second time we tap on it, mouseenter compat event
                // is NOT fired) and after a timeout (to allow for mouse compatibility
                // events to fire) we explicitly restart cycling

                this.pause();
                if (this.touchTimeout) {
                  clearTimeout(this.touchTimeout);
                }
                this.touchTimeout = setTimeout(() => this._maybeEnableCycle(), TOUCHEVENT_COMPAT_WAIT + this._config.interval);
              };
              const swipeConfig = {
                leftCallback: () => this._slide(this._directionToOrder(DIRECTION_LEFT)),
                rightCallback: () => this._slide(this._directionToOrder(DIRECTION_RIGHT)),
                endCallback: endCallBack
              };
              this._swipeHelper = new Swipe(this._element, swipeConfig);
            }
            _keydown(event) {
              if (/input|textarea/i.test(event.target.tagName)) {
                return;
              }
              const direction = KEY_TO_DIRECTION[event.key];
              if (direction) {
                event.preventDefault();
                this._slide(this._directionToOrder(direction));
              }
            }
            _getItemIndex(element) {
              return this._getItems().indexOf(element);
            }
            _setActiveIndicatorElement(index) {
              if (!this._indicatorsElement) {
                return;
              }
              const activeIndicator = SelectorEngine.findOne(SELECTOR_ACTIVE, this._indicatorsElement);
              activeIndicator.classList.remove(CLASS_NAME_ACTIVE$2);
              activeIndicator.removeAttribute('aria-current');
              const newActiveIndicator = SelectorEngine.findOne(`[data-bs-slide-to="${index}"]`, this._indicatorsElement);
              if (newActiveIndicator) {
                newActiveIndicator.classList.add(CLASS_NAME_ACTIVE$2);
                newActiveIndicator.setAttribute('aria-current', 'true');
              }
            }
            _updateInterval() {
              const element = this._activeElement || this._getActive();
              if (!element) {
                return;
              }
              const elementInterval = Number.parseInt(element.getAttribute('data-bs-interval'), 10);
              this._config.interval = elementInterval || this._config.defaultInterval;
            }
            _slide(order, element = null) {
              if (this._isSliding) {
                return;
              }
              const activeElement = this._getActive();
              const isNext = order === ORDER_NEXT;
              const nextElement = element || getNextActiveElement(this._getItems(), activeElement, isNext, this._config.wrap);
              if (nextElement === activeElement) {
                return;
              }
              const nextElementIndex = this._getItemIndex(nextElement);
              const triggerEvent = eventName => {
                return EventHandler.trigger(this._element, eventName, {
                  relatedTarget: nextElement,
                  direction: this._orderToDirection(order),
                  from: this._getItemIndex(activeElement),
                  to: nextElementIndex
                });
              };
              const slideEvent = triggerEvent(EVENT_SLIDE);
              if (slideEvent.defaultPrevented) {
                return;
              }
              if (!activeElement || !nextElement) {
                // Some weirdness is happening, so we bail
                // todo: change tests that use empty divs to avoid this check
                return;
              }
              const isCycling = Boolean(this._interval);
              this.pause();
              this._isSliding = true;
              this._setActiveIndicatorElement(nextElementIndex);
              this._activeElement = nextElement;
              const directionalClassName = isNext ? CLASS_NAME_START : CLASS_NAME_END;
              const orderClassName = isNext ? CLASS_NAME_NEXT : CLASS_NAME_PREV;
              nextElement.classList.add(orderClassName);
              reflow(nextElement);
              activeElement.classList.add(directionalClassName);
              nextElement.classList.add(directionalClassName);
              const completeCallBack = () => {
                nextElement.classList.remove(directionalClassName, orderClassName);
                nextElement.classList.add(CLASS_NAME_ACTIVE$2);
                activeElement.classList.remove(CLASS_NAME_ACTIVE$2, orderClassName, directionalClassName);
                this._isSliding = false;
                triggerEvent(EVENT_SLID);
              };
              this._queueCallback(completeCallBack, activeElement, this._isAnimated());
              if (isCycling) {
                this.cycle();
              }
            }
            _isAnimated() {
              return this._element.classList.contains(CLASS_NAME_SLIDE);
            }
            _getActive() {
              return SelectorEngine.findOne(SELECTOR_ACTIVE_ITEM, this._element);
            }
            _getItems() {
              return SelectorEngine.find(SELECTOR_ITEM, this._element);
            }
            _clearInterval() {
              if (this._interval) {
                clearInterval(this._interval);
                this._interval = null;
              }
            }
            _directionToOrder(direction) {
              if (isRTL()) {
                return direction === DIRECTION_LEFT ? ORDER_PREV : ORDER_NEXT;
              }
              return direction === DIRECTION_LEFT ? ORDER_NEXT : ORDER_PREV;
            }
            _orderToDirection(order) {
              if (isRTL()) {
                return order === ORDER_PREV ? DIRECTION_LEFT : DIRECTION_RIGHT;
              }
              return order === ORDER_PREV ? DIRECTION_RIGHT : DIRECTION_LEFT;
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Carousel.getOrCreateInstance(this, config);
                if (typeof config === 'number') {
                  data.to(config);
                  return;
                }
                if (typeof config === 'string') {
                  if (data[config] === undefined || config.startsWith('_') || config === 'constructor') {
                    throw new TypeError(`No method named "${config}"`);
                  }
                  data[config]();
                }
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_CLICK_DATA_API$5, SELECTOR_DATA_SLIDE, function (event) {
            const target = SelectorEngine.getElementFromSelector(this);
            if (!target || !target.classList.contains(CLASS_NAME_CAROUSEL)) {
              return;
            }
            event.preventDefault();
            const carousel = Carousel.getOrCreateInstance(target);
            const slideIndex = this.getAttribute('data-bs-slide-to');
            if (slideIndex) {
              carousel.to(slideIndex);
              carousel._maybeEnableCycle();
              return;
            }
            if (Manipulator.getDataAttribute(this, 'slide') === 'next') {
              carousel.next();
              carousel._maybeEnableCycle();
              return;
            }
            carousel.prev();
            carousel._maybeEnableCycle();
          });
          EventHandler.on(window, EVENT_LOAD_DATA_API$3, () => {
            const carousels = SelectorEngine.find(SELECTOR_DATA_RIDE);
            for (const carousel of carousels) {
              Carousel.getOrCreateInstance(carousel);
            }
          });

          /**
           * jQuery
           */

          defineJQueryPlugin(Carousel);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap collapse.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$b = 'collapse';
          const DATA_KEY$7 = 'bs.collapse';
          const EVENT_KEY$7 = `.${DATA_KEY$7}`;
          const DATA_API_KEY$4 = '.data-api';
          const EVENT_SHOW$6 = `show${EVENT_KEY$7}`;
          const EVENT_SHOWN$6 = `shown${EVENT_KEY$7}`;
          const EVENT_HIDE$6 = `hide${EVENT_KEY$7}`;
          const EVENT_HIDDEN$6 = `hidden${EVENT_KEY$7}`;
          const EVENT_CLICK_DATA_API$4 = `click${EVENT_KEY$7}${DATA_API_KEY$4}`;
          const CLASS_NAME_SHOW$7 = 'show';
          const CLASS_NAME_COLLAPSE = 'collapse';
          const CLASS_NAME_COLLAPSING = 'collapsing';
          const CLASS_NAME_COLLAPSED = 'collapsed';
          const CLASS_NAME_DEEPER_CHILDREN = `:scope .${CLASS_NAME_COLLAPSE} .${CLASS_NAME_COLLAPSE}`;
          const CLASS_NAME_HORIZONTAL = 'collapse-horizontal';
          const WIDTH = 'width';
          const HEIGHT = 'height';
          const SELECTOR_ACTIVES = '.collapse.show, .collapse.collapsing';
          const SELECTOR_DATA_TOGGLE$4 = '[data-bs-toggle="collapse"]';
          const Default$a = {
            parent: null,
            toggle: true
          };
          const DefaultType$a = {
            parent: '(null|element)',
            toggle: 'boolean'
          };

          /**
           * Class definition
           */

          class Collapse extends BaseComponent {
            constructor(element, config) {
              super(element, config);
              this._isTransitioning = false;
              this._triggerArray = [];
              const toggleList = SelectorEngine.find(SELECTOR_DATA_TOGGLE$4);
              for (const elem of toggleList) {
                const selector = SelectorEngine.getSelectorFromElement(elem);
                const filterElement = SelectorEngine.find(selector).filter(foundElement => foundElement === this._element);
                if (selector !== null && filterElement.length) {
                  this._triggerArray.push(elem);
                }
              }
              this._initializeChildren();
              if (!this._config.parent) {
                this._addAriaAndCollapsedClass(this._triggerArray, this._isShown());
              }
              if (this._config.toggle) {
                this.toggle();
              }
            }

            // Getters
            static get Default() {
              return Default$a;
            }
            static get DefaultType() {
              return DefaultType$a;
            }
            static get NAME() {
              return NAME$b;
            }

            // Public
            toggle() {
              if (this._isShown()) {
                this.hide();
              } else {
                this.show();
              }
            }
            show() {
              if (this._isTransitioning || this._isShown()) {
                return;
              }
              let activeChildren = [];

              // find active children
              if (this._config.parent) {
                activeChildren = this._getFirstLevelChildren(SELECTOR_ACTIVES).filter(element => element !== this._element).map(element => Collapse.getOrCreateInstance(element, {
                  toggle: false
                }));
              }
              if (activeChildren.length && activeChildren[0]._isTransitioning) {
                return;
              }
              const startEvent = EventHandler.trigger(this._element, EVENT_SHOW$6);
              if (startEvent.defaultPrevented) {
                return;
              }
              for (const activeInstance of activeChildren) {
                activeInstance.hide();
              }
              const dimension = this._getDimension();
              this._element.classList.remove(CLASS_NAME_COLLAPSE);
              this._element.classList.add(CLASS_NAME_COLLAPSING);
              this._element.style[dimension] = 0;
              this._addAriaAndCollapsedClass(this._triggerArray, true);
              this._isTransitioning = true;
              const complete = () => {
                this._isTransitioning = false;
                this._element.classList.remove(CLASS_NAME_COLLAPSING);
                this._element.classList.add(CLASS_NAME_COLLAPSE, CLASS_NAME_SHOW$7);
                this._element.style[dimension] = '';
                EventHandler.trigger(this._element, EVENT_SHOWN$6);
              };
              const capitalizedDimension = dimension[0].toUpperCase() + dimension.slice(1);
              const scrollSize = `scroll${capitalizedDimension}`;
              this._queueCallback(complete, this._element, true);
              this._element.style[dimension] = `${this._element[scrollSize]}px`;
            }
            hide() {
              if (this._isTransitioning || !this._isShown()) {
                return;
              }
              const startEvent = EventHandler.trigger(this._element, EVENT_HIDE$6);
              if (startEvent.defaultPrevented) {
                return;
              }
              const dimension = this._getDimension();
              this._element.style[dimension] = `${this._element.getBoundingClientRect()[dimension]}px`;
              reflow(this._element);
              this._element.classList.add(CLASS_NAME_COLLAPSING);
              this._element.classList.remove(CLASS_NAME_COLLAPSE, CLASS_NAME_SHOW$7);
              for (const trigger of this._triggerArray) {
                const element = SelectorEngine.getElementFromSelector(trigger);
                if (element && !this._isShown(element)) {
                  this._addAriaAndCollapsedClass([trigger], false);
                }
              }
              this._isTransitioning = true;
              const complete = () => {
                this._isTransitioning = false;
                this._element.classList.remove(CLASS_NAME_COLLAPSING);
                this._element.classList.add(CLASS_NAME_COLLAPSE);
                EventHandler.trigger(this._element, EVENT_HIDDEN$6);
              };
              this._element.style[dimension] = '';
              this._queueCallback(complete, this._element, true);
            }
            _isShown(element = this._element) {
              return element.classList.contains(CLASS_NAME_SHOW$7);
            }

            // Private
            _configAfterMerge(config) {
              config.toggle = Boolean(config.toggle); // Coerce string values
              config.parent = getElement(config.parent);
              return config;
            }
            _getDimension() {
              return this._element.classList.contains(CLASS_NAME_HORIZONTAL) ? WIDTH : HEIGHT;
            }
            _initializeChildren() {
              if (!this._config.parent) {
                return;
              }
              const children = this._getFirstLevelChildren(SELECTOR_DATA_TOGGLE$4);
              for (const element of children) {
                const selected = SelectorEngine.getElementFromSelector(element);
                if (selected) {
                  this._addAriaAndCollapsedClass([element], this._isShown(selected));
                }
              }
            }
            _getFirstLevelChildren(selector) {
              const children = SelectorEngine.find(CLASS_NAME_DEEPER_CHILDREN, this._config.parent);
              // remove children if greater depth
              return SelectorEngine.find(selector, this._config.parent).filter(element => !children.includes(element));
            }
            _addAriaAndCollapsedClass(triggerArray, isOpen) {
              if (!triggerArray.length) {
                return;
              }
              for (const element of triggerArray) {
                element.classList.toggle(CLASS_NAME_COLLAPSED, !isOpen);
                element.setAttribute('aria-expanded', isOpen);
              }
            }

            // Static
            static jQueryInterface(config) {
              const _config = {};
              if (typeof config === 'string' && /show|hide/.test(config)) {
                _config.toggle = false;
              }
              return this.each(function () {
                const data = Collapse.getOrCreateInstance(this, _config);
                if (typeof config === 'string') {
                  if (typeof data[config] === 'undefined') {
                    throw new TypeError(`No method named "${config}"`);
                  }
                  data[config]();
                }
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_CLICK_DATA_API$4, SELECTOR_DATA_TOGGLE$4, function (event) {
            // preventDefault only for <a> elements (which change the URL) not inside the collapsible element
            if (event.target.tagName === 'A' || event.delegateTarget && event.delegateTarget.tagName === 'A') {
              event.preventDefault();
            }
            for (const element of SelectorEngine.getMultipleElementsFromSelector(this)) {
              Collapse.getOrCreateInstance(element, {
                toggle: false
              }).toggle();
            }
          });

          /**
           * jQuery
           */

          defineJQueryPlugin(Collapse);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap dropdown.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$a = 'dropdown';
          const DATA_KEY$6 = 'bs.dropdown';
          const EVENT_KEY$6 = `.${DATA_KEY$6}`;
          const DATA_API_KEY$3 = '.data-api';
          const ESCAPE_KEY$2 = 'Escape';
          const TAB_KEY$1 = 'Tab';
          const ARROW_UP_KEY$1 = 'ArrowUp';
          const ARROW_DOWN_KEY$1 = 'ArrowDown';
          const RIGHT_MOUSE_BUTTON = 2; // MouseEvent.button value for the secondary button, usually the right button

          const EVENT_HIDE$5 = `hide${EVENT_KEY$6}`;
          const EVENT_HIDDEN$5 = `hidden${EVENT_KEY$6}`;
          const EVENT_SHOW$5 = `show${EVENT_KEY$6}`;
          const EVENT_SHOWN$5 = `shown${EVENT_KEY$6}`;
          const EVENT_CLICK_DATA_API$3 = `click${EVENT_KEY$6}${DATA_API_KEY$3}`;
          const EVENT_KEYDOWN_DATA_API = `keydown${EVENT_KEY$6}${DATA_API_KEY$3}`;
          const EVENT_KEYUP_DATA_API = `keyup${EVENT_KEY$6}${DATA_API_KEY$3}`;
          const CLASS_NAME_SHOW$6 = 'show';
          const CLASS_NAME_DROPUP = 'dropup';
          const CLASS_NAME_DROPEND = 'dropend';
          const CLASS_NAME_DROPSTART = 'dropstart';
          const CLASS_NAME_DROPUP_CENTER = 'dropup-center';
          const CLASS_NAME_DROPDOWN_CENTER = 'dropdown-center';
          const SELECTOR_DATA_TOGGLE$3 = '[data-bs-toggle="dropdown"]:not(.disabled):not(:disabled)';
          const SELECTOR_DATA_TOGGLE_SHOWN = `${SELECTOR_DATA_TOGGLE$3}.${CLASS_NAME_SHOW$6}`;
          const SELECTOR_MENU = '.dropdown-menu';
          const SELECTOR_NAVBAR = '.navbar';
          const SELECTOR_NAVBAR_NAV = '.navbar-nav';
          const SELECTOR_VISIBLE_ITEMS = '.dropdown-menu .dropdown-item:not(.disabled):not(:disabled)';
          const PLACEMENT_TOP = isRTL() ? 'top-end' : 'top-start';
          const PLACEMENT_TOPEND = isRTL() ? 'top-start' : 'top-end';
          const PLACEMENT_BOTTOM = isRTL() ? 'bottom-end' : 'bottom-start';
          const PLACEMENT_BOTTOMEND = isRTL() ? 'bottom-start' : 'bottom-end';
          const PLACEMENT_RIGHT = isRTL() ? 'left-start' : 'right-start';
          const PLACEMENT_LEFT = isRTL() ? 'right-start' : 'left-start';
          const PLACEMENT_TOPCENTER = 'top';
          const PLACEMENT_BOTTOMCENTER = 'bottom';
          const Default$9 = {
            autoClose: true,
            boundary: 'clippingParents',
            display: 'dynamic',
            offset: [0, 2],
            popperConfig: null,
            reference: 'toggle'
          };
          const DefaultType$9 = {
            autoClose: '(boolean|string)',
            boundary: '(string|element)',
            display: 'string',
            offset: '(array|string|function)',
            popperConfig: '(null|object|function)',
            reference: '(string|element|object)'
          };

          /**
           * Class definition
           */

          class Dropdown extends BaseComponent {
            constructor(element, config) {
              super(element, config);
              this._popper = null;
              this._parent = this._element.parentNode; // dropdown wrapper
              // todo: v6 revert #37011 & change markup https://getbootstrap.com/docs/5.3/forms/input-group/
              this._menu = SelectorEngine.next(this._element, SELECTOR_MENU)[0] || SelectorEngine.prev(this._element, SELECTOR_MENU)[0] || SelectorEngine.findOne(SELECTOR_MENU, this._parent);
              this._inNavbar = this._detectNavbar();
            }

            // Getters
            static get Default() {
              return Default$9;
            }
            static get DefaultType() {
              return DefaultType$9;
            }
            static get NAME() {
              return NAME$a;
            }

            // Public
            toggle() {
              return this._isShown() ? this.hide() : this.show();
            }
            show() {
              if (isDisabled(this._element) || this._isShown()) {
                return;
              }
              const relatedTarget = {
                relatedTarget: this._element
              };
              const showEvent = EventHandler.trigger(this._element, EVENT_SHOW$5, relatedTarget);
              if (showEvent.defaultPrevented) {
                return;
              }
              this._createPopper();

              // If this is a touch-enabled device we add extra
              // empty mouseover listeners to the body's immediate children;
              // only needed because of broken event delegation on iOS
              // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html
              if ('ontouchstart' in document.documentElement && !this._parent.closest(SELECTOR_NAVBAR_NAV)) {
                for (const element of [].concat(...document.body.children)) {
                  EventHandler.on(element, 'mouseover', noop);
                }
              }
              this._element.focus();
              this._element.setAttribute('aria-expanded', true);
              this._menu.classList.add(CLASS_NAME_SHOW$6);
              this._element.classList.add(CLASS_NAME_SHOW$6);
              EventHandler.trigger(this._element, EVENT_SHOWN$5, relatedTarget);
            }
            hide() {
              if (isDisabled(this._element) || !this._isShown()) {
                return;
              }
              const relatedTarget = {
                relatedTarget: this._element
              };
              this._completeHide(relatedTarget);
            }
            dispose() {
              if (this._popper) {
                this._popper.destroy();
              }
              super.dispose();
            }
            update() {
              this._inNavbar = this._detectNavbar();
              if (this._popper) {
                this._popper.update();
              }
            }

            // Private
            _completeHide(relatedTarget) {
              const hideEvent = EventHandler.trigger(this._element, EVENT_HIDE$5, relatedTarget);
              if (hideEvent.defaultPrevented) {
                return;
              }

              // If this is a touch-enabled device we remove the extra
              // empty mouseover listeners we added for iOS support
              if ('ontouchstart' in document.documentElement) {
                for (const element of [].concat(...document.body.children)) {
                  EventHandler.off(element, 'mouseover', noop);
                }
              }
              if (this._popper) {
                this._popper.destroy();
              }
              this._menu.classList.remove(CLASS_NAME_SHOW$6);
              this._element.classList.remove(CLASS_NAME_SHOW$6);
              this._element.setAttribute('aria-expanded', 'false');
              Manipulator.removeDataAttribute(this._menu, 'popper');
              EventHandler.trigger(this._element, EVENT_HIDDEN$5, relatedTarget);
            }
            _getConfig(config) {
              config = super._getConfig(config);
              if (typeof config.reference === 'object' && !isElement(config.reference) && typeof config.reference.getBoundingClientRect !== 'function') {
                // Popper virtual elements require a getBoundingClientRect method
                throw new TypeError(`${NAME$a.toUpperCase()}: Option "reference" provided type "object" without a required "getBoundingClientRect" method.`);
              }
              return config;
            }
            _createPopper() {
              if (typeof Popper__namespace === 'undefined') {
                throw new TypeError('Bootstrap\'s dropdowns require Popper (https://popper.js.org)');
              }
              let referenceElement = this._element;
              if (this._config.reference === 'parent') {
                referenceElement = this._parent;
              } else if (isElement(this._config.reference)) {
                referenceElement = getElement(this._config.reference);
              } else if (typeof this._config.reference === 'object') {
                referenceElement = this._config.reference;
              }
              const popperConfig = this._getPopperConfig();
              this._popper = Popper__namespace.createPopper(referenceElement, this._menu, popperConfig);
            }
            _isShown() {
              return this._menu.classList.contains(CLASS_NAME_SHOW$6);
            }
            _getPlacement() {
              const parentDropdown = this._parent;
              if (parentDropdown.classList.contains(CLASS_NAME_DROPEND)) {
                return PLACEMENT_RIGHT;
              }
              if (parentDropdown.classList.contains(CLASS_NAME_DROPSTART)) {
                return PLACEMENT_LEFT;
              }
              if (parentDropdown.classList.contains(CLASS_NAME_DROPUP_CENTER)) {
                return PLACEMENT_TOPCENTER;
              }
              if (parentDropdown.classList.contains(CLASS_NAME_DROPDOWN_CENTER)) {
                return PLACEMENT_BOTTOMCENTER;
              }

              // We need to trim the value because custom properties can also include spaces
              const isEnd = getComputedStyle(this._menu).getPropertyValue('--bs-position').trim() === 'end';
              if (parentDropdown.classList.contains(CLASS_NAME_DROPUP)) {
                return isEnd ? PLACEMENT_TOPEND : PLACEMENT_TOP;
              }
              return isEnd ? PLACEMENT_BOTTOMEND : PLACEMENT_BOTTOM;
            }
            _detectNavbar() {
              return this._element.closest(SELECTOR_NAVBAR) !== null;
            }
            _getOffset() {
              const {
                offset
              } = this._config;
              if (typeof offset === 'string') {
                return offset.split(',').map(value => Number.parseInt(value, 10));
              }
              if (typeof offset === 'function') {
                return popperData => offset(popperData, this._element);
              }
              return offset;
            }
            _getPopperConfig() {
              const defaultBsPopperConfig = {
                placement: this._getPlacement(),
                modifiers: [{
                  name: 'preventOverflow',
                  options: {
                    boundary: this._config.boundary
                  }
                }, {
                  name: 'offset',
                  options: {
                    offset: this._getOffset()
                  }
                }]
              };

              // Disable Popper if we have a static display or Dropdown is in Navbar
              if (this._inNavbar || this._config.display === 'static') {
                Manipulator.setDataAttribute(this._menu, 'popper', 'static'); // todo:v6 remove
                defaultBsPopperConfig.modifiers = [{
                  name: 'applyStyles',
                  enabled: false
                }];
              }
              return {
                ...defaultBsPopperConfig,
                ...execute(this._config.popperConfig, [defaultBsPopperConfig])
              };
            }
            _selectMenuItem({
              key,
              target
            }) {
              const items = SelectorEngine.find(SELECTOR_VISIBLE_ITEMS, this._menu).filter(element => isVisible(element));
              if (!items.length) {
                return;
              }

              // if target isn't included in items (e.g. when expanding the dropdown)
              // allow cycling to get the last item in case key equals ARROW_UP_KEY
              getNextActiveElement(items, target, key === ARROW_DOWN_KEY$1, !items.includes(target)).focus();
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Dropdown.getOrCreateInstance(this, config);
                if (typeof config !== 'string') {
                  return;
                }
                if (typeof data[config] === 'undefined') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config]();
              });
            }
            static clearMenus(event) {
              if (event.button === RIGHT_MOUSE_BUTTON || event.type === 'keyup' && event.key !== TAB_KEY$1) {
                return;
              }
              const openToggles = SelectorEngine.find(SELECTOR_DATA_TOGGLE_SHOWN);
              for (const toggle of openToggles) {
                const context = Dropdown.getInstance(toggle);
                if (!context || context._config.autoClose === false) {
                  continue;
                }
                const composedPath = event.composedPath();
                const isMenuTarget = composedPath.includes(context._menu);
                if (composedPath.includes(context._element) || context._config.autoClose === 'inside' && !isMenuTarget || context._config.autoClose === 'outside' && isMenuTarget) {
                  continue;
                }

                // Tab navigation through the dropdown menu or events from contained inputs shouldn't close the menu
                if (context._menu.contains(event.target) && (event.type === 'keyup' && event.key === TAB_KEY$1 || /input|select|option|textarea|form/i.test(event.target.tagName))) {
                  continue;
                }
                const relatedTarget = {
                  relatedTarget: context._element
                };
                if (event.type === 'click') {
                  relatedTarget.clickEvent = event;
                }
                context._completeHide(relatedTarget);
              }
            }
            static dataApiKeydownHandler(event) {
              // If not an UP | DOWN | ESCAPE key => not a dropdown command
              // If input/textarea && if key is other than ESCAPE => not a dropdown command

              const isInput = /input|textarea/i.test(event.target.tagName);
              const isEscapeEvent = event.key === ESCAPE_KEY$2;
              const isUpOrDownEvent = [ARROW_UP_KEY$1, ARROW_DOWN_KEY$1].includes(event.key);
              if (!isUpOrDownEvent && !isEscapeEvent) {
                return;
              }
              if (isInput && !isEscapeEvent) {
                return;
              }
              event.preventDefault();

              // todo: v6 revert #37011 & change markup https://getbootstrap.com/docs/5.3/forms/input-group/
              const getToggleButton = this.matches(SELECTOR_DATA_TOGGLE$3) ? this : SelectorEngine.prev(this, SELECTOR_DATA_TOGGLE$3)[0] || SelectorEngine.next(this, SELECTOR_DATA_TOGGLE$3)[0] || SelectorEngine.findOne(SELECTOR_DATA_TOGGLE$3, event.delegateTarget.parentNode);
              const instance = Dropdown.getOrCreateInstance(getToggleButton);
              if (isUpOrDownEvent) {
                event.stopPropagation();
                instance.show();
                instance._selectMenuItem(event);
                return;
              }
              if (instance._isShown()) {
                // else is escape and we check if it is shown
                event.stopPropagation();
                instance.hide();
                getToggleButton.focus();
              }
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_KEYDOWN_DATA_API, SELECTOR_DATA_TOGGLE$3, Dropdown.dataApiKeydownHandler);
          EventHandler.on(document, EVENT_KEYDOWN_DATA_API, SELECTOR_MENU, Dropdown.dataApiKeydownHandler);
          EventHandler.on(document, EVENT_CLICK_DATA_API$3, Dropdown.clearMenus);
          EventHandler.on(document, EVENT_KEYUP_DATA_API, Dropdown.clearMenus);
          EventHandler.on(document, EVENT_CLICK_DATA_API$3, SELECTOR_DATA_TOGGLE$3, function (event) {
            event.preventDefault();
            Dropdown.getOrCreateInstance(this).toggle();
          });

          /**
           * jQuery
           */

          defineJQueryPlugin(Dropdown);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/scrollBar.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const SELECTOR_FIXED_CONTENT = '.fixed-top, .fixed-bottom, .is-fixed, .sticky-top';
          const SELECTOR_STICKY_CONTENT = '.sticky-top';
          const PROPERTY_PADDING = 'padding-right';
          const PROPERTY_MARGIN = 'margin-right';

          /**
           * Class definition
           */

          class ScrollBarHelper {
            constructor() {
              this._element = document.body;
            }

            // Public
            getWidth() {
              // https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth#usage_notes
              const documentWidth = document.documentElement.clientWidth;
              return Math.abs(window.innerWidth - documentWidth);
            }
            hide() {
              const width = this.getWidth();
              this._disableOverFlow();
              // give padding to element to balance the hidden scrollbar width
              this._setElementAttributes(this._element, PROPERTY_PADDING, calculatedValue => calculatedValue + width);
              // trick: We adjust positive paddingRight and negative marginRight to sticky-top elements to keep showing fullwidth
              this._setElementAttributes(SELECTOR_FIXED_CONTENT, PROPERTY_PADDING, calculatedValue => calculatedValue + width);
              this._setElementAttributes(SELECTOR_STICKY_CONTENT, PROPERTY_MARGIN, calculatedValue => calculatedValue - width);
            }
            reset() {
              this._resetElementAttributes(this._element, 'overflow');
              this._resetElementAttributes(this._element, PROPERTY_PADDING);
              this._resetElementAttributes(SELECTOR_FIXED_CONTENT, PROPERTY_PADDING);
              this._resetElementAttributes(SELECTOR_STICKY_CONTENT, PROPERTY_MARGIN);
            }
            isOverflowing() {
              return this.getWidth() > 0;
            }

            // Private
            _disableOverFlow() {
              this._saveInitialAttribute(this._element, 'overflow');
              this._element.style.overflow = 'hidden';
            }
            _setElementAttributes(selector, styleProperty, callback) {
              const scrollbarWidth = this.getWidth();
              const manipulationCallBack = element => {
                if (element !== this._element && window.innerWidth > element.clientWidth + scrollbarWidth) {
                  return;
                }
                this._saveInitialAttribute(element, styleProperty);
                const calculatedValue = window.getComputedStyle(element).getPropertyValue(styleProperty);
                element.style.setProperty(styleProperty, `${callback(Number.parseFloat(calculatedValue))}px`);
              };
              this._applyManipulationCallback(selector, manipulationCallBack);
            }
            _saveInitialAttribute(element, styleProperty) {
              const actualValue = element.style.getPropertyValue(styleProperty);
              if (actualValue) {
                Manipulator.setDataAttribute(element, styleProperty, actualValue);
              }
            }
            _resetElementAttributes(selector, styleProperty) {
              const manipulationCallBack = element => {
                const value = Manipulator.getDataAttribute(element, styleProperty);
                // We only want to remove the property if the value is `null`; the value can also be zero
                if (value === null) {
                  element.style.removeProperty(styleProperty);
                  return;
                }
                Manipulator.removeDataAttribute(element, styleProperty);
                element.style.setProperty(styleProperty, value);
              };
              this._applyManipulationCallback(selector, manipulationCallBack);
            }
            _applyManipulationCallback(selector, callBack) {
              if (isElement(selector)) {
                callBack(selector);
                return;
              }
              for (const sel of SelectorEngine.find(selector, this._element)) {
                callBack(sel);
              }
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/backdrop.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$9 = 'backdrop';
          const CLASS_NAME_FADE$4 = 'fade';
          const CLASS_NAME_SHOW$5 = 'show';
          const EVENT_MOUSEDOWN = `mousedown.bs.${NAME$9}`;
          const Default$8 = {
            className: 'modal-backdrop',
            clickCallback: null,
            isAnimated: false,
            isVisible: true,
            // if false, we use the backdrop helper without adding any element to the dom
            rootElement: 'body' // give the choice to place backdrop under different elements
          };

          const DefaultType$8 = {
            className: 'string',
            clickCallback: '(function|null)',
            isAnimated: 'boolean',
            isVisible: 'boolean',
            rootElement: '(element|string)'
          };

          /**
           * Class definition
           */

          class Backdrop extends Config {
            constructor(config) {
              super();
              this._config = this._getConfig(config);
              this._isAppended = false;
              this._element = null;
            }

            // Getters
            static get Default() {
              return Default$8;
            }
            static get DefaultType() {
              return DefaultType$8;
            }
            static get NAME() {
              return NAME$9;
            }

            // Public
            show(callback) {
              if (!this._config.isVisible) {
                execute(callback);
                return;
              }
              this._append();
              const element = this._getElement();
              if (this._config.isAnimated) {
                reflow(element);
              }
              element.classList.add(CLASS_NAME_SHOW$5);
              this._emulateAnimation(() => {
                execute(callback);
              });
            }
            hide(callback) {
              if (!this._config.isVisible) {
                execute(callback);
                return;
              }
              this._getElement().classList.remove(CLASS_NAME_SHOW$5);
              this._emulateAnimation(() => {
                this.dispose();
                execute(callback);
              });
            }
            dispose() {
              if (!this._isAppended) {
                return;
              }
              EventHandler.off(this._element, EVENT_MOUSEDOWN);
              this._element.remove();
              this._isAppended = false;
            }

            // Private
            _getElement() {
              if (!this._element) {
                const backdrop = document.createElement('div');
                backdrop.className = this._config.className;
                if (this._config.isAnimated) {
                  backdrop.classList.add(CLASS_NAME_FADE$4);
                }
                this._element = backdrop;
              }
              return this._element;
            }
            _configAfterMerge(config) {
              // use getElement() with the default "body" to get a fresh Element on each instantiation
              config.rootElement = getElement(config.rootElement);
              return config;
            }
            _append() {
              if (this._isAppended) {
                return;
              }
              const element = this._getElement();
              this._config.rootElement.append(element);
              EventHandler.on(element, EVENT_MOUSEDOWN, () => {
                execute(this._config.clickCallback);
              });
              this._isAppended = true;
            }
            _emulateAnimation(callback) {
              executeAfterTransition(callback, this._getElement(), this._config.isAnimated);
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/focustrap.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$8 = 'focustrap';
          const DATA_KEY$5 = 'bs.focustrap';
          const EVENT_KEY$5 = `.${DATA_KEY$5}`;
          const EVENT_FOCUSIN$2 = `focusin${EVENT_KEY$5}`;
          const EVENT_KEYDOWN_TAB = `keydown.tab${EVENT_KEY$5}`;
          const TAB_KEY = 'Tab';
          const TAB_NAV_FORWARD = 'forward';
          const TAB_NAV_BACKWARD = 'backward';
          const Default$7 = {
            autofocus: true,
            trapElement: null // The element to trap focus inside of
          };

          const DefaultType$7 = {
            autofocus: 'boolean',
            trapElement: 'element'
          };

          /**
           * Class definition
           */

          class FocusTrap extends Config {
            constructor(config) {
              super();
              this._config = this._getConfig(config);
              this._isActive = false;
              this._lastTabNavDirection = null;
            }

            // Getters
            static get Default() {
              return Default$7;
            }
            static get DefaultType() {
              return DefaultType$7;
            }
            static get NAME() {
              return NAME$8;
            }

            // Public
            activate() {
              if (this._isActive) {
                return;
              }
              if (this._config.autofocus) {
                this._config.trapElement.focus();
              }
              EventHandler.off(document, EVENT_KEY$5); // guard against infinite focus loop
              EventHandler.on(document, EVENT_FOCUSIN$2, event => this._handleFocusin(event));
              EventHandler.on(document, EVENT_KEYDOWN_TAB, event => this._handleKeydown(event));
              this._isActive = true;
            }
            deactivate() {
              if (!this._isActive) {
                return;
              }
              this._isActive = false;
              EventHandler.off(document, EVENT_KEY$5);
            }

            // Private
            _handleFocusin(event) {
              const {
                trapElement
              } = this._config;
              if (event.target === document || event.target === trapElement || trapElement.contains(event.target)) {
                return;
              }
              const elements = SelectorEngine.focusableChildren(trapElement);
              if (elements.length === 0) {
                trapElement.focus();
              } else if (this._lastTabNavDirection === TAB_NAV_BACKWARD) {
                elements[elements.length - 1].focus();
              } else {
                elements[0].focus();
              }
            }
            _handleKeydown(event) {
              if (event.key !== TAB_KEY) {
                return;
              }
              this._lastTabNavDirection = event.shiftKey ? TAB_NAV_BACKWARD : TAB_NAV_FORWARD;
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap modal.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$7 = 'modal';
          const DATA_KEY$4 = 'bs.modal';
          const EVENT_KEY$4 = `.${DATA_KEY$4}`;
          const DATA_API_KEY$2 = '.data-api';
          const ESCAPE_KEY$1 = 'Escape';
          const EVENT_HIDE$4 = `hide${EVENT_KEY$4}`;
          const EVENT_HIDE_PREVENTED$1 = `hidePrevented${EVENT_KEY$4}`;
          const EVENT_HIDDEN$4 = `hidden${EVENT_KEY$4}`;
          const EVENT_SHOW$4 = `show${EVENT_KEY$4}`;
          const EVENT_SHOWN$4 = `shown${EVENT_KEY$4}`;
          const EVENT_RESIZE$1 = `resize${EVENT_KEY$4}`;
          const EVENT_CLICK_DISMISS = `click.dismiss${EVENT_KEY$4}`;
          const EVENT_MOUSEDOWN_DISMISS = `mousedown.dismiss${EVENT_KEY$4}`;
          const EVENT_KEYDOWN_DISMISS$1 = `keydown.dismiss${EVENT_KEY$4}`;
          const EVENT_CLICK_DATA_API$2 = `click${EVENT_KEY$4}${DATA_API_KEY$2}`;
          const CLASS_NAME_OPEN = 'modal-open';
          const CLASS_NAME_FADE$3 = 'fade';
          const CLASS_NAME_SHOW$4 = 'show';
          const CLASS_NAME_STATIC = 'modal-static';
          const OPEN_SELECTOR$1 = '.modal.show';
          const SELECTOR_DIALOG = '.modal-dialog';
          const SELECTOR_MODAL_BODY = '.modal-body';
          const SELECTOR_DATA_TOGGLE$2 = '[data-bs-toggle="modal"]';
          const Default$6 = {
            backdrop: true,
            focus: true,
            keyboard: true
          };
          const DefaultType$6 = {
            backdrop: '(boolean|string)',
            focus: 'boolean',
            keyboard: 'boolean'
          };

          /**
           * Class definition
           */

          class Modal extends BaseComponent {
            constructor(element, config) {
              super(element, config);
              this._dialog = SelectorEngine.findOne(SELECTOR_DIALOG, this._element);
              this._backdrop = this._initializeBackDrop();
              this._focustrap = this._initializeFocusTrap();
              this._isShown = false;
              this._isTransitioning = false;
              this._scrollBar = new ScrollBarHelper();
              this._addEventListeners();
            }

            // Getters
            static get Default() {
              return Default$6;
            }
            static get DefaultType() {
              return DefaultType$6;
            }
            static get NAME() {
              return NAME$7;
            }

            // Public
            toggle(relatedTarget) {
              return this._isShown ? this.hide() : this.show(relatedTarget);
            }
            show(relatedTarget) {
              if (this._isShown || this._isTransitioning) {
                return;
              }
              const showEvent = EventHandler.trigger(this._element, EVENT_SHOW$4, {
                relatedTarget
              });
              if (showEvent.defaultPrevented) {
                return;
              }
              this._isShown = true;
              this._isTransitioning = true;
              this._scrollBar.hide();
              document.body.classList.add(CLASS_NAME_OPEN);
              this._adjustDialog();
              this._backdrop.show(() => this._showElement(relatedTarget));
            }
            hide() {
              if (!this._isShown || this._isTransitioning) {
                return;
              }
              const hideEvent = EventHandler.trigger(this._element, EVENT_HIDE$4);
              if (hideEvent.defaultPrevented) {
                return;
              }
              this._isShown = false;
              this._isTransitioning = true;
              this._focustrap.deactivate();
              this._element.classList.remove(CLASS_NAME_SHOW$4);
              this._queueCallback(() => this._hideModal(), this._element, this._isAnimated());
            }
            dispose() {
              for (const htmlElement of [window, this._dialog]) {
                EventHandler.off(htmlElement, EVENT_KEY$4);
              }
              this._backdrop.dispose();
              this._focustrap.deactivate();
              super.dispose();
            }
            handleUpdate() {
              this._adjustDialog();
            }

            // Private
            _initializeBackDrop() {
              return new Backdrop({
                isVisible: Boolean(this._config.backdrop),
                // 'static' option will be translated to true, and booleans will keep their value,
                isAnimated: this._isAnimated()
              });
            }
            _initializeFocusTrap() {
              return new FocusTrap({
                trapElement: this._element
              });
            }
            _showElement(relatedTarget) {
              // try to append dynamic modal
              if (!document.body.contains(this._element)) {
                document.body.append(this._element);
              }
              this._element.style.display = 'block';
              this._element.removeAttribute('aria-hidden');
              this._element.setAttribute('aria-modal', true);
              this._element.setAttribute('role', 'dialog');
              this._element.scrollTop = 0;
              const modalBody = SelectorEngine.findOne(SELECTOR_MODAL_BODY, this._dialog);
              if (modalBody) {
                modalBody.scrollTop = 0;
              }
              reflow(this._element);
              this._element.classList.add(CLASS_NAME_SHOW$4);
              const transitionComplete = () => {
                if (this._config.focus) {
                  this._focustrap.activate();
                }
                this._isTransitioning = false;
                EventHandler.trigger(this._element, EVENT_SHOWN$4, {
                  relatedTarget
                });
              };
              this._queueCallback(transitionComplete, this._dialog, this._isAnimated());
            }
            _addEventListeners() {
              EventHandler.on(this._element, EVENT_KEYDOWN_DISMISS$1, event => {
                if (event.key !== ESCAPE_KEY$1) {
                  return;
                }
                if (this._config.keyboard) {
                  this.hide();
                  return;
                }
                this._triggerBackdropTransition();
              });
              EventHandler.on(window, EVENT_RESIZE$1, () => {
                if (this._isShown && !this._isTransitioning) {
                  this._adjustDialog();
                }
              });
              EventHandler.on(this._element, EVENT_MOUSEDOWN_DISMISS, event => {
                // a bad trick to segregate clicks that may start inside dialog but end outside, and avoid listen to scrollbar clicks
                EventHandler.one(this._element, EVENT_CLICK_DISMISS, event2 => {
                  if (this._element !== event.target || this._element !== event2.target) {
                    return;
                  }
                  if (this._config.backdrop === 'static') {
                    this._triggerBackdropTransition();
                    return;
                  }
                  if (this._config.backdrop) {
                    this.hide();
                  }
                });
              });
            }
            _hideModal() {
              this._element.style.display = 'none';
              this._element.setAttribute('aria-hidden', true);
              this._element.removeAttribute('aria-modal');
              this._element.removeAttribute('role');
              this._isTransitioning = false;
              this._backdrop.hide(() => {
                document.body.classList.remove(CLASS_NAME_OPEN);
                this._resetAdjustments();
                this._scrollBar.reset();
                EventHandler.trigger(this._element, EVENT_HIDDEN$4);
              });
            }
            _isAnimated() {
              return this._element.classList.contains(CLASS_NAME_FADE$3);
            }
            _triggerBackdropTransition() {
              const hideEvent = EventHandler.trigger(this._element, EVENT_HIDE_PREVENTED$1);
              if (hideEvent.defaultPrevented) {
                return;
              }
              const isModalOverflowing = this._element.scrollHeight > document.documentElement.clientHeight;
              const initialOverflowY = this._element.style.overflowY;
              // return if the following background transition hasn't yet completed
              if (initialOverflowY === 'hidden' || this._element.classList.contains(CLASS_NAME_STATIC)) {
                return;
              }
              if (!isModalOverflowing) {
                this._element.style.overflowY = 'hidden';
              }
              this._element.classList.add(CLASS_NAME_STATIC);
              this._queueCallback(() => {
                this._element.classList.remove(CLASS_NAME_STATIC);
                this._queueCallback(() => {
                  this._element.style.overflowY = initialOverflowY;
                }, this._dialog);
              }, this._dialog);
              this._element.focus();
            }

            /**
             * The following methods are used to handle overflowing modals
             */

            _adjustDialog() {
              const isModalOverflowing = this._element.scrollHeight > document.documentElement.clientHeight;
              const scrollbarWidth = this._scrollBar.getWidth();
              const isBodyOverflowing = scrollbarWidth > 0;
              if (isBodyOverflowing && !isModalOverflowing) {
                const property = isRTL() ? 'paddingLeft' : 'paddingRight';
                this._element.style[property] = `${scrollbarWidth}px`;
              }
              if (!isBodyOverflowing && isModalOverflowing) {
                const property = isRTL() ? 'paddingRight' : 'paddingLeft';
                this._element.style[property] = `${scrollbarWidth}px`;
              }
            }
            _resetAdjustments() {
              this._element.style.paddingLeft = '';
              this._element.style.paddingRight = '';
            }

            // Static
            static jQueryInterface(config, relatedTarget) {
              return this.each(function () {
                const data = Modal.getOrCreateInstance(this, config);
                if (typeof config !== 'string') {
                  return;
                }
                if (typeof data[config] === 'undefined') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config](relatedTarget);
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_CLICK_DATA_API$2, SELECTOR_DATA_TOGGLE$2, function (event) {
            const target = SelectorEngine.getElementFromSelector(this);
            if (['A', 'AREA'].includes(this.tagName)) {
              event.preventDefault();
            }
            EventHandler.one(target, EVENT_SHOW$4, showEvent => {
              if (showEvent.defaultPrevented) {
                // only register focus restorer if modal will actually get shown
                return;
              }
              EventHandler.one(target, EVENT_HIDDEN$4, () => {
                if (isVisible(this)) {
                  this.focus();
                }
              });
            });

            // avoid conflict when clicking modal toggler while another one is open
            const alreadyOpen = SelectorEngine.findOne(OPEN_SELECTOR$1);
            if (alreadyOpen) {
              Modal.getInstance(alreadyOpen).hide();
            }
            const data = Modal.getOrCreateInstance(target);
            data.toggle(this);
          });
          enableDismissTrigger(Modal);

          /**
           * jQuery
           */

          defineJQueryPlugin(Modal);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap offcanvas.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$6 = 'offcanvas';
          const DATA_KEY$3 = 'bs.offcanvas';
          const EVENT_KEY$3 = `.${DATA_KEY$3}`;
          const DATA_API_KEY$1 = '.data-api';
          const EVENT_LOAD_DATA_API$2 = `load${EVENT_KEY$3}${DATA_API_KEY$1}`;
          const ESCAPE_KEY = 'Escape';
          const CLASS_NAME_SHOW$3 = 'show';
          const CLASS_NAME_SHOWING$1 = 'showing';
          const CLASS_NAME_HIDING = 'hiding';
          const CLASS_NAME_BACKDROP = 'offcanvas-backdrop';
          const OPEN_SELECTOR = '.offcanvas.show';
          const EVENT_SHOW$3 = `show${EVENT_KEY$3}`;
          const EVENT_SHOWN$3 = `shown${EVENT_KEY$3}`;
          const EVENT_HIDE$3 = `hide${EVENT_KEY$3}`;
          const EVENT_HIDE_PREVENTED = `hidePrevented${EVENT_KEY$3}`;
          const EVENT_HIDDEN$3 = `hidden${EVENT_KEY$3}`;
          const EVENT_RESIZE = `resize${EVENT_KEY$3}`;
          const EVENT_CLICK_DATA_API$1 = `click${EVENT_KEY$3}${DATA_API_KEY$1}`;
          const EVENT_KEYDOWN_DISMISS = `keydown.dismiss${EVENT_KEY$3}`;
          const SELECTOR_DATA_TOGGLE$1 = '[data-bs-toggle="offcanvas"]';
          const Default$5 = {
            backdrop: true,
            keyboard: true,
            scroll: false
          };
          const DefaultType$5 = {
            backdrop: '(boolean|string)',
            keyboard: 'boolean',
            scroll: 'boolean'
          };

          /**
           * Class definition
           */

          class Offcanvas extends BaseComponent {
            constructor(element, config) {
              super(element, config);
              this._isShown = false;
              this._backdrop = this._initializeBackDrop();
              this._focustrap = this._initializeFocusTrap();
              this._addEventListeners();
            }

            // Getters
            static get Default() {
              return Default$5;
            }
            static get DefaultType() {
              return DefaultType$5;
            }
            static get NAME() {
              return NAME$6;
            }

            // Public
            toggle(relatedTarget) {
              return this._isShown ? this.hide() : this.show(relatedTarget);
            }
            show(relatedTarget) {
              if (this._isShown) {
                return;
              }
              const showEvent = EventHandler.trigger(this._element, EVENT_SHOW$3, {
                relatedTarget
              });
              if (showEvent.defaultPrevented) {
                return;
              }
              this._isShown = true;
              this._backdrop.show();
              if (!this._config.scroll) {
                new ScrollBarHelper().hide();
              }
              this._element.setAttribute('aria-modal', true);
              this._element.setAttribute('role', 'dialog');
              this._element.classList.add(CLASS_NAME_SHOWING$1);
              const completeCallBack = () => {
                if (!this._config.scroll || this._config.backdrop) {
                  this._focustrap.activate();
                }
                this._element.classList.add(CLASS_NAME_SHOW$3);
                this._element.classList.remove(CLASS_NAME_SHOWING$1);
                EventHandler.trigger(this._element, EVENT_SHOWN$3, {
                  relatedTarget
                });
              };
              this._queueCallback(completeCallBack, this._element, true);
            }
            hide() {
              if (!this._isShown) {
                return;
              }
              const hideEvent = EventHandler.trigger(this._element, EVENT_HIDE$3);
              if (hideEvent.defaultPrevented) {
                return;
              }
              this._focustrap.deactivate();
              this._element.blur();
              this._isShown = false;
              this._element.classList.add(CLASS_NAME_HIDING);
              this._backdrop.hide();
              const completeCallback = () => {
                this._element.classList.remove(CLASS_NAME_SHOW$3, CLASS_NAME_HIDING);
                this._element.removeAttribute('aria-modal');
                this._element.removeAttribute('role');
                if (!this._config.scroll) {
                  new ScrollBarHelper().reset();
                }
                EventHandler.trigger(this._element, EVENT_HIDDEN$3);
              };
              this._queueCallback(completeCallback, this._element, true);
            }
            dispose() {
              this._backdrop.dispose();
              this._focustrap.deactivate();
              super.dispose();
            }

            // Private
            _initializeBackDrop() {
              const clickCallback = () => {
                if (this._config.backdrop === 'static') {
                  EventHandler.trigger(this._element, EVENT_HIDE_PREVENTED);
                  return;
                }
                this.hide();
              };

              // 'static' option will be translated to true, and booleans will keep their value
              const isVisible = Boolean(this._config.backdrop);
              return new Backdrop({
                className: CLASS_NAME_BACKDROP,
                isVisible,
                isAnimated: true,
                rootElement: this._element.parentNode,
                clickCallback: isVisible ? clickCallback : null
              });
            }
            _initializeFocusTrap() {
              return new FocusTrap({
                trapElement: this._element
              });
            }
            _addEventListeners() {
              EventHandler.on(this._element, EVENT_KEYDOWN_DISMISS, event => {
                if (event.key !== ESCAPE_KEY) {
                  return;
                }
                if (this._config.keyboard) {
                  this.hide();
                  return;
                }
                EventHandler.trigger(this._element, EVENT_HIDE_PREVENTED);
              });
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Offcanvas.getOrCreateInstance(this, config);
                if (typeof config !== 'string') {
                  return;
                }
                if (data[config] === undefined || config.startsWith('_') || config === 'constructor') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config](this);
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_CLICK_DATA_API$1, SELECTOR_DATA_TOGGLE$1, function (event) {
            const target = SelectorEngine.getElementFromSelector(this);
            if (['A', 'AREA'].includes(this.tagName)) {
              event.preventDefault();
            }
            if (isDisabled(this)) {
              return;
            }
            EventHandler.one(target, EVENT_HIDDEN$3, () => {
              // focus on trigger when it is closed
              if (isVisible(this)) {
                this.focus();
              }
            });

            // avoid conflict when clicking a toggler of an offcanvas, while another is open
            const alreadyOpen = SelectorEngine.findOne(OPEN_SELECTOR);
            if (alreadyOpen && alreadyOpen !== target) {
              Offcanvas.getInstance(alreadyOpen).hide();
            }
            const data = Offcanvas.getOrCreateInstance(target);
            data.toggle(this);
          });
          EventHandler.on(window, EVENT_LOAD_DATA_API$2, () => {
            for (const selector of SelectorEngine.find(OPEN_SELECTOR)) {
              Offcanvas.getOrCreateInstance(selector).show();
            }
          });
          EventHandler.on(window, EVENT_RESIZE, () => {
            for (const element of SelectorEngine.find('[aria-modal][class*=show][class*=offcanvas-]')) {
              if (getComputedStyle(element).position !== 'fixed') {
                Offcanvas.getOrCreateInstance(element).hide();
              }
            }
          });
          enableDismissTrigger(Offcanvas);

          /**
           * jQuery
           */

          defineJQueryPlugin(Offcanvas);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/sanitizer.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          const uriAttributes = new Set(['background', 'cite', 'href', 'itemtype', 'longdesc', 'poster', 'src', 'xlink:href']);
          const ARIA_ATTRIBUTE_PATTERN = /^aria-[\w-]*$/i;

          /**
           * A pattern that recognizes a commonly useful subset of URLs that are safe.
           *
           * Shout-out to Angular https://github.com/angular/angular/blob/12.2.x/packages/core/src/sanitization/url_sanitizer.ts
           */
          const SAFE_URL_PATTERN = /^(?:(?:https?|mailto|ftp|tel|file|sms):|[^#&/:?]*(?:[#/?]|$))/i;

          /**
           * A pattern that matches safe data URLs. Only matches image, video and audio types.
           *
           * Shout-out to Angular https://github.com/angular/angular/blob/12.2.x/packages/core/src/sanitization/url_sanitizer.ts
           */
          const DATA_URL_PATTERN = /^data:(?:image\/(?:bmp|gif|jpeg|jpg|png|tiff|webp)|video\/(?:mpeg|mp4|ogg|webm)|audio\/(?:mp3|oga|ogg|opus));base64,[\d+/a-z]+=*$/i;
          const allowedAttribute = (attribute, allowedAttributeList) => {
            const attributeName = attribute.nodeName.toLowerCase();
            if (allowedAttributeList.includes(attributeName)) {
              if (uriAttributes.has(attributeName)) {
                return Boolean(SAFE_URL_PATTERN.test(attribute.nodeValue) || DATA_URL_PATTERN.test(attribute.nodeValue));
              }
              return true;
            }

            // Check if a regular expression validates the attribute.
            return allowedAttributeList.filter(attributeRegex => attributeRegex instanceof RegExp).some(regex => regex.test(attributeName));
          };
          const DefaultAllowlist = {
            // Global attributes allowed on any supplied element below.
            '*': ['class', 'dir', 'id', 'lang', 'role', ARIA_ATTRIBUTE_PATTERN],
            a: ['target', 'href', 'title', 'rel'],
            area: [],
            b: [],
            br: [],
            col: [],
            code: [],
            div: [],
            em: [],
            hr: [],
            h1: [],
            h2: [],
            h3: [],
            h4: [],
            h5: [],
            h6: [],
            i: [],
            img: ['src', 'srcset', 'alt', 'title', 'width', 'height'],
            li: [],
            ol: [],
            p: [],
            pre: [],
            s: [],
            small: [],
            span: [],
            sub: [],
            sup: [],
            strong: [],
            u: [],
            ul: []
          };
          function sanitizeHtml(unsafeHtml, allowList, sanitizeFunction) {
            if (!unsafeHtml.length) {
              return unsafeHtml;
            }
            if (sanitizeFunction && typeof sanitizeFunction === 'function') {
              return sanitizeFunction(unsafeHtml);
            }
            const domParser = new window.DOMParser();
            const createdDocument = domParser.parseFromString(unsafeHtml, 'text/html');
            const elements = [].concat(...createdDocument.body.querySelectorAll('*'));
            for (const element of elements) {
              const elementName = element.nodeName.toLowerCase();
              if (!Object.keys(allowList).includes(elementName)) {
                element.remove();
                continue;
              }
              const attributeList = [].concat(...element.attributes);
              const allowedAttributes = [].concat(allowList['*'] || [], allowList[elementName] || []);
              for (const attribute of attributeList) {
                if (!allowedAttribute(attribute, allowedAttributes)) {
                  element.removeAttribute(attribute.nodeName);
                }
              }
            }
            return createdDocument.body.innerHTML;
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap util/template-factory.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$5 = 'TemplateFactory';
          const Default$4 = {
            allowList: DefaultAllowlist,
            content: {},
            // { selector : text ,  selector2 : text2 , }
            extraClass: '',
            html: false,
            sanitize: true,
            sanitizeFn: null,
            template: '<div></div>'
          };
          const DefaultType$4 = {
            allowList: 'object',
            content: 'object',
            extraClass: '(string|function)',
            html: 'boolean',
            sanitize: 'boolean',
            sanitizeFn: '(null|function)',
            template: 'string'
          };
          const DefaultContentType = {
            entry: '(string|element|function|null)',
            selector: '(string|element)'
          };

          /**
           * Class definition
           */

          class TemplateFactory extends Config {
            constructor(config) {
              super();
              this._config = this._getConfig(config);
            }

            // Getters
            static get Default() {
              return Default$4;
            }
            static get DefaultType() {
              return DefaultType$4;
            }
            static get NAME() {
              return NAME$5;
            }

            // Public
            getContent() {
              return Object.values(this._config.content).map(config => this._resolvePossibleFunction(config)).filter(Boolean);
            }
            hasContent() {
              return this.getContent().length > 0;
            }
            changeContent(content) {
              this._checkContent(content);
              this._config.content = {
                ...this._config.content,
                ...content
              };
              return this;
            }
            toHtml() {
              const templateWrapper = document.createElement('div');
              templateWrapper.innerHTML = this._maybeSanitize(this._config.template);
              for (const [selector, text] of Object.entries(this._config.content)) {
                this._setContent(templateWrapper, text, selector);
              }
              const template = templateWrapper.children[0];
              const extraClass = this._resolvePossibleFunction(this._config.extraClass);
              if (extraClass) {
                template.classList.add(...extraClass.split(' '));
              }
              return template;
            }

            // Private
            _typeCheckConfig(config) {
              super._typeCheckConfig(config);
              this._checkContent(config.content);
            }
            _checkContent(arg) {
              for (const [selector, content] of Object.entries(arg)) {
                super._typeCheckConfig({
                  selector,
                  entry: content
                }, DefaultContentType);
              }
            }
            _setContent(template, content, selector) {
              const templateElement = SelectorEngine.findOne(selector, template);
              if (!templateElement) {
                return;
              }
              content = this._resolvePossibleFunction(content);
              if (!content) {
                templateElement.remove();
                return;
              }
              if (isElement(content)) {
                this._putElementInTemplate(getElement(content), templateElement);
                return;
              }
              if (this._config.html) {
                templateElement.innerHTML = this._maybeSanitize(content);
                return;
              }
              templateElement.textContent = content;
            }
            _maybeSanitize(arg) {
              return this._config.sanitize ? sanitizeHtml(arg, this._config.allowList, this._config.sanitizeFn) : arg;
            }
            _resolvePossibleFunction(arg) {
              return execute(arg, [this]);
            }
            _putElementInTemplate(element, templateElement) {
              if (this._config.html) {
                templateElement.innerHTML = '';
                templateElement.append(element);
                return;
              }
              templateElement.textContent = element.textContent;
            }
          }

          /**
           * --------------------------------------------------------------------------
           * Bootstrap tooltip.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$4 = 'tooltip';
          const DISALLOWED_ATTRIBUTES = new Set(['sanitize', 'allowList', 'sanitizeFn']);
          const CLASS_NAME_FADE$2 = 'fade';
          const CLASS_NAME_MODAL = 'modal';
          const CLASS_NAME_SHOW$2 = 'show';
          const SELECTOR_TOOLTIP_INNER = '.tooltip-inner';
          const SELECTOR_MODAL = `.${CLASS_NAME_MODAL}`;
          const EVENT_MODAL_HIDE = 'hide.bs.modal';
          const TRIGGER_HOVER = 'hover';
          const TRIGGER_FOCUS = 'focus';
          const TRIGGER_CLICK = 'click';
          const TRIGGER_MANUAL = 'manual';
          const EVENT_HIDE$2 = 'hide';
          const EVENT_HIDDEN$2 = 'hidden';
          const EVENT_SHOW$2 = 'show';
          const EVENT_SHOWN$2 = 'shown';
          const EVENT_INSERTED = 'inserted';
          const EVENT_CLICK$1 = 'click';
          const EVENT_FOCUSIN$1 = 'focusin';
          const EVENT_FOCUSOUT$1 = 'focusout';
          const EVENT_MOUSEENTER = 'mouseenter';
          const EVENT_MOUSELEAVE = 'mouseleave';
          const AttachmentMap = {
            AUTO: 'auto',
            TOP: 'top',
            RIGHT: isRTL() ? 'left' : 'right',
            BOTTOM: 'bottom',
            LEFT: isRTL() ? 'right' : 'left'
          };
          const Default$3 = {
            allowList: DefaultAllowlist,
            animation: true,
            boundary: 'clippingParents',
            container: false,
            customClass: '',
            delay: 0,
            fallbackPlacements: ['top', 'right', 'bottom', 'left'],
            html: false,
            offset: [0, 0],
            placement: 'top',
            popperConfig: null,
            sanitize: true,
            sanitizeFn: null,
            selector: false,
            template: '<div class="tooltip" role="tooltip">' + '<div class="tooltip-arrow"></div>' + '<div class="tooltip-inner"></div>' + '</div>',
            title: '',
            trigger: 'hover focus'
          };
          const DefaultType$3 = {
            allowList: 'object',
            animation: 'boolean',
            boundary: '(string|element)',
            container: '(string|element|boolean)',
            customClass: '(string|function)',
            delay: '(number|object)',
            fallbackPlacements: 'array',
            html: 'boolean',
            offset: '(array|string|function)',
            placement: '(string|function)',
            popperConfig: '(null|object|function)',
            sanitize: 'boolean',
            sanitizeFn: '(null|function)',
            selector: '(string|boolean)',
            template: 'string',
            title: '(string|element|function)',
            trigger: 'string'
          };

          /**
           * Class definition
           */

          class Tooltip extends BaseComponent {
            constructor(element, config) {
              if (typeof Popper__namespace === 'undefined') {
                throw new TypeError('Bootstrap\'s tooltips require Popper (https://popper.js.org)');
              }
              super(element, config);

              // Private
              this._isEnabled = true;
              this._timeout = 0;
              this._isHovered = null;
              this._activeTrigger = {};
              this._popper = null;
              this._templateFactory = null;
              this._newContent = null;

              // Protected
              this.tip = null;
              this._setListeners();
              if (!this._config.selector) {
                this._fixTitle();
              }
            }

            // Getters
            static get Default() {
              return Default$3;
            }
            static get DefaultType() {
              return DefaultType$3;
            }
            static get NAME() {
              return NAME$4;
            }

            // Public
            enable() {
              this._isEnabled = true;
            }
            disable() {
              this._isEnabled = false;
            }
            toggleEnabled() {
              this._isEnabled = !this._isEnabled;
            }
            toggle() {
              if (!this._isEnabled) {
                return;
              }
              this._activeTrigger.click = !this._activeTrigger.click;
              if (this._isShown()) {
                this._leave();
                return;
              }
              this._enter();
            }
            dispose() {
              clearTimeout(this._timeout);
              EventHandler.off(this._element.closest(SELECTOR_MODAL), EVENT_MODAL_HIDE, this._hideModalHandler);
              if (this._element.getAttribute('data-bs-original-title')) {
                this._element.setAttribute('title', this._element.getAttribute('data-bs-original-title'));
              }
              this._disposePopper();
              super.dispose();
            }
            show() {
              if (this._element.style.display === 'none') {
                throw new Error('Please use show on visible elements');
              }
              if (!(this._isWithContent() && this._isEnabled)) {
                return;
              }
              const showEvent = EventHandler.trigger(this._element, this.constructor.eventName(EVENT_SHOW$2));
              const shadowRoot = findShadowRoot(this._element);
              const isInTheDom = (shadowRoot || this._element.ownerDocument.documentElement).contains(this._element);
              if (showEvent.defaultPrevented || !isInTheDom) {
                return;
              }

              // todo v6 remove this OR make it optional
              this._disposePopper();
              const tip = this._getTipElement();
              this._element.setAttribute('aria-describedby', tip.getAttribute('id'));
              const {
                container
              } = this._config;
              if (!this._element.ownerDocument.documentElement.contains(this.tip)) {
                container.append(tip);
                EventHandler.trigger(this._element, this.constructor.eventName(EVENT_INSERTED));
              }
              this._popper = this._createPopper(tip);
              tip.classList.add(CLASS_NAME_SHOW$2);

              // If this is a touch-enabled device we add extra
              // empty mouseover listeners to the body's immediate children;
              // only needed because of broken event delegation on iOS
              // https://www.quirksmode.org/blog/archives/2014/02/mouse_event_bub.html
              if ('ontouchstart' in document.documentElement) {
                for (const element of [].concat(...document.body.children)) {
                  EventHandler.on(element, 'mouseover', noop);
                }
              }
              const complete = () => {
                EventHandler.trigger(this._element, this.constructor.eventName(EVENT_SHOWN$2));
                if (this._isHovered === false) {
                  this._leave();
                }
                this._isHovered = false;
              };
              this._queueCallback(complete, this.tip, this._isAnimated());
            }
            hide() {
              if (!this._isShown()) {
                return;
              }
              const hideEvent = EventHandler.trigger(this._element, this.constructor.eventName(EVENT_HIDE$2));
              if (hideEvent.defaultPrevented) {
                return;
              }
              const tip = this._getTipElement();
              tip.classList.remove(CLASS_NAME_SHOW$2);

              // If this is a touch-enabled device we remove the extra
              // empty mouseover listeners we added for iOS support
              if ('ontouchstart' in document.documentElement) {
                for (const element of [].concat(...document.body.children)) {
                  EventHandler.off(element, 'mouseover', noop);
                }
              }
              this._activeTrigger[TRIGGER_CLICK] = false;
              this._activeTrigger[TRIGGER_FOCUS] = false;
              this._activeTrigger[TRIGGER_HOVER] = false;
              this._isHovered = null; // it is a trick to support manual triggering

              const complete = () => {
                if (this._isWithActiveTrigger()) {
                  return;
                }
                if (!this._isHovered) {
                  this._disposePopper();
                }
                this._element.removeAttribute('aria-describedby');
                EventHandler.trigger(this._element, this.constructor.eventName(EVENT_HIDDEN$2));
              };
              this._queueCallback(complete, this.tip, this._isAnimated());
            }
            update() {
              if (this._popper) {
                this._popper.update();
              }
            }

            // Protected
            _isWithContent() {
              return Boolean(this._getTitle());
            }
            _getTipElement() {
              if (!this.tip) {
                this.tip = this._createTipElement(this._newContent || this._getContentForTemplate());
              }
              return this.tip;
            }
            _createTipElement(content) {
              const tip = this._getTemplateFactory(content).toHtml();

              // todo: remove this check on v6
              if (!tip) {
                return null;
              }
              tip.classList.remove(CLASS_NAME_FADE$2, CLASS_NAME_SHOW$2);
              // todo: on v6 the following can be achieved with CSS only
              tip.classList.add(`bs-${this.constructor.NAME}-auto`);
              const tipId = getUID(this.constructor.NAME).toString();
              tip.setAttribute('id', tipId);
              if (this._isAnimated()) {
                tip.classList.add(CLASS_NAME_FADE$2);
              }
              return tip;
            }
            setContent(content) {
              this._newContent = content;
              if (this._isShown()) {
                this._disposePopper();
                this.show();
              }
            }
            _getTemplateFactory(content) {
              if (this._templateFactory) {
                this._templateFactory.changeContent(content);
              } else {
                this._templateFactory = new TemplateFactory({
                  ...this._config,
                  // the `content` var has to be after `this._config`
                  // to override config.content in case of popover
                  content,
                  extraClass: this._resolvePossibleFunction(this._config.customClass)
                });
              }
              return this._templateFactory;
            }
            _getContentForTemplate() {
              return {
                [SELECTOR_TOOLTIP_INNER]: this._getTitle()
              };
            }
            _getTitle() {
              return this._resolvePossibleFunction(this._config.title) || this._element.getAttribute('data-bs-original-title');
            }

            // Private
            _initializeOnDelegatedTarget(event) {
              return this.constructor.getOrCreateInstance(event.delegateTarget, this._getDelegateConfig());
            }
            _isAnimated() {
              return this._config.animation || this.tip && this.tip.classList.contains(CLASS_NAME_FADE$2);
            }
            _isShown() {
              return this.tip && this.tip.classList.contains(CLASS_NAME_SHOW$2);
            }
            _createPopper(tip) {
              const placement = execute(this._config.placement, [this, tip, this._element]);
              const attachment = AttachmentMap[placement.toUpperCase()];
              return Popper__namespace.createPopper(this._element, tip, this._getPopperConfig(attachment));
            }
            _getOffset() {
              const {
                offset
              } = this._config;
              if (typeof offset === 'string') {
                return offset.split(',').map(value => Number.parseInt(value, 10));
              }
              if (typeof offset === 'function') {
                return popperData => offset(popperData, this._element);
              }
              return offset;
            }
            _resolvePossibleFunction(arg) {
              return execute(arg, [this._element]);
            }
            _getPopperConfig(attachment) {
              const defaultBsPopperConfig = {
                placement: attachment,
                modifiers: [{
                  name: 'flip',
                  options: {
                    fallbackPlacements: this._config.fallbackPlacements
                  }
                }, {
                  name: 'offset',
                  options: {
                    offset: this._getOffset()
                  }
                }, {
                  name: 'preventOverflow',
                  options: {
                    boundary: this._config.boundary
                  }
                }, {
                  name: 'arrow',
                  options: {
                    element: `.${this.constructor.NAME}-arrow`
                  }
                }, {
                  name: 'preSetPlacement',
                  enabled: true,
                  phase: 'beforeMain',
                  fn: data => {
                    // Pre-set Popper's placement attribute in order to read the arrow sizes properly.
                    // Otherwise, Popper mixes up the width and height dimensions since the initial arrow style is for top placement
                    this._getTipElement().setAttribute('data-popper-placement', data.state.placement);
                  }
                }]
              };
              return {
                ...defaultBsPopperConfig,
                ...execute(this._config.popperConfig, [defaultBsPopperConfig])
              };
            }
            _setListeners() {
              const triggers = this._config.trigger.split(' ');
              for (const trigger of triggers) {
                if (trigger === 'click') {
                  EventHandler.on(this._element, this.constructor.eventName(EVENT_CLICK$1), this._config.selector, event => {
                    const context = this._initializeOnDelegatedTarget(event);
                    context.toggle();
                  });
                } else if (trigger !== TRIGGER_MANUAL) {
                  const eventIn = trigger === TRIGGER_HOVER ? this.constructor.eventName(EVENT_MOUSEENTER) : this.constructor.eventName(EVENT_FOCUSIN$1);
                  const eventOut = trigger === TRIGGER_HOVER ? this.constructor.eventName(EVENT_MOUSELEAVE) : this.constructor.eventName(EVENT_FOCUSOUT$1);
                  EventHandler.on(this._element, eventIn, this._config.selector, event => {
                    const context = this._initializeOnDelegatedTarget(event);
                    context._activeTrigger[event.type === 'focusin' ? TRIGGER_FOCUS : TRIGGER_HOVER] = true;
                    context._enter();
                  });
                  EventHandler.on(this._element, eventOut, this._config.selector, event => {
                    const context = this._initializeOnDelegatedTarget(event);
                    context._activeTrigger[event.type === 'focusout' ? TRIGGER_FOCUS : TRIGGER_HOVER] = context._element.contains(event.relatedTarget);
                    context._leave();
                  });
                }
              }
              this._hideModalHandler = () => {
                if (this._element) {
                  this.hide();
                }
              };
              EventHandler.on(this._element.closest(SELECTOR_MODAL), EVENT_MODAL_HIDE, this._hideModalHandler);
            }
            _fixTitle() {
              const title = this._element.getAttribute('title');
              if (!title) {
                return;
              }
              if (!this._element.getAttribute('aria-label') && !this._element.textContent.trim()) {
                this._element.setAttribute('aria-label', title);
              }
              this._element.setAttribute('data-bs-original-title', title); // DO NOT USE IT. Is only for backwards compatibility
              this._element.removeAttribute('title');
            }
            _enter() {
              if (this._isShown() || this._isHovered) {
                this._isHovered = true;
                return;
              }
              this._isHovered = true;
              this._setTimeout(() => {
                if (this._isHovered) {
                  this.show();
                }
              }, this._config.delay.show);
            }
            _leave() {
              if (this._isWithActiveTrigger()) {
                return;
              }
              this._isHovered = false;
              this._setTimeout(() => {
                if (!this._isHovered) {
                  this.hide();
                }
              }, this._config.delay.hide);
            }
            _setTimeout(handler, timeout) {
              clearTimeout(this._timeout);
              this._timeout = setTimeout(handler, timeout);
            }
            _isWithActiveTrigger() {
              return Object.values(this._activeTrigger).includes(true);
            }
            _getConfig(config) {
              const dataAttributes = Manipulator.getDataAttributes(this._element);
              for (const dataAttribute of Object.keys(dataAttributes)) {
                if (DISALLOWED_ATTRIBUTES.has(dataAttribute)) {
                  delete dataAttributes[dataAttribute];
                }
              }
              config = {
                ...dataAttributes,
                ...(typeof config === 'object' && config ? config : {})
              };
              config = this._mergeConfigObj(config);
              config = this._configAfterMerge(config);
              this._typeCheckConfig(config);
              return config;
            }
            _configAfterMerge(config) {
              config.container = config.container === false ? document.body : getElement(config.container);
              if (typeof config.delay === 'number') {
                config.delay = {
                  show: config.delay,
                  hide: config.delay
                };
              }
              if (typeof config.title === 'number') {
                config.title = config.title.toString();
              }
              if (typeof config.content === 'number') {
                config.content = config.content.toString();
              }
              return config;
            }
            _getDelegateConfig() {
              const config = {};
              for (const [key, value] of Object.entries(this._config)) {
                if (this.constructor.Default[key] !== value) {
                  config[key] = value;
                }
              }
              config.selector = false;
              config.trigger = 'manual';

              // In the future can be replaced with:
              // const keysWithDifferentValues = Object.entries(this._config).filter(entry => this.constructor.Default[entry[0]] !== this._config[entry[0]])
              // `Object.fromEntries(keysWithDifferentValues)`
              return config;
            }
            _disposePopper() {
              if (this._popper) {
                this._popper.destroy();
                this._popper = null;
              }
              if (this.tip) {
                this.tip.remove();
                this.tip = null;
              }
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Tooltip.getOrCreateInstance(this, config);
                if (typeof config !== 'string') {
                  return;
                }
                if (typeof data[config] === 'undefined') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config]();
              });
            }
          }

          /**
           * jQuery
           */

          defineJQueryPlugin(Tooltip);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap popover.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$3 = 'popover';
          const SELECTOR_TITLE = '.popover-header';
          const SELECTOR_CONTENT = '.popover-body';
          const Default$2 = {
            ...Tooltip.Default,
            content: '',
            offset: [0, 8],
            placement: 'right',
            template: '<div class="popover" role="tooltip">' + '<div class="popover-arrow"></div>' + '<h3 class="popover-header"></h3>' + '<div class="popover-body"></div>' + '</div>',
            trigger: 'click'
          };
          const DefaultType$2 = {
            ...Tooltip.DefaultType,
            content: '(null|string|element|function)'
          };

          /**
           * Class definition
           */

          class Popover extends Tooltip {
            // Getters
            static get Default() {
              return Default$2;
            }
            static get DefaultType() {
              return DefaultType$2;
            }
            static get NAME() {
              return NAME$3;
            }

            // Overrides
            _isWithContent() {
              return this._getTitle() || this._getContent();
            }

            // Private
            _getContentForTemplate() {
              return {
                [SELECTOR_TITLE]: this._getTitle(),
                [SELECTOR_CONTENT]: this._getContent()
              };
            }
            _getContent() {
              return this._resolvePossibleFunction(this._config.content);
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Popover.getOrCreateInstance(this, config);
                if (typeof config !== 'string') {
                  return;
                }
                if (typeof data[config] === 'undefined') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config]();
              });
            }
          }

          /**
           * jQuery
           */

          defineJQueryPlugin(Popover);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap scrollspy.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$2 = 'scrollspy';
          const DATA_KEY$2 = 'bs.scrollspy';
          const EVENT_KEY$2 = `.${DATA_KEY$2}`;
          const DATA_API_KEY = '.data-api';
          const EVENT_ACTIVATE = `activate${EVENT_KEY$2}`;
          const EVENT_CLICK = `click${EVENT_KEY$2}`;
          const EVENT_LOAD_DATA_API$1 = `load${EVENT_KEY$2}${DATA_API_KEY}`;
          const CLASS_NAME_DROPDOWN_ITEM = 'dropdown-item';
          const CLASS_NAME_ACTIVE$1 = 'active';
          const SELECTOR_DATA_SPY = '[data-bs-spy="scroll"]';
          const SELECTOR_TARGET_LINKS = '[href]';
          const SELECTOR_NAV_LIST_GROUP = '.nav, .list-group';
          const SELECTOR_NAV_LINKS = '.nav-link';
          const SELECTOR_NAV_ITEMS = '.nav-item';
          const SELECTOR_LIST_ITEMS = '.list-group-item';
          const SELECTOR_LINK_ITEMS = `${SELECTOR_NAV_LINKS}, ${SELECTOR_NAV_ITEMS} > ${SELECTOR_NAV_LINKS}, ${SELECTOR_LIST_ITEMS}`;
          const SELECTOR_DROPDOWN = '.dropdown';
          const SELECTOR_DROPDOWN_TOGGLE$1 = '.dropdown-toggle';
          const Default$1 = {
            offset: null,
            // TODO: v6 @deprecated, keep it for backwards compatibility reasons
            rootMargin: '0px 0px -25%',
            smoothScroll: false,
            target: null,
            threshold: [0.1, 0.5, 1]
          };
          const DefaultType$1 = {
            offset: '(number|null)',
            // TODO v6 @deprecated, keep it for backwards compatibility reasons
            rootMargin: 'string',
            smoothScroll: 'boolean',
            target: 'element',
            threshold: 'array'
          };

          /**
           * Class definition
           */

          class ScrollSpy extends BaseComponent {
            constructor(element, config) {
              super(element, config);

              // this._element is the observablesContainer and config.target the menu links wrapper
              this._targetLinks = new Map();
              this._observableSections = new Map();
              this._rootElement = getComputedStyle(this._element).overflowY === 'visible' ? null : this._element;
              this._activeTarget = null;
              this._observer = null;
              this._previousScrollData = {
                visibleEntryTop: 0,
                parentScrollTop: 0
              };
              this.refresh(); // initialize
            }

            // Getters
            static get Default() {
              return Default$1;
            }
            static get DefaultType() {
              return DefaultType$1;
            }
            static get NAME() {
              return NAME$2;
            }

            // Public
            refresh() {
              this._initializeTargetsAndObservables();
              this._maybeEnableSmoothScroll();
              if (this._observer) {
                this._observer.disconnect();
              } else {
                this._observer = this._getNewObserver();
              }
              for (const section of this._observableSections.values()) {
                this._observer.observe(section);
              }
            }
            dispose() {
              this._observer.disconnect();
              super.dispose();
            }

            // Private
            _configAfterMerge(config) {
              // TODO: on v6 target should be given explicitly & remove the {target: 'ss-target'} case
              config.target = getElement(config.target) || document.body;

              // TODO: v6 Only for backwards compatibility reasons. Use rootMargin only
              config.rootMargin = config.offset ? `${config.offset}px 0px -30%` : config.rootMargin;
              if (typeof config.threshold === 'string') {
                config.threshold = config.threshold.split(',').map(value => Number.parseFloat(value));
              }
              return config;
            }
            _maybeEnableSmoothScroll() {
              if (!this._config.smoothScroll) {
                return;
              }

              // unregister any previous listeners
              EventHandler.off(this._config.target, EVENT_CLICK);
              EventHandler.on(this._config.target, EVENT_CLICK, SELECTOR_TARGET_LINKS, event => {
                const observableSection = this._observableSections.get(event.target.hash);
                if (observableSection) {
                  event.preventDefault();
                  const root = this._rootElement || window;
                  const height = observableSection.offsetTop - this._element.offsetTop;
                  if (root.scrollTo) {
                    root.scrollTo({
                      top: height,
                      behavior: 'smooth'
                    });
                    return;
                  }

                  // Chrome 60 doesn't support `scrollTo`
                  root.scrollTop = height;
                }
              });
            }
            _getNewObserver() {
              const options = {
                root: this._rootElement,
                threshold: this._config.threshold,
                rootMargin: this._config.rootMargin
              };
              return new IntersectionObserver(entries => this._observerCallback(entries), options);
            }

            // The logic of selection
            _observerCallback(entries) {
              const targetElement = entry => this._targetLinks.get(`#${entry.target.id}`);
              const activate = entry => {
                this._previousScrollData.visibleEntryTop = entry.target.offsetTop;
                this._process(targetElement(entry));
              };
              const parentScrollTop = (this._rootElement || document.documentElement).scrollTop;
              const userScrollsDown = parentScrollTop >= this._previousScrollData.parentScrollTop;
              this._previousScrollData.parentScrollTop = parentScrollTop;
              for (const entry of entries) {
                if (!entry.isIntersecting) {
                  this._activeTarget = null;
                  this._clearActiveClass(targetElement(entry));
                  continue;
                }
                const entryIsLowerThanPrevious = entry.target.offsetTop >= this._previousScrollData.visibleEntryTop;
                // if we are scrolling down, pick the bigger offsetTop
                if (userScrollsDown && entryIsLowerThanPrevious) {
                  activate(entry);
                  // if parent isn't scrolled, let's keep the first visible item, breaking the iteration
                  if (!parentScrollTop) {
                    return;
                  }
                  continue;
                }

                // if we are scrolling up, pick the smallest offsetTop
                if (!userScrollsDown && !entryIsLowerThanPrevious) {
                  activate(entry);
                }
              }
            }
            _initializeTargetsAndObservables() {
              this._targetLinks = new Map();
              this._observableSections = new Map();
              const targetLinks = SelectorEngine.find(SELECTOR_TARGET_LINKS, this._config.target);
              for (const anchor of targetLinks) {
                // ensure that the anchor has an id and is not disabled
                if (!anchor.hash || isDisabled(anchor)) {
                  continue;
                }
                const observableSection = SelectorEngine.findOne(anchor.hash, this._element);

                // ensure that the observableSection exists & is visible
                if (isVisible(observableSection)) {
                  this._targetLinks.set(anchor.hash, anchor);
                  this._observableSections.set(anchor.hash, observableSection);
                }
              }
            }
            _process(target) {
              if (this._activeTarget === target) {
                return;
              }
              this._clearActiveClass(this._config.target);
              this._activeTarget = target;
              target.classList.add(CLASS_NAME_ACTIVE$1);
              this._activateParents(target);
              EventHandler.trigger(this._element, EVENT_ACTIVATE, {
                relatedTarget: target
              });
            }
            _activateParents(target) {
              // Activate dropdown parents
              if (target.classList.contains(CLASS_NAME_DROPDOWN_ITEM)) {
                SelectorEngine.findOne(SELECTOR_DROPDOWN_TOGGLE$1, target.closest(SELECTOR_DROPDOWN)).classList.add(CLASS_NAME_ACTIVE$1);
                return;
              }
              for (const listGroup of SelectorEngine.parents(target, SELECTOR_NAV_LIST_GROUP)) {
                // Set triggered links parents as active
                // With both <ul> and <nav> markup a parent is the previous sibling of any nav ancestor
                for (const item of SelectorEngine.prev(listGroup, SELECTOR_LINK_ITEMS)) {
                  item.classList.add(CLASS_NAME_ACTIVE$1);
                }
              }
            }
            _clearActiveClass(parent) {
              parent.classList.remove(CLASS_NAME_ACTIVE$1);
              const activeNodes = SelectorEngine.find(`${SELECTOR_TARGET_LINKS}.${CLASS_NAME_ACTIVE$1}`, parent);
              for (const node of activeNodes) {
                node.classList.remove(CLASS_NAME_ACTIVE$1);
              }
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = ScrollSpy.getOrCreateInstance(this, config);
                if (typeof config !== 'string') {
                  return;
                }
                if (data[config] === undefined || config.startsWith('_') || config === 'constructor') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config]();
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(window, EVENT_LOAD_DATA_API$1, () => {
            for (const spy of SelectorEngine.find(SELECTOR_DATA_SPY)) {
              ScrollSpy.getOrCreateInstance(spy);
            }
          });

          /**
           * jQuery
           */

          defineJQueryPlugin(ScrollSpy);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap tab.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME$1 = 'tab';
          const DATA_KEY$1 = 'bs.tab';
          const EVENT_KEY$1 = `.${DATA_KEY$1}`;
          const EVENT_HIDE$1 = `hide${EVENT_KEY$1}`;
          const EVENT_HIDDEN$1 = `hidden${EVENT_KEY$1}`;
          const EVENT_SHOW$1 = `show${EVENT_KEY$1}`;
          const EVENT_SHOWN$1 = `shown${EVENT_KEY$1}`;
          const EVENT_CLICK_DATA_API = `click${EVENT_KEY$1}`;
          const EVENT_KEYDOWN = `keydown${EVENT_KEY$1}`;
          const EVENT_LOAD_DATA_API = `load${EVENT_KEY$1}`;
          const ARROW_LEFT_KEY = 'ArrowLeft';
          const ARROW_RIGHT_KEY = 'ArrowRight';
          const ARROW_UP_KEY = 'ArrowUp';
          const ARROW_DOWN_KEY = 'ArrowDown';
          const CLASS_NAME_ACTIVE = 'active';
          const CLASS_NAME_FADE$1 = 'fade';
          const CLASS_NAME_SHOW$1 = 'show';
          const CLASS_DROPDOWN = 'dropdown';
          const SELECTOR_DROPDOWN_TOGGLE = '.dropdown-toggle';
          const SELECTOR_DROPDOWN_MENU = '.dropdown-menu';
          const NOT_SELECTOR_DROPDOWN_TOGGLE = ':not(.dropdown-toggle)';
          const SELECTOR_TAB_PANEL = '.list-group, .nav, [role="tablist"]';
          const SELECTOR_OUTER = '.nav-item, .list-group-item';
          const SELECTOR_INNER = `.nav-link${NOT_SELECTOR_DROPDOWN_TOGGLE}, .list-group-item${NOT_SELECTOR_DROPDOWN_TOGGLE}, [role="tab"]${NOT_SELECTOR_DROPDOWN_TOGGLE}`;
          const SELECTOR_DATA_TOGGLE = '[data-bs-toggle="tab"], [data-bs-toggle="pill"], [data-bs-toggle="list"]'; // todo:v6: could be only `tab`
          const SELECTOR_INNER_ELEM = `${SELECTOR_INNER}, ${SELECTOR_DATA_TOGGLE}`;
          const SELECTOR_DATA_TOGGLE_ACTIVE = `.${CLASS_NAME_ACTIVE}[data-bs-toggle="tab"], .${CLASS_NAME_ACTIVE}[data-bs-toggle="pill"], .${CLASS_NAME_ACTIVE}[data-bs-toggle="list"]`;

          /**
           * Class definition
           */

          class Tab extends BaseComponent {
            constructor(element) {
              super(element);
              this._parent = this._element.closest(SELECTOR_TAB_PANEL);
              if (!this._parent) {
                return;
                // todo: should Throw exception on v6
                // throw new TypeError(`${element.outerHTML} has not a valid parent ${SELECTOR_INNER_ELEM}`)
              }

              // Set up initial aria attributes
              this._setInitialAttributes(this._parent, this._getChildren());
              EventHandler.on(this._element, EVENT_KEYDOWN, event => this._keydown(event));
            }

            // Getters
            static get NAME() {
              return NAME$1;
            }

            // Public
            show() {
              // Shows this elem and deactivate the active sibling if exists
              const innerElem = this._element;
              if (this._elemIsActive(innerElem)) {
                return;
              }

              // Search for active tab on same parent to deactivate it
              const active = this._getActiveElem();
              const hideEvent = active ? EventHandler.trigger(active, EVENT_HIDE$1, {
                relatedTarget: innerElem
              }) : null;
              const showEvent = EventHandler.trigger(innerElem, EVENT_SHOW$1, {
                relatedTarget: active
              });
              if (showEvent.defaultPrevented || hideEvent && hideEvent.defaultPrevented) {
                return;
              }
              this._deactivate(active, innerElem);
              this._activate(innerElem, active);
            }

            // Private
            _activate(element, relatedElem) {
              if (!element) {
                return;
              }
              element.classList.add(CLASS_NAME_ACTIVE);
              this._activate(SelectorEngine.getElementFromSelector(element)); // Search and activate/show the proper section

              const complete = () => {
                if (element.getAttribute('role') !== 'tab') {
                  element.classList.add(CLASS_NAME_SHOW$1);
                  return;
                }
                element.removeAttribute('tabindex');
                element.setAttribute('aria-selected', true);
                this._toggleDropDown(element, true);
                EventHandler.trigger(element, EVENT_SHOWN$1, {
                  relatedTarget: relatedElem
                });
              };
              this._queueCallback(complete, element, element.classList.contains(CLASS_NAME_FADE$1));
            }
            _deactivate(element, relatedElem) {
              if (!element) {
                return;
              }
              element.classList.remove(CLASS_NAME_ACTIVE);
              element.blur();
              this._deactivate(SelectorEngine.getElementFromSelector(element)); // Search and deactivate the shown section too

              const complete = () => {
                if (element.getAttribute('role') !== 'tab') {
                  element.classList.remove(CLASS_NAME_SHOW$1);
                  return;
                }
                element.setAttribute('aria-selected', false);
                element.setAttribute('tabindex', '-1');
                this._toggleDropDown(element, false);
                EventHandler.trigger(element, EVENT_HIDDEN$1, {
                  relatedTarget: relatedElem
                });
              };
              this._queueCallback(complete, element, element.classList.contains(CLASS_NAME_FADE$1));
            }
            _keydown(event) {
              if (![ARROW_LEFT_KEY, ARROW_RIGHT_KEY, ARROW_UP_KEY, ARROW_DOWN_KEY].includes(event.key)) {
                return;
              }
              event.stopPropagation(); // stopPropagation/preventDefault both added to support up/down keys without scrolling the page
              event.preventDefault();
              const isNext = [ARROW_RIGHT_KEY, ARROW_DOWN_KEY].includes(event.key);
              const nextActiveElement = getNextActiveElement(this._getChildren().filter(element => !isDisabled(element)), event.target, isNext, true);
              if (nextActiveElement) {
                nextActiveElement.focus({
                  preventScroll: true
                });
                Tab.getOrCreateInstance(nextActiveElement).show();
              }
            }
            _getChildren() {
              // collection of inner elements
              return SelectorEngine.find(SELECTOR_INNER_ELEM, this._parent);
            }
            _getActiveElem() {
              return this._getChildren().find(child => this._elemIsActive(child)) || null;
            }
            _setInitialAttributes(parent, children) {
              this._setAttributeIfNotExists(parent, 'role', 'tablist');
              for (const child of children) {
                this._setInitialAttributesOnChild(child);
              }
            }
            _setInitialAttributesOnChild(child) {
              child = this._getInnerElement(child);
              const isActive = this._elemIsActive(child);
              const outerElem = this._getOuterElement(child);
              child.setAttribute('aria-selected', isActive);
              if (outerElem !== child) {
                this._setAttributeIfNotExists(outerElem, 'role', 'presentation');
              }
              if (!isActive) {
                child.setAttribute('tabindex', '-1');
              }
              this._setAttributeIfNotExists(child, 'role', 'tab');

              // set attributes to the related panel too
              this._setInitialAttributesOnTargetPanel(child);
            }
            _setInitialAttributesOnTargetPanel(child) {
              const target = SelectorEngine.getElementFromSelector(child);
              if (!target) {
                return;
              }
              this._setAttributeIfNotExists(target, 'role', 'tabpanel');
              if (child.id) {
                this._setAttributeIfNotExists(target, 'aria-labelledby', `${child.id}`);
              }
            }
            _toggleDropDown(element, open) {
              const outerElem = this._getOuterElement(element);
              if (!outerElem.classList.contains(CLASS_DROPDOWN)) {
                return;
              }
              const toggle = (selector, className) => {
                const element = SelectorEngine.findOne(selector, outerElem);
                if (element) {
                  element.classList.toggle(className, open);
                }
              };
              toggle(SELECTOR_DROPDOWN_TOGGLE, CLASS_NAME_ACTIVE);
              toggle(SELECTOR_DROPDOWN_MENU, CLASS_NAME_SHOW$1);
              outerElem.setAttribute('aria-expanded', open);
            }
            _setAttributeIfNotExists(element, attribute, value) {
              if (!element.hasAttribute(attribute)) {
                element.setAttribute(attribute, value);
              }
            }
            _elemIsActive(elem) {
              return elem.classList.contains(CLASS_NAME_ACTIVE);
            }

            // Try to get the inner element (usually the .nav-link)
            _getInnerElement(elem) {
              return elem.matches(SELECTOR_INNER_ELEM) ? elem : SelectorEngine.findOne(SELECTOR_INNER_ELEM, elem);
            }

            // Try to get the outer element (usually the .nav-item)
            _getOuterElement(elem) {
              return elem.closest(SELECTOR_OUTER) || elem;
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Tab.getOrCreateInstance(this);
                if (typeof config !== 'string') {
                  return;
                }
                if (data[config] === undefined || config.startsWith('_') || config === 'constructor') {
                  throw new TypeError(`No method named "${config}"`);
                }
                data[config]();
              });
            }
          }

          /**
           * Data API implementation
           */

          EventHandler.on(document, EVENT_CLICK_DATA_API, SELECTOR_DATA_TOGGLE, function (event) {
            if (['A', 'AREA'].includes(this.tagName)) {
              event.preventDefault();
            }
            if (isDisabled(this)) {
              return;
            }
            Tab.getOrCreateInstance(this).show();
          });

          /**
           * Initialize on focus
           */
          EventHandler.on(window, EVENT_LOAD_DATA_API, () => {
            for (const element of SelectorEngine.find(SELECTOR_DATA_TOGGLE_ACTIVE)) {
              Tab.getOrCreateInstance(element);
            }
          });
          /**
           * jQuery
           */

          defineJQueryPlugin(Tab);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap toast.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */

          /**
           * Constants
           */

          const NAME = 'toast';
          const DATA_KEY = 'bs.toast';
          const EVENT_KEY = `.${DATA_KEY}`;
          const EVENT_MOUSEOVER = `mouseover${EVENT_KEY}`;
          const EVENT_MOUSEOUT = `mouseout${EVENT_KEY}`;
          const EVENT_FOCUSIN = `focusin${EVENT_KEY}`;
          const EVENT_FOCUSOUT = `focusout${EVENT_KEY}`;
          const EVENT_HIDE = `hide${EVENT_KEY}`;
          const EVENT_HIDDEN = `hidden${EVENT_KEY}`;
          const EVENT_SHOW = `show${EVENT_KEY}`;
          const EVENT_SHOWN = `shown${EVENT_KEY}`;
          const CLASS_NAME_FADE = 'fade';
          const CLASS_NAME_HIDE = 'hide'; // @deprecated - kept here only for backwards compatibility
          const CLASS_NAME_SHOW = 'show';
          const CLASS_NAME_SHOWING = 'showing';
          const DefaultType = {
            animation: 'boolean',
            autohide: 'boolean',
            delay: 'number'
          };
          const Default = {
            animation: true,
            autohide: true,
            delay: 5000
          };

          /**
           * Class definition
           */

          class Toast extends BaseComponent {
            constructor(element, config) {
              super(element, config);
              this._timeout = null;
              this._hasMouseInteraction = false;
              this._hasKeyboardInteraction = false;
              this._setListeners();
            }

            // Getters
            static get Default() {
              return Default;
            }
            static get DefaultType() {
              return DefaultType;
            }
            static get NAME() {
              return NAME;
            }

            // Public
            show() {
              const showEvent = EventHandler.trigger(this._element, EVENT_SHOW);
              if (showEvent.defaultPrevented) {
                return;
              }
              this._clearTimeout();
              if (this._config.animation) {
                this._element.classList.add(CLASS_NAME_FADE);
              }
              const complete = () => {
                this._element.classList.remove(CLASS_NAME_SHOWING);
                EventHandler.trigger(this._element, EVENT_SHOWN);
                this._maybeScheduleHide();
              };
              this._element.classList.remove(CLASS_NAME_HIDE); // @deprecated
              reflow(this._element);
              this._element.classList.add(CLASS_NAME_SHOW, CLASS_NAME_SHOWING);
              this._queueCallback(complete, this._element, this._config.animation);
            }
            hide() {
              if (!this.isShown()) {
                return;
              }
              const hideEvent = EventHandler.trigger(this._element, EVENT_HIDE);
              if (hideEvent.defaultPrevented) {
                return;
              }
              const complete = () => {
                this._element.classList.add(CLASS_NAME_HIDE); // @deprecated
                this._element.classList.remove(CLASS_NAME_SHOWING, CLASS_NAME_SHOW);
                EventHandler.trigger(this._element, EVENT_HIDDEN);
              };
              this._element.classList.add(CLASS_NAME_SHOWING);
              this._queueCallback(complete, this._element, this._config.animation);
            }
            dispose() {
              this._clearTimeout();
              if (this.isShown()) {
                this._element.classList.remove(CLASS_NAME_SHOW);
              }
              super.dispose();
            }
            isShown() {
              return this._element.classList.contains(CLASS_NAME_SHOW);
            }

            // Private

            _maybeScheduleHide() {
              if (!this._config.autohide) {
                return;
              }
              if (this._hasMouseInteraction || this._hasKeyboardInteraction) {
                return;
              }
              this._timeout = setTimeout(() => {
                this.hide();
              }, this._config.delay);
            }
            _onInteraction(event, isInteracting) {
              switch (event.type) {
                case 'mouseover':
                case 'mouseout':
                  {
                    this._hasMouseInteraction = isInteracting;
                    break;
                  }
                case 'focusin':
                case 'focusout':
                  {
                    this._hasKeyboardInteraction = isInteracting;
                    break;
                  }
              }
              if (isInteracting) {
                this._clearTimeout();
                return;
              }
              const nextElement = event.relatedTarget;
              if (this._element === nextElement || this._element.contains(nextElement)) {
                return;
              }
              this._maybeScheduleHide();
            }
            _setListeners() {
              EventHandler.on(this._element, EVENT_MOUSEOVER, event => this._onInteraction(event, true));
              EventHandler.on(this._element, EVENT_MOUSEOUT, event => this._onInteraction(event, false));
              EventHandler.on(this._element, EVENT_FOCUSIN, event => this._onInteraction(event, true));
              EventHandler.on(this._element, EVENT_FOCUSOUT, event => this._onInteraction(event, false));
            }
            _clearTimeout() {
              clearTimeout(this._timeout);
              this._timeout = null;
            }

            // Static
            static jQueryInterface(config) {
              return this.each(function () {
                const data = Toast.getOrCreateInstance(this, config);
                if (typeof config === 'string') {
                  if (typeof data[config] === 'undefined') {
                    throw new TypeError(`No method named "${config}"`);
                  }
                  data[config](this);
                }
              });
            }
          }

          /**
           * Data API implementation
           */

          enableDismissTrigger(Toast);

          /**
           * jQuery
           */

          defineJQueryPlugin(Toast);

          /**
           * --------------------------------------------------------------------------
           * Bootstrap index.umd.js
           * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
           * --------------------------------------------------------------------------
           */
          const index_umd = {
            Alert,
            Button,
            Carousel,
            Collapse,
            Dropdown,
            Modal,
            Offcanvas,
            Popover,
            ScrollSpy,
            Tab,
            Toast,
            Tooltip
          };

          return index_umd;

        }));
        //# sourceMappingURL=bootstrap.js.map

    </script>
    """
    st.markdown(boostrap_js, unsafe_allow_html=True)

    general_style = """
    
      <style>
            .main-horizontal-menu{
                text-decoration: none; 
                color: white; 
                font-size: 2rem;
                border: 1px solid gray;
                border-radius: 5px;
                padding: 10px;
            }
            a.main-horizontal-menu{
                text-decoration: none; 
                color: white;
            }
            
            .main-horizontal-menu:hover{
                border: 1px solid orange;
                padding: 15px;
            }
            
            p > a.main-horizontal-menu{
                visibility: hidden;
            }
            
            div.stApp{
                background-color:#2C2C2C;
            }
            
           section.main > div.block-container{
                padding: 0rem 5rem 10rem 10rem;
            }
        </style>
    """
    st.markdown(general_style, unsafe_allow_html=True)  # Apply general style

    hide_menu = """
    <style>
        #MainMenu{
            visibility: Visible;  # hidden
        }
        div.stApp > header{
            visibility: Visible;  # hidden
        }
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)  # Hiding the main menu (at the top-right)

    remove_page_top_padding = """
        <style>
            .st-emotion-cache-z5fcl4{
                padding-top: 0;
            }
        </style>
    """
    st.markdown(remove_page_top_padding, unsafe_allow_html=True)  # Hiding the main menu (at the top-right)

    content_style = """
        <style>
            h1.custom_title_h1{
                text-align:center;
                color: gray
            }
            h4.custom_setting_section_h4{
                color: gray
            }
            
        </style>
        
    """
    st.markdown(content_style, unsafe_allow_html=True)  # Add style to page content

    hide_footer = """
    <style>
        footer{
            visibility: hidden
        }
    </style>
    """
    st.markdown(hide_footer, unsafe_allow_html=True)  # Hiding the main menu (at the top-right)

    add_html_divider = """
        <style>
            hr {
              display: block;
              margin-top: 0.5em;
              margin-bottom: 0.5em;
              margin-left: auto;
              margin-right: auto;
              border-style: inset;
            }

            .main-title-divider{
              border-width: 10px;
            }

            .section-divider{
              border-width: 1px;
            }

            .domain-divider{
              border-width: 1px;
            }
        </style>
    """

    st.markdown(add_html_divider, unsafe_allow_html=True)


def format_an_upcoming_event_display(event: dict, display_num_char: int | None = None):
    event_description = event['text'] if display_num_char is None else event['text'][0:display_num_char]
    if len(event_description) < len(event['text']):
        event_description += " . . ."
    return f"""
        <a href="#">
            <div class="card text-bg-dark" style="width: 25em;">
              <img src="data:image/png;base64,{get_article_image_base64(event['image_name'])}" class="card-img" alt="...">
              <div class="card-img-overlay" style="background-color: rgba(0,0,0,0.5);">
                <p class="card-text">{event_description}</p>
              </div>
            </div>
        </a>
    """


def format_article_display(article: list[dict]):
    article_markdown = ""
    for i, paragraph in enumerate(article):
        if i % 2 == 0:
            article_markdown += f"""
                <div class="card mb-3 col-md-7">
                  <div class="row g-0">
                    <div class="col-md-4" style="max-width: 240px;">
                      <img src="{paragraph['image_url']}" 
                      class="img-fluid rounded-start" alt="...">
                    </div>
                    <div class="col-md-8">
                      <div class="card-body">
                        <!--h5 class="card-title">title</h5 -->
                        <p class="card-text">{paragraph['text']}</p>
                      </div>
                    </div>
                  </div>
                </div>
                """
        else:
            article_markdown += f"""
                <div class="card mb-3 col-md-7">
                  <div class="row g-0">
                    <div class="col-md-8">
                      <div class="card-body">
                        <!--h5 class="card-title">title</h5 -->
                        <p class="card-text">{paragraph['text']}</p>
                      </div>
                    </div>
                    <div class="col-md-4" style="max-width: 240px;">
                      <img src="{paragraph['image_url']}" 
                      class="img-fluid rounded-start" alt="...">
                    </div>
                  </div>
                </div>
                """
    return article_markdown
