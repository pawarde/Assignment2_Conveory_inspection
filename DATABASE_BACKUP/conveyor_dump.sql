PGDMP                         |            conveyor %   12.20 (Ubuntu 12.20-0ubuntu0.20.04.1) %   12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16405    conveyor    DATABASE     n   CREATE DATABASE conveyor WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_IN' LC_CTYPE = 'en_IN';
    DROP DATABASE conveyor;
                postgres    false            �            1259    16408    process    TABLE     �   CREATE TABLE public.process (
    id integer NOT NULL,
    defect text,
    created_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.process;
       public         heap    postgres    false            �            1259    16406    process_id_seq    SEQUENCE     �   CREATE SEQUENCE public.process_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.process_id_seq;
       public          postgres    false    203            �           0    0    process_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.process_id_seq OWNED BY public.process.id;
          public          postgres    false    202                       2604    16411 
   process id    DEFAULT     h   ALTER TABLE ONLY public.process ALTER COLUMN id SET DEFAULT nextval('public.process_id_seq'::regclass);
 9   ALTER TABLE public.process ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    202    203    203            �          0    16408    process 
   TABLE DATA           ;   COPY public.process (id, defect, created_time) FROM stdin;
    public          postgres    false    203   �
       �           0    0    process_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.process_id_seq', 154, true);
          public          postgres    false    202                       2606    16417    process process_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.process
    ADD CONSTRAINT process_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.process DROP CONSTRAINT process_pkey;
       public            postgres    false    203            �   1  x�}��]5���)�����t!QRP� H<>��Bwҏl���ݙ#~��׿�����߿���>�s���Oz>�|�󍭢^������'�,��^J�KM�-c���JjG�ͻ�Jzk��^�$zv/�RT"[]�}�7$y���r��QÑ���-����ec�%���.���"V�ąu(ch"�B!���ėpʾO>	���✡�L]�c�ݍ]�S�mr��/�\ x[��\�[�Ⱥ�2Jp6[�B��-�Z�B6�~������{m>�B6�)�硐ͷ��,���i�r����o,��-��c�l�{��(f�}�׮�s�pV������oJ9�l<Qm�C9C���PΣi4'_F9��%���(gש�\����u�>�����s~ipYm��=������=gh��N�P����hd�q����G�o�04{�y4
>��y�s���n7����U���7�9�4�sf&Q��[���r��唳�������sNԘ��s�9�u{9ǜ軍�rN�v���rN�����R�g��adS�Иa+�C)_���&��R�ϸu���;�0GC)_T&�|P��O�ǭ��r�	2|(��4},�JιQ=���b��т�Е�8؈��3�����(fhʎb$����XI1�<��.+)f�xK_I1C����VṚ�epYE1c��\Y�97��]WQ���E8?�XOJ�:�#�/�FΏ&\�^��c�3�.�"�����GE8?���������D�\Ώ�U�i�M8�4>&�p~4ٷ0��r�:�J�:��ԡ�t_M9�~�b&�j�k4�^�9���c6��~�|8g�u��Q=NK'��L�׌��D�0�
eÊr�g;
�&ZŅS�Ci��hY���6ۧa�Dy����lG�C��1(qX�Rt4!��O��ņQ�0�G=�$GJ�'Eh?�QⰜi���D�?~�O[H2|�0̤FD���ᾈ�l8"߸��G���y�	+$�D��&a�|�U����9q<4�;+q��Hdp<B2���z� �Y��i(x1����M�2$'�D���|'$(�hzA�B��D��=@�"D�:��HV|����D�y� "�kzLq��_"E�?�%QT��ZH`ѝ��8Ib|�z~8��G�V��َ�spN\Ǌ?�Ij�r�  ���YQt,7��G=�����sB���X�7 +U��9�x�P�v�x�?�I��c�O�I�3�8q�����3q�h��O�e�����7#�CD�#̣0"J��q_Q��%SO,C��}�2c���Z�,Kk     