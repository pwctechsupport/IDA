--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

-- Started on 2022-11-28 03:23:05

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3475 (class 1262 OID 16394)
-- Name: IDA; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "IDA" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';


ALTER DATABASE "IDA" OWNER TO postgres;

\connect "IDA"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 231 (class 1259 OID 16562)
-- Name: UserFirstLogin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."UserFirstLogin" (
    "UserLoginID" integer NOT NULL,
    "Username" text NOT NULL,
    "Password" text NOT NULL,
    "LastLogin" timestamp without time zone
);


ALTER TABLE public."UserFirstLogin" OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16561)
-- Name: UserFirstLogin_UserLoginID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."UserFirstLogin_UserLoginID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."UserFirstLogin_UserLoginID_seq" OWNER TO postgres;

--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 230
-- Name: UserFirstLogin_UserLoginID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."UserFirstLogin_UserLoginID_seq" OWNED BY public."UserFirstLogin"."UserLoginID";


--
-- TOC entry 233 (class 1259 OID 16572)
-- Name: UserLogin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."UserLogin" (
    "UserLoginID" integer NOT NULL,
    "Username" text NOT NULL,
    "Password" text NOT NULL,
    "LastLogin" timestamp without time zone
);


ALTER TABLE public."UserLogin" OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 16571)
-- Name: UserLogin_UserLoginID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."UserLogin_UserLoginID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."UserLogin_UserLoginID_seq" OWNER TO postgres;

--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 232
-- Name: UserLogin_UserLoginID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."UserLogin_UserLoginID_seq" OWNED BY public."UserLogin"."UserLoginID";


--
-- TOC entry 218 (class 1259 OID 16429)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16428)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 217
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 220 (class 1259 OID 16438)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16437)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 219
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 216 (class 1259 OID 16422)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16421)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 3480 (class 0 OID 0)
-- Dependencies: 215
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 222 (class 1259 OID 16445)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16454)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16453)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- TOC entry 3481 (class 0 OID 0)
-- Dependencies: 223
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- TOC entry 221 (class 1259 OID 16444)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- TOC entry 3482 (class 0 OID 0)
-- Dependencies: 221
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- TOC entry 226 (class 1259 OID 16461)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16460)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3483 (class 0 OID 0)
-- Dependencies: 225
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- TOC entry 209 (class 1259 OID 16395)
-- Name: chatlist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chatlist (
    chatlistid integer NOT NULL,
    chatlistcode text,
    description text,
    isquestion integer,
    parentchatcode text,
    status integer,
    "Order" integer,
    isreset integer,
    isupload integer,
    mltype text,
    issample integer
);


ALTER TABLE public.chatlist OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16400)
-- Name: chatlist_chatlistid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chatlist_chatlistid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chatlist_chatlistid_seq OWNER TO postgres;

--
-- TOC entry 3484 (class 0 OID 0)
-- Dependencies: 210
-- Name: chatlist_chatlistid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chatlist_chatlistid_seq OWNED BY public.chatlist.chatlistid;


--
-- TOC entry 235 (class 1259 OID 16581)
-- Name: contactus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contactus (
    contactusid integer NOT NULL,
    name text,
    job text,
    company text,
    email text,
    "SubmitTime" timestamp without time zone
);


ALTER TABLE public.contactus OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 16580)
-- Name: contactus_contactusid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contactus_contactusid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contactus_contactusid_seq OWNER TO postgres;

--
-- TOC entry 3485 (class 0 OID 0)
-- Dependencies: 234
-- Name: contactus_contactusid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contactus_contactusid_seq OWNED BY public.contactus.contactusid;


--
-- TOC entry 228 (class 1259 OID 16520)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16519)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 3486 (class 0 OID 0)
-- Dependencies: 227
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 214 (class 1259 OID 16413)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16412)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 3487 (class 0 OID 0)
-- Dependencies: 213
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 212 (class 1259 OID 16404)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16403)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 3488 (class 0 OID 0)
-- Dependencies: 211
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 229 (class 1259 OID 16549)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 3239 (class 2604 OID 16565)
-- Name: UserFirstLogin UserLoginID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UserFirstLogin" ALTER COLUMN "UserLoginID" SET DEFAULT nextval('public."UserFirstLogin_UserLoginID_seq"'::regclass);


--
-- TOC entry 3240 (class 2604 OID 16575)
-- Name: UserLogin UserLoginID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UserLogin" ALTER COLUMN "UserLoginID" SET DEFAULT nextval('public."UserLogin_UserLoginID_seq"'::regclass);


--
-- TOC entry 3232 (class 2604 OID 16432)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 3233 (class 2604 OID 16441)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 3231 (class 2604 OID 16425)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 3234 (class 2604 OID 16448)
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- TOC entry 3235 (class 2604 OID 16457)
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- TOC entry 3236 (class 2604 OID 16464)
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 3228 (class 2604 OID 16401)
-- Name: chatlist chatlistid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chatlist ALTER COLUMN chatlistid SET DEFAULT nextval('public.chatlist_chatlistid_seq'::regclass);


--
-- TOC entry 3241 (class 2604 OID 16584)
-- Name: contactus contactusid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactus ALTER COLUMN contactusid SET DEFAULT nextval('public.contactus_contactusid_seq'::regclass);


--
-- TOC entry 3237 (class 2604 OID 16523)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 3230 (class 2604 OID 16416)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 3229 (class 2604 OID 16407)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 3465 (class 0 OID 16562)
-- Dependencies: 231
-- Data for Name: UserFirstLogin; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."UserFirstLogin" ("UserLoginID", "Username", "Password", "LastLogin") VALUES (1, 'userhero', 'b''SmFrYXJ0YTIwMjlh', NULL);


--
-- TOC entry 3467 (class 0 OID 16572)
-- Dependencies: 233
-- Data for Name: UserLogin; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."UserLogin" ("UserLoginID", "Username", "Password", "LastLogin") VALUES (1, 'preparer', 'b''SmFrYXJ0YTIwMjIh''', '2022-09-27 03:29:40');


--
-- TOC entry 3452 (class 0 OID 16429)
-- Dependencies: 218
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3454 (class 0 OID 16438)
-- Dependencies: 220
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3450 (class 0 OID 16422)
-- Dependencies: 216
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add auth group', 7, 'add_authgroup');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change auth group', 7, 'change_authgroup');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete auth group', 7, 'delete_authgroup');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view auth group', 7, 'view_authgroup');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add auth group permissions', 8, 'add_authgrouppermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change auth group permissions', 8, 'change_authgrouppermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete auth group permissions', 8, 'delete_authgrouppermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view auth group permissions', 8, 'view_authgrouppermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add auth permission', 9, 'add_authpermission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change auth permission', 9, 'change_authpermission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete auth permission', 9, 'delete_authpermission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view auth permission', 9, 'view_authpermission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add auth user', 10, 'add_authuser');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change auth user', 10, 'change_authuser');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete auth user', 10, 'delete_authuser');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view auth user', 10, 'view_authuser');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add auth user groups', 11, 'add_authusergroups');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change auth user groups', 11, 'change_authusergroups');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete auth user groups', 11, 'delete_authusergroups');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view auth user groups', 11, 'view_authusergroups');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can add auth user user permissions', 12, 'add_authuseruserpermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can change auth user user permissions', 12, 'change_authuseruserpermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can delete auth user user permissions', 12, 'delete_authuseruserpermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can view auth user user permissions', 12, 'view_authuseruserpermissions');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can add chatlist', 13, 'add_chatlist');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can change chatlist', 13, 'change_chatlist');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can delete chatlist', 13, 'delete_chatlist');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can view chatlist', 13, 'view_chatlist');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can add django admin log', 14, 'add_djangoadminlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can change django admin log', 14, 'change_djangoadminlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can delete django admin log', 14, 'delete_djangoadminlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can view django admin log', 14, 'view_djangoadminlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (57, 'Can add django content type', 15, 'add_djangocontenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (58, 'Can change django content type', 15, 'change_djangocontenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (59, 'Can delete django content type', 15, 'delete_djangocontenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (60, 'Can view django content type', 15, 'view_djangocontenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (61, 'Can add django migrations', 16, 'add_djangomigrations');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (62, 'Can change django migrations', 16, 'change_djangomigrations');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (63, 'Can delete django migrations', 16, 'delete_djangomigrations');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (64, 'Can view django migrations', 16, 'view_djangomigrations');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (65, 'Can add django session', 17, 'add_djangosession');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (66, 'Can change django session', 17, 'change_djangosession');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (67, 'Can delete django session', 17, 'delete_djangosession');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (68, 'Can view django session', 17, 'view_djangosession');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (69, 'Can add contactus', 18, 'add_contactus');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (70, 'Can change contactus', 18, 'change_contactus');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (71, 'Can delete contactus', 18, 'delete_contactus');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (72, 'Can view contactus', 18, 'view_contactus');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (73, 'Can add user first login', 19, 'add_userfirstlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (74, 'Can change user first login', 19, 'change_userfirstlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (75, 'Can delete user first login', 19, 'delete_userfirstlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (76, 'Can view user first login', 19, 'view_userfirstlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (77, 'Can add userlogin', 20, 'add_userlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (78, 'Can change userlogin', 20, 'change_userlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (79, 'Can delete userlogin', 20, 'delete_userlogin');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (80, 'Can view userlogin', 20, 'view_userlogin');


--
-- TOC entry 3456 (class 0 OID 16445)
-- Dependencies: 222
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3458 (class 0 OID 16454)
-- Dependencies: 224
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3460 (class 0 OID 16461)
-- Dependencies: 226
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3443 (class 0 OID 16395)
-- Dependencies: 209
-- Data for Name: chatlist; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (89, '9_2', 'The sample data contains transactions made by credit cards, which consist 1 target variable (class), and three input variables (the transaction amount, credit limit, and income of each credit card holder) that has been transformed to protect sensitive features. Based on the input variables, it is possible to classify and predict whether a transaction is fraudulent (class = 1) or not (class = 0)', 1, '5_2', 1, 1, 0, 0, 'Probability', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (88, '9_1', 'The sample data consists of three variables or inputs i.e. coal price, USD/IDR forex rate, and oil price from November 2012 to September 2021 on monthly measurement. With this data it is possible to explore the relationship between the variables and predict or forecast the unknown coal price given certain known value of USD/IDR forex rate and oil price for a number of period.', 1, '5_1', 1, 1, 0, 0, 'Regression', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (90, '9_3', 'The sample data consists of three variables or inputs i.e. coal price, USD/IDR forex rate, and oil price from November 2012 to September 2021 on monthly measurement. With this data it is possible to explore the relationship between the variables and predict or forecast the unknown coal price given certain known value of USD/IDR forex rate and oil price for a number of period.', 1, '5_3', 1, 1, 0, 0, 'Regression', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (92, '9_5', 'The sample contains data of a mall’s customer which consists of customer age of the customer, annual income of the customer in thousands of dollar, and spending score assigned by the mall to the customer behaviour and spending nature. With this data, it is possible to group the customers and it can be used to aid growing businesses and check the development of the market.', 1, '5_5', 1, 1, 0, 0, 'Cluster', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (1, '1', 'Hello, welcome to <b> Machine Learning Engine</b>. What would you like to do today?', 1, '0', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (2, '1_1', 'Predict something with my existing data', 0, '0', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (3, '1_2', 'See trend/cluster from my data', 0, '0', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (4, '2_1', 'Would you like to know more of the concept on prediction?', 1, '1_1', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (112, '10_1', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_9', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (113, '10_2', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_11', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (114, '10_3', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_13', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (115, '10_4', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_15', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (116, '10_5', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_17', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (117, '10_6', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_19', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (118, '10_7', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_21', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (119, '10_8', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '9_23', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (120, '11_1', 'Here''s the result of your project', 1, '10_1', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (121, '11_2', 'Would you like to restart another project?', 1, '10_1', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (122, '11_3', 'Yes', 0, '10_1', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (123, '11_4', 'No', 0, '10_1', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (124, '11_5', 'Here''s the result of your project', 1, '10_2', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (125, '11_6', 'Would you like to restart another project?', 1, '10_2', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (126, '11_7', 'Yes', 0, '10_2', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (127, '11_8', 'No', 0, '10_2', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (128, '11_9', 'Here''s the result of your project', 1, '10_3', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (129, '11_10', 'Would you like to restart another project?', 1, '10_3', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (130, '11_11', 'Yes', 0, '10_3', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (131, '11_12', 'No', 0, '10_3', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (132, '11_13', 'Here''s the result of your project', 1, '10_4', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (133, '11_14', 'Would you like to restart another project?', 1, '10_4', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (134, '11_15', 'Yes', 0, '10_4', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (135, '11_16', 'No', 0, '10_4', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (136, '11_17', 'Here''s the result of your project', 1, '10_5', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (137, '11_18', 'Would you like to restart another project?', 1, '10_5', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (138, '11_19', 'Yes', 0, '10_5', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (139, '11_20', 'No', 0, '10_5', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (140, '11_21', 'Here''s the result of your project', 1, '10_6', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (141, '11_22', 'Would you like to restart another project?', 1, '10_6', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (142, '11_23', 'Yes', 0, '10_6', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (143, '11_24', 'No', 0, '10_6', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (144, '11_25', 'Here''s the result of your project', 1, '10_7', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (34, '5_3', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_6', 1, 1, 0, 1, 'Regression', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (145, '11_26', 'Would you like to restart another project?', 1, '10_7', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (146, '11_27', 'Yes', 0, '10_7', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (147, '11_28', 'No', 0, '10_7', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (35, '5_4', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_7', 1, 1, 0, 1, 'Probability', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (36, '5_5', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_10', 1, 1, 0, 1, 'Cluster', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (37, '5_6', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_11', 1, 1, 0, 1, 'Trend', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (38, '5_7', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_14', 1, 1, 0, 1, 'Cluster', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (39, '5_8', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_15', 1, 1, 0, 1, 'Trend', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (40, '6_1', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_1', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (41, '6_2', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_2', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (61, '7_14', 'Would you like to restart another project?', 1, '6_4', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (62, '7_15', 'Yes', 0, '6_4', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (63, '7_16', 'No', 0, '6_4', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (65, '7_18', 'Would you like to restart another project?', 1, '6_5', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (66, '7_19', 'Yes', 0, '6_5', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (67, '7_20', 'No', 0, '6_5', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (148, '11_29', 'Here''s the result of your project', 1, '10_8', 1, 1, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (149, '11_30', 'Would you like to restart another project?', 1, '10_8', 1, 2, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (150, '11_31', 'Yes', 0, '10_8', 1, 3, 1, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (151, '11_32', 'No', 0, '10_8', 1, 4, 0, 0, '', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (97, '9_10', 'I would like to use my own data', 0, '5_1', 1, 3, 1, 0, 'Regression', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (99, '9_12', 'I would like to use my own data', 0, '5_2', 1, 3, 1, 0, 'Probability', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (101, '9_14', 'I would like to use my own data', 0, '5_3', 1, 3, 1, 0, 'Regression', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (103, '9_16', 'I would like to use my own data', 0, '5_4', 1, 3, 1, 0, 'Probability', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (105, '9_18', 'I would like to use my own data', 0, '5_5', 1, 3, 1, 0, 'Cluster', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (107, '9_20', 'I would like to use my own data', 0, '5_6', 1, 3, 1, 0, 'Trend', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (109, '9_22', 'I would like to use my own data', 0, '5_7', 1, 3, 1, 0, 'Cluster', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (111, '9_24', 'I would like to use my own data', 0, '5_8', 1, 3, 1, 0, 'Trend', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (96, '9_9', 'Ok let''s use the sample data', 0, '5_1', 1, 2, 0, 0, 'Regression', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (98, '9_11', 'Ok let''s use the sample data', 0, '5_2', 1, 2, 0, 0, 'Probability', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (100, '9_13', 'Ok let''s use the sample data', 0, '5_3', 1, 2, 0, 0, 'Regression', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (102, '9_15', 'Ok let''s use the sample data', 0, '5_4', 1, 2, 0, 0, 'Probability', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (104, '9_17', 'Ok let''s use the sample data', 0, '5_5', 1, 2, 0, 0, 'Cluster', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (106, '9_19', 'Ok let''s use the sample data', 0, '5_6', 1, 2, 0, 0, 'Trend', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (5, '2_2', 'Yes, please!', 0, '1_1', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (6, '2_3', 'No, I''m cool with the concept!', 0, '1_1', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (8, '3_2', 'This is exactly what I need, let''s go!', 0, '2_2', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (9, '3_3', 'I changed my mind, go back to previous.', 0, '2_2', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (10, '4_1', 'Okay, tell me more on your project.', 1, '2_3', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (11, '4_2', 'I would like to predict the value for a number of period/data points', 0, '2_3', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (108, '9_21', 'Ok let''s use the sample data', 0, '5_7', 1, 2, 0, 0, 'Cluster', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (12, '4_3', 'I would like to predict the probability of the next value as the expected value', 0, '2_3', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (13, '4_4', 'Go back to previous', 0, '2_3', 1, 4, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (14, '4_5', 'Okay, tell me more on your project.', 1, '3_2', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (15, '4_6', 'I would like to predict the value for a number of period/data points', 0, '3_2', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (16, '4_7', 'I would like to predict the probability of the next value as the expected value', 0, '3_2', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (17, '4_8', 'Go back to previous', 0, '3_2', 1, 4, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (18, '2_4', 'Would you like to know more of the concept on clustering?', 1, '1_2', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (19, '2_5', 'Yes, please!', 0, '1_2', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (20, '2_6', 'No, I''m cool with the concept!', 0, '1_2', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (22, '3_5', 'This is exactly what I need, let''s go!', 0, '2_5', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (23, '3_6', 'I changed my mind, go back to previous.', 0, '2_5', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (24, '4_9', 'Okay, tell me more on your project.', 1, '2_6', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (25, '4_10', 'I''m interested to see clusters/groups in my data', 0, '2_6', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (26, '4_11', 'I''m interested to see trends in my data', 0, '2_6', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (27, '4_12', 'Go back to previous', 0, '2_6', 1, 4, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (28, '4_13', 'Okay, tell me more on your project.', 1, '3_5', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (29, '4_14', 'I''m interested to see clusters/groups in my data', 0, '3_5', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (30, '4_15', 'I''m interested to see trends in my data', 0, '3_5', 1, 3, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (31, '4_16', 'Go back to previous', 0, '3_5', 1, 4, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (32, '5_1', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_2', 1, 1, 0, 1, 'Regression', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (33, '5_2', 'Please upload your data according to the following format (.xlsx or .csv)', 1, '4_3', 1, 1, 0, 1, 'Probability', 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (42, '6_3', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_3', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (43, '6_4', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_4', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (44, '6_5', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_5', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (45, '6_6', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_6', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (46, '6_7', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_7', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (47, '6_8', 'Analysing your data with our cool built-in machine learning algorithms, please wait...', 1, '5_8', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (49, '7_2', 'Would you like to restart another project?', 1, '6_1', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (50, '7_3', 'Yes', 0, '6_1', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (51, '7_4', 'No', 0, '6_1', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (53, '7_6', 'Would you like to restart another project?', 1, '6_2', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (54, '7_7', 'Yes', 0, '6_2', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (55, '7_8', 'No', 0, '6_2', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (57, '7_10', 'Would you like to restart another project?', 1, '6_3', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (58, '7_11', 'Yes', 0, '6_3', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (59, '7_12', 'No', 0, '6_3', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (21, '3_4', 'Clustering in the field of data science is often referred as <b>unsupervised machine learning</b>.</br></br>In unsupervised machine learning, a program looks for patterns in unlabeled data. Unsupervised machine learning can find patterns or trends that people aren’t explicitly looking for. For example, an unsupervised machine learning program could look through online sales data and identify different types of clients making purchases.</br></br>Example use cases include:</br>Customer segmentation, product mix/cluster, anomaly detection', 1, '2_5', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (48, '7_1', 'Here''s the result of your project', 1, '6_1', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (52, '7_5', 'Here''s the result of your project', 1, '6_2', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (56, '7_9', 'Here''s the result of your project', 1, '6_3', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (60, '7_13', 'Here''s the result of your project', 1, '6_4', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (69, '7_22', 'Would you like to restart another project?', 1, '6_6', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (70, '7_23', 'Yes', 0, '6_6', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (71, '7_24', 'No', 0, '6_6', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (73, '7_26', 'Would you like to restart another project?', 1, '6_7', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (74, '7_27', 'Yes', 0, '6_7', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (75, '7_28', 'No', 0, '6_7', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (77, '7_30', 'Would you like to restart another project?', 1, '6_8', 1, 2, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (78, '7_31', 'Yes', 0, '6_8', 1, 3, 1, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (79, '7_32', 'No', 0, '6_8', 1, 4, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (80, '8_1', 'Thank you for using Machine Learning Engine.', 1, '7_4', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (81, '8_2', 'Thank you for using Machine Learning Engine.', 1, '7_8', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (82, '8_3', 'Thank you for using Machine Learning Engine.', 1, '7_12', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (83, '8_4', 'Thank you for using Machine Learning Engine.', 1, '7_16', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (84, '8_5', 'Thank you for using Machine Learning Engine.', 1, '7_20', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (85, '8_6', 'Thank you for using Machine Learning Engine.', 1, '7_24', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (86, '8_7', 'Thank you for using Machine Learning Engine.', 1, '7_28', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (87, '8_8', 'Thank you for using Machine Learning Engine.', 1, '7_32', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (7, '3_1', 'Prediction or forecasting in the field of data science is often referred as <b>supervised machine learning</b>.</br></br>Supervised machine learning models are trained with labeled data sets, which allow the models to learn and grow more accurate over time. For example, an algorithm would be trained with pictures of dogs and other things, all labeled by humans, and the machine would learn ways to identify pictures of dogs on its own.</br></br>Supervised model typically can be further categorised into:</br>1. Regression/forecasting, predict a continuous outcome (y) based on the value of one or more predictor variables (x).</br>Example use cases of regression/forecasting include:</br>price prediction, GDP prediction, price elasticity, demand forecast</br></br>2. Classification, a predictive modeling problem where a class label is predicted for a given example of input data. </br>Example use cases of classification include:</br>Given certain transaction, classify if it is fraud/non-fraud, identify anomaly transaction, predict customer churn, staff retention, predict credit rating/worthiness', 1, '2_2', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (64, '7_17', 'Here''s the result of your project', 1, '6_5', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (68, '7_21', 'Here''s the result of your project', 1, '6_6', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (72, '7_25', 'Here''s the result of your project', 1, '6_7', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (76, '7_29', 'Here''s the result of your project', 1, '6_8', 1, 1, 0, 0, NULL, 0);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (91, '9_4', 'The sample data contains transactions made by credit cards, which consist 1 target variable (class), and three input variables (the transaction amount, credit limit, and income of each credit card holder) that has been transformed to protect sensitive features. Based on the input variables, it is possible to classify and predict whether a transaction is fraudulent (class = 1) or not (class = 0)', 1, '5_4', 1, 1, 0, 0, 'Probability', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (93, '9_6', 'The sample contains data of a mall’s customer which consists of customer age of the customer, annual income of the customer in thousands of dollar, and spending score assigned by the mall to the customer behaviour and spending nature. With this data and the visualization result, it is possible to analyse the target market. For example, it can be used to analyse which range of age will be the target market for the new business development.', 1, '5_6', 1, 1, 0, 0, 'Trend', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (94, '9_7', 'The sample contains data of a mall’s customer which consists of customer age of the customer, annual income of the customer in thousands of dollar, and spending score assigned by the mall to the customer behaviour and spending nature. With this data, it is possible to group the customers and it can be used to aid growing businesses and check the development of the market.', 1, '5_7', 1, 1, 0, 0, 'Cluster', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (95, '9_8', 'The sample contains data of a mall’s customer which consists of customer age of the customer, annual income of the customer in thousands of dollar, and spending score assigned by the mall to the customer behaviour and spending nature. With this data and the visualization result, it is possible to analyse the target market. For example, it can be used to analyse which range of age will be the target market for the new business development.', 1, '5_8', 1, 1, 0, 0, 'Trend', 1);
INSERT INTO public.chatlist (chatlistid, chatlistcode, description, isquestion, parentchatcode, status, "Order", isreset, isupload, mltype, issample) VALUES (110, '9_23', 'Ok let''s use the sample data', 0, '5_8', 1, 2, 0, 0, 'Trend', 1);


--
-- TOC entry 3469 (class 0 OID 16581)
-- Dependencies: 235
-- Data for Name: contactus; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.contactus (contactusid, name, job, company, email, "SubmitTime") VALUES (1, '', '', '', '', '2022-09-26 05:40:33');
INSERT INTO public.contactus (contactusid, name, job, company, email, "SubmitTime") VALUES (2, 'TestInsert', 'TestInsert', 'TestInsert', 'TestInsert@mail.com', '2022-09-27 09:55:06');


--
-- TOC entry 3462 (class 0 OID 16520)
-- Dependencies: 228
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3448 (class 0 OID 16413)
-- Dependencies: 214
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'FirstApp', 'authgroup');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'FirstApp', 'authgrouppermissions');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'FirstApp', 'authpermission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'FirstApp', 'authuser');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'FirstApp', 'authusergroups');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'FirstApp', 'authuseruserpermissions');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'FirstApp', 'chatlist');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'FirstApp', 'djangoadminlog');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (15, 'FirstApp', 'djangocontenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (16, 'FirstApp', 'djangomigrations');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (17, 'FirstApp', 'djangosession');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (18, 'FirstApp', 'contactus');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (19, 'FirstApp', 'userfirstlogin');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (20, 'FirstApp', 'userlogin');


--
-- TOC entry 3446 (class 0 OID 16404)
-- Dependencies: 212
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'FirstApp', '0001_initial', '2022-09-23 05:31:51.11695+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'FirstApp', '0002_sqlitestudiotemptable', '2022-09-23 05:31:51.126949+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'FirstApp', '0003_auto_20220330_0857', '2022-09-23 05:31:51.133954+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'FirstApp', '0004_contactus_userfirstlogin_userlogin', '2022-09-23 05:31:51.144955+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'contenttypes', '0001_initial', '2022-09-23 05:31:51.168946+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'auth', '0001_initial', '2022-09-23 05:31:51.407957+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'admin', '0001_initial', '2022-09-23 05:31:51.463959+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'admin', '0002_logentry_remove_auto_add', '2022-09-23 05:31:51.474963+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'admin', '0003_logentry_add_action_flag_choices', '2022-09-23 05:31:51.487952+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'contenttypes', '0002_remove_content_type_name', '2022-09-23 05:31:51.514952+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0002_alter_permission_name_max_length', '2022-09-23 05:31:51.527962+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0003_alter_user_email_max_length', '2022-09-23 05:31:51.53895+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0004_alter_user_username_opts', '2022-09-23 05:31:51.551951+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0005_alter_user_last_login_null', '2022-09-23 05:31:51.56295+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'auth', '0006_require_contenttypes_0002', '2022-09-23 05:31:51.567951+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'auth', '0007_alter_validators_add_error_messages', '2022-09-23 05:31:51.580953+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'auth', '0008_alter_user_username_max_length', '2022-09-23 05:31:51.600951+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'auth', '0009_alter_user_last_name_max_length', '2022-09-23 05:31:51.612953+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'auth', '0010_alter_group_name_max_length', '2022-09-23 05:31:51.626955+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'auth', '0011_update_proxy_permissions', '2022-09-23 05:31:51.643954+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'auth', '0012_alter_user_first_name_max_length', '2022-09-23 05:31:51.654955+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'sessions', '0001_initial', '2022-09-23 05:31:51.692952+00');


--
-- TOC entry 3463 (class 0 OID 16549)
-- Dependencies: 229
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('z76ig257ubkqqhmw7672u6tlebpw9eyh', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ol6FW:wgKS8jkLtbCiY8Pc4sKyETeRJA7jSYGkYmSxlJlzWDI', '2022-11-02 10:24:34.97907+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('f0d7si4q3b94308t3qu8n508ukdrsapz', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ofHWC:-6sb_TWv_zBSAQ0NkzndgvVx4gLrdAKH40OeA2EX8Ts', '2022-10-17 09:13:44.125438+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('rw8r07cmsm8qa11pppzaktn4vsredvhr', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyJ9:1obbgB:Ucu9QAjXDKxuo6JdC0W0nsti_MCAQiCrz4EfC9IH8fs', '2022-10-07 05:56:51.809469+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('76f3aco6pcc95d7ak55pb1hho6uttm93', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyJ9:1obd8C:EKpSqCISRPf2Nw_Vp1vHx6IEIS4vM0RZCEsv6fj1knI', '2022-10-07 07:29:52.281645+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('duaoel70kfebhkgttvij3jtrxj7h0udf', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyJ9:1od12e:zCl-TaLLIaewKX7Rlyz16UtYquQXKoRuvU_TPbJ2WmE', '2022-10-11 03:13:52.339645+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('8ye3wre2jodb5nusfcvxt5db6amdzpvm', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1osd1B:A3cBo8SVgyM3nOmPlmsPmvzRPeyrwMPxAImv15Xgqzk', '2022-11-23 04:48:53.962433+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('eep9k8hpvvqdq0olzal4zpir0a6c1hze', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIl9zZXNzaW9uX2V4cGlyeSI6MzAwMDAsIm5hbWUiOiJwcmVwYXJlciJ9:1od17x:N0Fh1WKAkTRKDOEb_SaJnTdO-a9XghTaUOBuI--z1RI', '2022-09-27 11:39:21.521482+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('5qw4x3jn5y9qnstbin46hht4dnnjee0o', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1oxJSf:kK3ckUDtcxBfeW95gPaTjj64u16WCUuz4jKs22EjzTE', '2022-12-06 02:56:37.169855+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('gn6cg6jbyzc8erp5z6756idfropmnamr', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1osd1X:_iIbE1g8kFT7NI_pVXBnvxSgpQ2l0ihTxRfzsunO1Kc', '2022-11-23 04:49:15.880354+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('ej7i68nb82e9dk5q2fsvbaz654uvch1m', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ofEcg:H61nlExF_6b-W9zmJZPUO1afjOKbZ7GpgcNSNjS1rio', '2022-10-17 06:08:14.313099+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('srqn9m2tnf8zdg97yuqhp8y4dt46dong', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1osd2T:o-qcLNCEqM36FTgUjZO_7QCy0z_D556vbgDcEv-Vs1w', '2022-11-23 04:50:13.786099+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('h6mur9rwply2lsrm5sf5ib27ep2ndlc0', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1osdhA:dYOdAuwm9Dgnf7YCjDYwsVvaBZ4gqxeudWffvEslo8s', '2022-11-23 05:32:16.256427+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('eddm10o13ha1ii1n5p4l7g749z8w7w3a', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciIsIl9zZXNzaW9uX2V4cGlyeSI6MzAwMDB9:1od7T7:KXJLQ-LCcDEff2K8OXBB14Z_H3H0hoWsK0imIQaI2GU', '2022-09-27 18:25:37.105181+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('fr8yxssz1w9qs5q8of7zjc745nqec0cp', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1odLgg:H9iNYqrp3IoKqotBn6TCSQt6J0FhTkC5L1GGmXBYz18', '2022-10-12 01:16:34.96237+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('o0rkn16ec5w53n2eiqd9zuje4jg1cgrb', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1oy65l:SlAWZzSgWZvCOjBmsX4drgBMlD1pKTTKj-PmTFP1Ius', '2022-12-08 06:52:13.715428+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('00114z0rzkyyo87emfpanf6jiwseus2v', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciIsIl9zZXNzaW9uX2V4cGlyeSI6MzAwMDB9:1od1AW:HktS8zVWGsr-5x7l6AHeM5DNI6cizp1yA_kd6FLHDJk', '2022-09-27 11:42:00.460813+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('lyu0nifqyh4v8wr0jeumo475r4qvn6em', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ozU9u:jDl2gBRHadKzKzuWTo3vHtKeKktX-8eLnomZ7UuVInw', '2022-12-12 02:46:14.895606+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('7x1ge88vgs4to6g4t30wiac0ayrrpwvx', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1osdwe:QGpFdfEea3DU9w6_zjs06fRsPHe50RH52ubeZla4Ars', '2022-11-23 05:48:16.808972+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('8635o1zbjkcyliifmj05u0lzd7bvob5p', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1odLhN:M5PkD20a0BMoQGVkIGTIlKBECK0qKCL8h72xOvVxJNE', '2022-10-12 01:17:17.156925+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('4pxqwh6m10u2sjzcjd6eo9wsqjvl7w13', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ohndm:HGplAy3IcoYweytKkg9X12hRww1UINnYDb7pWwXI7Dw', '2022-10-24 07:55:58.738343+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('kvq4zv2n17mk3c4ic54xwvoacl2b3qyv', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyJ9:1oixFQ:UtVUvTIMesxkC387s0Nalo9Z_ChQBMTkco_z3rmmqpc', '2022-10-27 12:23:36.126746+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('rkunvko5c6p1tmd9dbxi85hgvhb4xr5i', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ose3B:jQMRinKC4g5w0TqFnPYB7hIE0cyh_Jxu0DotLObk9hs', '2022-11-23 05:55:01.55064+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('23zeeggt2maymuubcy1gb8d40q2elvug', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ol69T:83nLJ7wInGdkAvKiGwrPMMDcfSSAInduoMThUZNWOb4', '2022-11-02 10:18:19.259043+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('tcuzrj2e6a9gf6nvnzqwb2q64i9ij3hl', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ofHH6:bKebXUNod5kmFDcQV-n5Qw0L3pF2iyhvGMgDW8u9mPs', '2022-10-17 08:58:08.088045+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('842pvhpebpkcxupppuplhrbtj4mgcz4i', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1ot2A4:D34W-2QtMH1f_vrrUOBOUNIf0LA3PJjeOPcMA4i9ffo', '2022-11-24 07:39:44.039612+00');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('stya6itxktaufchhrotu0cou22hq7f6w', 'eyJmaXJzdG5hbWUiOiJ1c2VyaGVybyIsIm5hbWUiOiJwcmVwYXJlciJ9:1otJss:onUEc6_KTcYUo0KF8zBK14chnQrOvebWRGeXaluxsZ0', '2022-11-25 02:35:10.891922+00');


--
-- TOC entry 3489 (class 0 OID 0)
-- Dependencies: 230
-- Name: UserFirstLogin_UserLoginID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."UserFirstLogin_UserLoginID_seq"', 1, true);


--
-- TOC entry 3490 (class 0 OID 0)
-- Dependencies: 232
-- Name: UserLogin_UserLoginID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."UserLogin_UserLoginID_seq"', 1, true);


--
-- TOC entry 3491 (class 0 OID 0)
-- Dependencies: 217
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3492 (class 0 OID 0)
-- Dependencies: 219
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3493 (class 0 OID 0)
-- Dependencies: 215
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 80, true);


--
-- TOC entry 3494 (class 0 OID 0)
-- Dependencies: 223
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 3495 (class 0 OID 0)
-- Dependencies: 221
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- TOC entry 3496 (class 0 OID 0)
-- Dependencies: 225
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3497 (class 0 OID 0)
-- Dependencies: 210
-- Name: chatlist_chatlistid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.chatlist_chatlistid_seq', 151, true);


--
-- TOC entry 3498 (class 0 OID 0)
-- Dependencies: 234
-- Name: contactus_contactusid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contactus_contactusid_seq', 2, true);


--
-- TOC entry 3499 (class 0 OID 0)
-- Dependencies: 227
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- TOC entry 3500 (class 0 OID 0)
-- Dependencies: 213
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 20, true);


--
-- TOC entry 3501 (class 0 OID 0)
-- Dependencies: 211
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- TOC entry 3290 (class 2606 OID 16569)
-- Name: UserFirstLogin UserFirstLogin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UserFirstLogin"
    ADD CONSTRAINT "UserFirstLogin_pkey" PRIMARY KEY ("UserLoginID");


--
-- TOC entry 3292 (class 2606 OID 16579)
-- Name: UserLogin UserLogin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UserLogin"
    ADD CONSTRAINT "UserLogin_pkey" PRIMARY KEY ("UserLoginID");


--
-- TOC entry 3255 (class 2606 OID 16547)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3260 (class 2606 OID 16477)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 3263 (class 2606 OID 16443)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3257 (class 2606 OID 16434)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3250 (class 2606 OID 16468)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3252 (class 2606 OID 16427)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3271 (class 2606 OID 16459)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3274 (class 2606 OID 16492)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 3265 (class 2606 OID 16450)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3277 (class 2606 OID 16466)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3280 (class 2606 OID 16506)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 3268 (class 2606 OID 16542)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3294 (class 2606 OID 16588)
-- Name: contactus contactus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contactus
    ADD CONSTRAINT contactus_pkey PRIMARY KEY (contactusid);


--
-- TOC entry 3283 (class 2606 OID 16528)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3245 (class 2606 OID 16420)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3247 (class 2606 OID 16418)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3243 (class 2606 OID 16411)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3287 (class 2606 OID 16555)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3253 (class 1259 OID 16548)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3258 (class 1259 OID 16488)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 3261 (class 1259 OID 16489)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3248 (class 1259 OID 16474)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 3269 (class 1259 OID 16504)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 3272 (class 1259 OID 16503)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 3275 (class 1259 OID 16518)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3278 (class 1259 OID 16517)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 3266 (class 1259 OID 16543)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3281 (class 1259 OID 16539)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3284 (class 1259 OID 16540)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3285 (class 1259 OID 16557)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3288 (class 1259 OID 16556)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3297 (class 2606 OID 16483)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3296 (class 2606 OID 16478)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3295 (class 2606 OID 16469)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3299 (class 2606 OID 16498)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3298 (class 2606 OID 16493)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3301 (class 2606 OID 16512)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3300 (class 2606 OID 16507)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3302 (class 2606 OID 16529)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3303 (class 2606 OID 16534)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2022-11-28 03:23:06

--
-- PostgreSQL database dump complete
--

