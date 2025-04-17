# -*- coding: utf-8 -*-
import pygame
import random
import math

# --- Konstanta ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
DARK_RED = (150, 0, 0)
GREY = (128, 128, 128)
GOLD = (255, 215, 0) # Shield Upgrade
LIGHT_BLUE = (173, 216, 230) # Slow Field
DARK_GREY = (100, 100, 100) # Piercing Rounds
# BARU: Warna Item Baru
ELECTRIC_BLUE = (0, 128, 255) # EMP Burst
BRIGHT_RED = (255, 60, 60) # Rapid Fire
GREENISH_YELLOW = (173, 255, 47) # Scrambler

COMMANDER_COLOR = PURPLE

PLAYER_COLOR = (200, 200, 255)
ENEMY_COLOR = (255, 50, 50)
DASHER_COLOR = CYAN
MINELAYER_COLOR = (200, 100, 255)
MINE_COLOR = DARK_RED
POWERUP_AMMO_COLOR = GREEN
POWERUP_SPREAD_COLOR = CYAN
POWERUP_SHIELD_COLOR = YELLOW
POWERUP_OPTION_COLOR = PURPLE
POWERUP_BOMB_COLOR = ORANGE
POWERUP_SHIELD_UPGRADE_COLOR = GOLD
POWERUP_PIERCING_COLOR = DARK_GREY
POWERUP_SLOWFIELD_COLOR = LIGHT_BLUE
# BARU: Warna Powerup Baru
POWERUP_EMP_COLOR = ELECTRIC_BLUE
POWERUP_RAPIDFIRE_COLOR = BRIGHT_RED
POWERUP_SCRAMBLER_COLOR = GREENISH_YELLOW


BOSS_COLOR = (200, 0, 200)
BOSS_BULLET_COLOR = ORANGE
HEALTH_BAR_BG = (50, 50, 50)
PLAYER_HEALTH_COLOR = GREEN
BOSS_HEALTH_COLOR = RED
PAUSE_OVERLAY_COLOR = (0, 0, 0, 150)
EXPLOSION_COLORS = [(255, 255, 0), (255, 165, 0), (255, 0, 0), (100, 100, 100)]
SHIELD_COLOR = (0, 200, 255, 100)
OPTION_COLOR = (220, 220, 220)
SLOW_FIELD_VISUAL_COLOR = (100, 150, 255, 60) # Warna visual slow field
EMP_VISUAL_COLOR = (0, 150, 255, 180) # Warna visual EMP

PLAYER_SPEED = 5
BULLET_SPEED = 7
# Konstanta dasar untuk penskalaan musuh
ENEMY_BULLET_SPEED_BASE = 4.5
ENEMY_SHOOT_DELAY_BASE = 1000
MIN_ENEMY_SHOOT_DELAY = 500
ENEMY_BULLET_SPEED_SCALE = 0.15
ENEMY_SHOOT_DELAY_SCALE = 40

ENEMY_MAX_RANDOM_X_SPEED = 1.8
ENEMY_SPEED_Y = 0.3
ENEMY_OSCILLATION_SPEED = 0.005
ENEMY_OSCILLATION_AMPLITUDE = 4
# Konstanta Dasher Enemy
DASHER_SPEED_Y = 0.6
DASHER_DASH_CHANCE = 0.01
DASHER_DASH_SPEED_X = 6
DASHER_DASH_DURATION = 450
# Konstanta Mine Layer Enemy
MINELAYER_SPEED_Y = 0.4
MINELAYER_DROP_DELAY = 1800
MINELAYER_DROP_MIN_Y = 50
MINES_ON_DEATH = 2
# Konstanta Mine
MINE_DURATION = 7000
MINE_SPEED_Y = 0.6
MINE_EXPLOSION_RADIUS = 40
# Konstanta Commander Enemy
COMMANDER_SPEED_Y = 0.25
COMMANDER_HEALTH = 4
COMMANDER_REINFORCEMENT_DELAY = 4500
COMMANDER_REINFORCEMENTS_COUNT = 1

MAX_ENEMIES_ON_SCREEN = 25

# Konstanta Power-Up
POWERUP_DROP_CHANCE = 0.16 # Naikkan lagi sedikit
POWERUP_SPEED = 3
MAX_WEAPON_LEVEL = 5
SPREAD_DURATION = 25000
PIERCING_DURATION = 15000
SLOWFIELD_DURATION = 12000
SCRAMBLER_DURATION = 10000
RAPID_FIRE_DURATION = 15000
RAPID_FIRE_DELAY = 50
EMP_RADIUS = 150
INITIAL_BOMBS = 1
INITIAL_EMP_CHARGES = 1
INITIAL_RAPIDFIRE_CHARGES = 1
AUTO_ITEMS_ON_BOSS_START = 2

SPREAD_ANGLE = 15
MAX_OPTIONS = 2

# Konstanta Boss
BOSS_WAVE_INTERVAL = 5
BOSS_HEALTH_INITIAL = 120
BOSS_HEALTH_INCREMENT = 60
PLAYER_BOSS_HEALTH = 10
# Konstanta Dasar & Batas untuk Boss Dinamis
BOSS_SPEED_X_BASE = 3.5
BOSS_SPEED_X_MAX = 5.0
BOSS_SHOOT_DELAY_BASE = 650
BOSS_SHOOT_DELAY_MIN = 400
BOSS_BULLET_SPEED_BASE = 6.0
BOSS_BULLET_SPEED_MAX = 8.0
BOSS_SPREAD_CHANCE_BASE = 0.25
BOSS_SPREAD_CHANCE_MAX = 0.50

BOSS_SPREAD_BULLETS = 7

# Konstanta Gameplay Baru
PLAYER_LIVES = 3
PLAYER_INVINCIBILITY_DURATION = 2000
PLAYER_BLINK_INTERVAL = 200
HIT_FLASH_DURATION = 60
# Konstanta Multiplier
MULTIPLIER_THRESHOLD = 5
MAX_MULTIPLIER = 5
# Konstanta Wave System
WAVE_TRANSITION_DELAY = 3500
# Konstanta Efek Bom & EMP
BOMB_FLASH_DURATION = 150
EMP_EFFECT_DURATION = 300 # Durasi visual EMP

# Konstanta Penskalaan Jumlah Musuh
ENEMY_COUNT_BASE = 8
ENEMY_COUNT_SCALE_PER_WAVE = 1.5
# Konstanta UI Beranda
TITLE_BLINK_INTERVAL = 550 # Interval kedip teks start (ms)

# Status game
TITLE_SCREEN = 0
PLAYING = 1
GAME_OVER = 2
BOSS_FIGHT = 3
PAUSED = 4
WAVE_TRANSITION = 5

# --- Kelas Player ---
# (Tidak ada perubahan di kelas Player)
class Player(pygame.sprite.Sprite):
    """ Merepresentasikan kapal pemain dengan nyawa, respawn, perisai, option, bom, dan status efek baru """
    def __init__(self):
        super().__init__()
        self.original_image = pygame.Surface([40, 40], pygame.SRCALPHA)
        points = [(20, 0), (40, 32), (28, 32), (28, 40), (12, 40), (12, 32), (0, 32)]
        pygame.draw.polygon(self.original_image, PLAYER_COLOR, points)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(); self.rect.centerx = SCREEN_WIDTH // 2; self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0; self.last_shot_time = 0; self.shoot_delay = 250
        self.weapon_level = 1
        self.lives = PLAYER_LIVES; self.hidden = False; self.hide_timer = pygame.time.get_ticks()
        self.invincible = False; self.invincible_timer = pygame.time.get_ticks()
        self.current_boss_health = PLAYER_BOSS_HEALTH
        self.options = pygame.sprite.Group()
        self.max_options = MAX_OPTIONS

        # Item Aktif & Charges
        self.bomb_count = INITIAL_BOMBS
        self.emp_charges = INITIAL_EMP_CHARGES # BARU
        self.rapid_fire_charges = INITIAL_RAPIDFIRE_CHARGES # BARU

        # Status Efek Visual/Temporer
        self.bomb_flash_active = False; self.bomb_flash_timer = 0
        self.emp_effect_active = False; self.emp_effect_timer = 0; self.emp_effect_radius = 0 # BARU
        self.rapid_fire_active = False; self.rapid_fire_end_time = 0 # BARU
        self.spread_active = False; self.spread_end_time = 0
        self.piercing_rounds_active = False; self.piercing_rounds_end_time = 0
        self.slow_field_active = False; self.slow_field_end_time = 0
        self.scrambler_active = False; self.scrambler_end_time = 0 # BARU

        # Status Perisai
        self.shield_active = False
        self.shield_upgrade_ready = False
        self.current_shield_reflects = False


    def update(self):
        """ Memperbarui posisi, status efek, respawn, perisai, option """
        now = pygame.time.get_ticks()
        if self.hidden:
             if now - self.hide_timer > 1000: self.unhide()
             return

        # Update & Nonaktifkan Efek Temporer
        if self.bomb_flash_active and now > self.bomb_flash_timer: self.bomb_flash_active = False
        if self.emp_effect_active and now > self.emp_effect_timer: self.emp_effect_active = False # BARU
        if self.spread_active and now > self.spread_end_time: self.deactivate_spread()
        if self.piercing_rounds_active and now > self.piercing_rounds_end_time: self.deactivate_piercing()
        if self.slow_field_active and now > self.slow_field_end_time: self.deactivate_slow_field()
        if self.scrambler_active and now > self.scrambler_end_time: self.deactivate_scrambler() # BARU
        if self.rapid_fire_active and now > self.rapid_fire_end_time: self.deactivate_rapid_fire() # BARU

        # Update Invincibility & Blinking
        if self.invincible and now > self.invincible_timer:
            self.invincible = False; self.image = self.original_image.copy(); self.image.set_alpha(255)
        show_normal = True
        if self.invincible:
            show_normal = (now // PLAYER_BLINK_INTERVAL) % 2 == 0
            self.image.set_alpha(255 if show_normal else 0)

        # Pergerakan Pemain
        self.speed_x = 0; keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]: self.speed_x = -PLAYER_SPEED
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]: self.speed_x = PLAYER_SPEED
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0: self.rect.left = 0

        # Update Posisi Option
        self.update_options()

    def update_options(self):
        """ Mengatur posisi option agar mengikuti pemain """
        option_list = self.options.sprites()
        num_options = len(option_list)
        if num_options == 1:
            target_x = self.rect.centerx - 40
            target_y = self.rect.centery + 20
            option_list[0].set_target(target_x, target_y)
        elif num_options >= 2:
            target_x_left = self.rect.centerx - 40
            target_x_right = self.rect.centerx + 40
            target_y = self.rect.centery + 20
            option_list[0].set_target(target_x_left, target_y)
            option_list[1].set_target(target_x_right, target_y)
        self.options.update()

    def draw_shield(self, surface):
        """ Menggambar perisai jika aktif (bisa reflektif atau normal) """
        if self.shield_active and not self.invincible and not self.hidden:
             shield_surf = pygame.Surface((self.rect.width + 10, self.rect.height + 10), pygame.SRCALPHA)
             color_to_draw = GOLD if self.current_shield_reflects else SHIELD_COLOR
             pygame.draw.circle(shield_surf, color_to_draw, shield_surf.get_rect().center, self.rect.width // 2 + 5)
             surface.blit(shield_surf, (self.rect.centerx - shield_surf.get_width()//2, self.rect.centery - shield_surf.get_height()//2))

    def draw_slow_field(self, surface):
        """ Menggambar lingkaran visual untuk slow field jika aktif """
        if self.slow_field_active and not self.hidden:
            field_surf = pygame.Surface((SLOW_FIELD_RADIUS * 2, SLOW_FIELD_RADIUS * 2), pygame.SRCALPHA)
            pygame.draw.circle(field_surf, SLOW_FIELD_VISUAL_COLOR, (SLOW_FIELD_RADIUS, SLOW_FIELD_RADIUS), SLOW_FIELD_RADIUS)
            surface.blit(field_surf, (self.rect.centerx - SLOW_FIELD_RADIUS, self.rect.centery - SLOW_FIELD_RADIUS))

    # BARU: Fungsi untuk menggambar efek visual aktif (EMP, Rapid Fire)
    def draw_active_effects(self, surface):
        """ Menggambar indikator visual untuk efek aktif """
        now = pygame.time.get_ticks()
        # Efek EMP (lingkaran mengembang)
        if self.emp_effect_active:
            time_passed = now - (self.emp_effect_timer - EMP_EFFECT_DURATION)
            progress = max(0, min(1, time_passed / EMP_EFFECT_DURATION)) # Clamp progress 0-1
            current_radius = int(EMP_RADIUS * progress)
            if 0 < current_radius <= EMP_RADIUS:
                alpha = max(0, 255 - int(progress * 255)) # Fade out alpha
                emp_color_alpha = (*EMP_VISUAL_COLOR[:3], alpha)
                pygame.draw.circle(surface, emp_color_alpha, self.rect.center, current_radius, 3) # Gambar lingkaran outline

        # Efek Rapid Fire (glow merah)
        if self.rapid_fire_active:
             # Gambar glow merah di sekitar player
             glow_surf = self.original_image.copy()
             glow_surf.fill((*BRIGHT_RED, 100), special_flags=pygame.BLEND_RGBA_MULT) # Tint merah transparan
             surface.blit(glow_surf, self.rect.topleft)


    def shoot(self, all_sprites, bullets):
        """ Membuat peluru pemain dan memicu option menembak """
        if self.hidden: return
        now = pygame.time.get_ticks()

        # BARU: Tentukan delay tembak berdasarkan status Rapid Fire
        current_shoot_delay = RAPID_FIRE_DELAY if self.rapid_fire_active else self.shoot_delay

        if now - self.last_shot_time > current_shoot_delay:
            self.last_shot_time = now
            center_x = self.rect.centerx; top_y = self.rect.top
            spawn_y_offset = self.rect.top + 10; spawn_y_offset2 = self.rect.top + 15

            if self.spread_active:
                angles = [0, -SPREAD_ANGLE / 2, SPREAD_ANGLE / 2, -SPREAD_ANGLE, SPREAD_ANGLE]
                spawn_points = [(center_x, top_y), (center_x - 4, spawn_y_offset), (center_x + 4, spawn_y_offset), (center_x - 8, spawn_y_offset2), (center_x + 8, spawn_y_offset2)]
                created_bullets = []
                for i, angle_deg in enumerate(angles):
                    angle_rad = math.radians(angle_deg); vx = BULLET_SPEED * math.sin(angle_rad); vy = -BULLET_SPEED * math.cos(angle_rad)
                    spawn_x, spawn_y = spawn_points[i]; bullet = Bullet(spawn_x, spawn_y, vx, vy, WHITE)
                    created_bullets.append(bullet)
                all_sprites.add(created_bullets); bullets.add(created_bullets)
            else:
                offset_x1 = 15; offset_x2 = 7; offset_x3 = 21; offset_x4 = 30
                if self.weapon_level == 1:
                    b = Bullet(center_x, top_y, 0, -BULLET_SPEED, WHITE); all_sprites.add(b); bullets.add(b)
                elif self.weapon_level == 2:
                    b1 = Bullet(center_x - offset_x1, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b2 = Bullet(center_x + offset_x1, spawn_y_offset, 0, -BULLET_SPEED, WHITE)
                    all_sprites.add(b1, b2); bullets.add(b1, b2)
                elif self.weapon_level == 3:
                    b1 = Bullet(center_x, top_y, 0, -BULLET_SPEED, WHITE); b2 = Bullet(center_x - offset_x1, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b3 = Bullet(center_x + offset_x1, spawn_y_offset, 0, -BULLET_SPEED, WHITE)
                    all_sprites.add(b1, b2, b3); bullets.add(b1, b2, b3)
                elif self.weapon_level == 4:
                    b1 = Bullet(center_x - offset_x3, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b2 = Bullet(center_x - offset_x2, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b3 = Bullet(center_x + offset_x2, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b4 = Bullet(center_x + offset_x3, spawn_y_offset, 0, -BULLET_SPEED, WHITE)
                    all_sprites.add(b1, b2, b3, b4); bullets.add(b1, b2, b3, b4)
                elif self.weapon_level >= 5:
                    b1 = Bullet(center_x, top_y, 0, -BULLET_SPEED, WHITE); b2 = Bullet(center_x - offset_x1, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b3 = Bullet(center_x + offset_x1, spawn_y_offset, 0, -BULLET_SPEED, WHITE); b4 = Bullet(center_x - offset_x4, spawn_y_offset2, 0, -BULLET_SPEED, WHITE); b5 = Bullet(center_x + offset_x4, spawn_y_offset2, 0, -BULLET_SPEED, WHITE)
                    all_sprites.add(b1, b2, b3, b4, b5); bullets.add(b1, b2, b3, b4, b5)

            for option in self.options:
                option.shoot(all_sprites, bullets)

    def increase_weapon_level(self):
        self.weapon_level = min(self.weapon_level + 1, MAX_WEAPON_LEVEL)
        print(f"Weapon Level Up! Level sekarang: {self.weapon_level}")

    def activate_spread(self, duration):
        self.spread_active = True; self.spread_end_time = pygame.time.get_ticks() + duration
        print("Spread Activated!")

    def deactivate_spread(self):
        self.spread_active = False; print("Spread Deactivated")

    def activate_piercing(self, duration):
        self.piercing_rounds_active = True; self.piercing_rounds_end_time = pygame.time.get_ticks() + duration
        print("Piercing Rounds Activated!")

    def deactivate_piercing(self):
        self.piercing_rounds_active = False; print("Piercing Rounds Deactivated")

    def activate_slow_field(self, duration):
        self.slow_field_active = True; self.slow_field_end_time = pygame.time.get_ticks() + duration
        print("Slow Field Activated!")

    def deactivate_slow_field(self):
        self.slow_field_active = False; print("Slow Field Deactivated")

    # BARU: Aktivasi & Deaktivasi Scrambler
    def activate_scrambler(self, duration):
        self.scrambler_active = True; self.scrambler_end_time = pygame.time.get_ticks() + duration
        print("Targeting Scrambler Activated!")

    def deactivate_scrambler(self):
        self.scrambler_active = False; print("Targeting Scrambler Deactivated")

    # BARU: Aktivasi & Deaktivasi Rapid Fire
    def activate_rapid_fire(self):
        if self.rapid_fire_charges > 0:
            self.rapid_fire_charges -= 1
            self.rapid_fire_active = True
            self.rapid_fire_end_time = pygame.time.get_ticks() + RAPID_FIRE_DURATION
            print(f"Rapid Fire Activated! Charges left: {self.rapid_fire_charges}")
            return True
        return False

    def deactivate_rapid_fire(self):
        self.rapid_fire_active = False; print("Rapid Fire Deactivated")

    def ready_shield_upgrade(self):
        self.shield_upgrade_ready = True
        print("Shield Upgrade Ready!")

    def activate_shield(self):
        """ Mengaktifkan perisai (bisa jadi reflektif jika upgrade siap) """
        self.shield_active = True
        if self.shield_upgrade_ready:
            self.current_shield_reflects = True
            self.shield_upgrade_ready = False # Upgrade terpakai
            print("Reflective Shield Activated!")
        else:
            self.current_shield_reflects = False
            print("Shield Activated!")

    def deactivate_shield(self):
        """ Menonaktifkan perisai (setelah kena hit) """
        was_reflective = self.current_shield_reflects
        self.shield_active = False
        self.current_shield_reflects = False # Reset status reflektif
        print(f"Shield Deactivated! (Was Reflective: {was_reflective})")
        expl = Explosion(self.rect.center, self.rect.width + 15, 'shield_break'); all_sprites.add(expl); explosions.add(expl)

    def add_option(self):
        if len(self.options) < self.max_options:
             new_option = Option(self.rect.center)
             self.options.add(new_option)
             all_sprites.add(new_option)
             print(f"Option Added! Count: {len(self.options)}")
             return True
        return False

    def clear_options(self):
        for option in self.options: option.kill()

    def add_bomb(self):
        self.bomb_count += 1
        print(f"Bomb Added! Count: {self.bomb_count}")

    def use_bomb(self, enemies_group, enemy_bullets_group):
        if self.bomb_count > 0:
            print("BOMB USED!")
            self.bomb_count -= 1
            self.bomb_flash_active = True
            self.bomb_flash_timer = pygame.time.get_ticks() + BOMB_FLASH_DURATION
            for enemy in enemies_group:
                expl_e = Explosion(enemy.rect.center, 40); all_sprites.add(expl_e); explosions.add(expl_e)
                enemy.kill()
            for bullet in enemy_bullets_group:
                bullet.kill()
            return True
        return False

    # BARU: Fungsi untuk menggunakan EMP
    def use_emp(self, enemy_bullets_group, boss_bullets_group):
        if self.emp_charges > 0:
            print("EMP BURST USED!")
            self.emp_charges -= 1
            self.emp_effect_active = True # Aktifkan efek visual
            self.emp_effect_timer = pygame.time.get_ticks() + EMP_EFFECT_DURATION

            center = self.rect.center
            bullets_destroyed = 0
            # Cek peluru musuh biasa
            for bullet in enemy_bullets_group:
                dist_x = bullet.rect.centerx - center[0]
                dist_y = bullet.rect.centery - center[1]
                distance = math.hypot(dist_x, dist_y)
                if distance < EMP_RADIUS:
                    bullet.kill()
                    bullets_destroyed += 1
            # Cek peluru boss
            for bullet in boss_bullets_group:
                dist_x = bullet.rect.centerx - center[0]
                dist_y = bullet.rect.centery - center[1]
                distance = math.hypot(dist_x, dist_y)
                if distance < EMP_RADIUS:
                    bullet.kill()
                    bullets_destroyed += 1

            print(f"- Destroyed {bullets_destroyed} bullets.")
            return True
        return False

    # BARU: Fungsi untuk menambah charge EMP
    def add_emp_charge(self):
        self.emp_charges += 1
        print(f"EMP Charge Added! Count: {self.emp_charges}")

    # BARU: Fungsi untuk menambah charge Rapid Fire
    def add_rapid_fire_charge(self):
        self.rapid_fire_charges += 1
        print(f"Rapid Fire Charge Added! Count: {self.rapid_fire_charges}")

    def take_boss_damage(self, amount):
        if self.shield_active: self.deactivate_shield(); return
        if not self.invincible:
            self.current_boss_health -= amount; print(f"Player Hit by Boss! Health: {self.current_boss_health}")

    def reset_boss_health(self):
        self.current_boss_health = PLAYER_BOSS_HEALTH

    def hide(self):
        if self.shield_active: self.deactivate_shield(); return False
        if not self.invincible:
            self.lives -= 1; self.hidden = True; self.hide_timer = pygame.time.get_ticks()
            self.rect.centerx = SCREEN_WIDTH // 2; self.rect.bottom = SCREEN_HEIGHT + 200
            print(f"Player died! Lives left: {self.lives}")
            # Nonaktifkan semua efek saat mati
            self.deactivate_spread(); self.deactivate_piercing(); self.deactivate_slow_field()
            self.deactivate_scrambler(); self.deactivate_rapid_fire() # Nonaktifkan efek baru juga
            self.shield_active = False; self.current_shield_reflects = False; self.clear_options()
            return True
        return False

    def unhide(self):
        self.hidden = False; self.rect.centerx = SCREEN_WIDTH // 2; self.rect.bottom = SCREEN_HEIGHT - 10
        self.invincible = True; self.invincible_timer = pygame.time.get_ticks() + PLAYER_INVINCIBILITY_DURATION
        self.image.set_alpha(255)

# --- Kelas Option ---
# (Tidak ada perubahan)
class Option(pygame.sprite.Sprite):
    """ Kapal kecil pendamping pemain """
    def __init__(self, start_pos):
        super().__init__()
        self.image = pygame.Surface([15, 15], pygame.SRCALPHA)
        pygame.draw.circle(self.image, OPTION_COLOR, (8, 8), 7)
        self.rect = self.image.get_rect(center=start_pos)
        self.target_x = start_pos[0]
        self.target_y = start_pos[1]
        self.follow_speed = 0.1

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

    def update(self):
        self.rect.centerx += int((self.target_x - self.rect.centerx) * self.follow_speed)
        self.rect.centery += int((self.target_y - self.rect.centery) * self.follow_speed)

    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top, 0, -BULLET_SPEED, WHITE)
        all_sprites.add(bullet)
        bullets.add(bullet)

# --- Kelas Enemy ---
class Enemy(pygame.sprite.Sprite):
    """ Kelas dasar untuk musuh normal """
    enemy_size = 30
    def __init__(self, x, y):
        super().__init__(); self.original_image = pygame.Surface([self.enemy_size, self.enemy_size], pygame.SRCALPHA); self.draw_shape()
        self.image = self.original_image.copy(); self.rect = self.image.get_rect(); self.rect.x = x; self.rect.y = y
        self.base_shoot_delay = ENEMY_SHOOT_DELAY_BASE
        self.last_shot_time = pygame.time.get_ticks() + random.randint(500, self.base_shoot_delay + 500)
        self.wave_offset = random.uniform(0, 2 * math.pi); self.base_center_y = float(self.rect.centery)
        self.speed_x = random.uniform(-ENEMY_MAX_RANDOM_X_SPEED, ENEMY_MAX_RANDOM_X_SPEED)
        self.is_hit = False; self.hit_timer = 0; self.speed_y = ENEMY_SPEED_Y

    def draw_shape(self):
        """ Menggambar bentuk default musuh (spiky) """
        self.original_image.fill((0,0,0,0))
        center = (self.enemy_size // 2, self.enemy_size // 2); radius_outer = self.enemy_size // 2; radius_inner = radius_outer * 0.5
        num_points = 6; points = []
        for i in range(num_points * 2):
            angle = math.pi * 2 * i / (num_points * 2) - math.pi / 2; radius = radius_outer if i % 2 == 0 else radius_inner
            px = center[0] + radius * math.cos(angle); py = center[1] + radius * math.sin(angle); points.append((px, py))
        pygame.draw.polygon(self.original_image, ENEMY_COLOR, points)

    def update(self):
        """ Memperbarui posisi musuh, cek hit flash, batas layar, dan efek slow field """
        now = pygame.time.get_ticks()

        # Cek efek slow field dari player
        current_speed_factor = 1.0
        if player in player_group and player.slow_field_active:
            dist_x = self.rect.centerx - player.rect.centerx
            dist_y = self.rect.centery - player.rect.centery
            distance = math.hypot(dist_x, dist_y)
            if distance < SLOW_FIELD_RADIUS:
                current_speed_factor = SLOW_FIELD_FACTOR

        # Pergerakan Horizontal
        self.rect.x += self.speed_x * current_speed_factor # Terapkan faktor perlambatan
        if random.random() < 0.04:
            self.speed_x += random.uniform(-0.7, 0.7);
            self.speed_x = max(-ENEMY_MAX_RANDOM_X_SPEED - 0.2, min(ENEMY_MAX_RANDOM_X_SPEED + 0.2, self.speed_x))
            if random.random() < 0.015: self.speed_x *= -1

        enemy_margin = 5
        if self.rect.right > SCREEN_WIDTH - enemy_margin:
            self.rect.right = SCREEN_WIDTH - enemy_margin
            self.speed_x *= -1
        elif self.rect.left < enemy_margin:
            self.rect.left = enemy_margin
            self.speed_x *= -1

        # Pergerakan Vertikal
        self.base_center_y += self.speed_y * current_speed_factor # Terapkan faktor perlambatan
        oscillation = math.sin(now * ENEMY_OSCILLATION_SPEED + self.wave_offset) * ENEMY_OSCILLATION_AMPLITUDE
        self.rect.centery = int(self.base_center_y + oscillation)

        # Cek batas bawah
        buffer_bottom = 40
        if self.rect.top > SCREEN_HEIGHT + buffer_bottom: self.kill()

        # Update Hit Flash
        if self.is_hit and now - self.hit_timer > HIT_FLASH_DURATION:
            self.is_hit = False; self.image = self.original_image.copy()

    def shoot(self, all_sprites, enemy_bullets):
        """ Secara acak membuat peluru musuh dengan kecepatan & delay terskala """
        now = pygame.time.get_ticks()
        wave_scale_factor_delay = current_wave_index // 3
        effective_shoot_delay = max(MIN_ENEMY_SHOOT_DELAY, self.base_shoot_delay - wave_scale_factor_delay * ENEMY_SHOOT_DELAY_SCALE)

        wave_scale_factor_speed = current_wave_index // 4
        effective_bullet_speed = ENEMY_BULLET_SPEED_BASE + wave_scale_factor_speed * ENEMY_BULLET_SPEED_SCALE

        # BARU: Cek efek Scrambler
        fire_chance = 0.20
        if player in player_group and player.scrambler_active:
            fire_chance *= 0.3 # Kurangi drastis peluang tembak jika scrambler aktif

        if now - self.last_shot_time > effective_shoot_delay + random.randint(-150, 150):
             self.last_shot_time = now
             if random.random() < fire_chance:
                bullet = Bullet(self.rect.centerx, self.rect.bottom, 0, effective_bullet_speed, YELLOW);
                all_sprites.add(bullet); enemy_bullets.add(bullet)

    def flash(self):
        """ Aktifkan efek hit flash """
        self.is_hit = True; self.hit_timer = pygame.time.get_ticks()
        flash_surf = self.original_image.copy(); flash_surf.fill(WHITE, special_flags=pygame.BLEND_RGB_MAX); self.image = flash_surf

    def take_damage(self, amount):
        """ Mengurangi health (jika ada) dan mengembalikan True jika mati """
        self.flash()
        return True

# --- Kelas DasherEnemy ---
class DasherEnemy(Enemy):
    """ Musuh tipe Dasher, lebih cepat dan bisa menerjang """
    def __init__(self, x, y):
        super().__init__(x, y); self.speed_y = DASHER_SPEED_Y
        self.is_dashing = False; self.dash_timer = 0; self.dash_target_x = 0; self.original_speed_x = self.speed_x

    def draw_shape(self):
        """ Menggambar bentuk Dasher (misal: panah) """
        self.original_image.fill((0,0,0,0))
        points = [(self.enemy_size // 2, 0), (self.enemy_size, self.enemy_size), (self.enemy_size // 2, self.enemy_size * 0.7), (0, self.enemy_size)]
        pygame.draw.polygon(self.original_image, DASHER_COLOR, points)

    def update(self):
        """ Update Dasher, termasuk logika dash, batas layar, dan slow field """
        # Panggil update dasar dari Enemy (sudah termasuk cek slow field untuk speed_x, speed_y)
        super().update()
        now = pygame.time.get_ticks()

        # Cek slow field (lagi, khusus untuk kecepatan dash)
        current_dash_speed_factor = 1.0
        if player in player_group and player.slow_field_active:
            dist_x = self.rect.centerx - player.rect.centerx
            dist_y = self.rect.centery - player.rect.centery
            distance = math.hypot(dist_x, dist_y)
            if distance < SLOW_FIELD_RADIUS:
                current_dash_speed_factor = SLOW_FIELD_FACTOR

        # Logika Dash
        if self.is_dashing:
            if now - self.dash_timer > DASHER_DASH_DURATION:
                self.is_dashing = False; self.speed_x = self.original_speed_x
            else:
                # Override pergerakan X jika sedang dash
                dash_move = DASHER_DASH_SPEED_X * current_dash_speed_factor # Terapkan slow field ke dash
                if self.rect.centerx < self.dash_target_x: self.rect.x += dash_move
                else: self.rect.x -= dash_move
                # Cek lagi batas layar saat dash
                enemy_margin = 5
                if self.rect.right > SCREEN_WIDTH - enemy_margin:
                    self.rect.right = SCREEN_WIDTH - enemy_margin; self.is_dashing = False; self.speed_x = -abs(self.original_speed_x)
                elif self.rect.left < enemy_margin:
                    self.rect.left = enemy_margin; self.is_dashing = False; self.speed_x = abs(self.original_speed_x)
        else:
            # Cek peluang dash jika tidak sedang dash
            if random.random() < DASHER_DASH_CHANCE:
                self.is_dashing = True; self.dash_timer = now; self.original_speed_x = self.speed_x
                if player in player_group: self.dash_target_x = player.rect.centerx
                else: self.dash_target_x = SCREEN_WIDTH // 2
                print("Dasher starts dashing!")

    def shoot(self, all_sprites, enemy_bullets): pass

# --- Kelas MineLayerEnemy ---
class MineLayerEnemy(Enemy):
    """ Musuh yang menjatuhkan ranjau, bukan menembak """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed_y = MINELAYER_SPEED_Y
        self.last_drop_time = pygame.time.get_ticks() + random.randint(500, MINELAYER_DROP_DELAY)

    def draw_shape(self):
        """ Menggambar bentuk MineLayer (misal: kotak dengan tanda X) """
        self.original_image.fill((0,0,0,0))
        pygame.draw.rect(self.original_image, MINELAYER_COLOR, (2, 2, self.enemy_size - 4, self.enemy_size - 4), border_radius=4)
        pygame.draw.line(self.original_image, WHITE, (5, 5), (self.enemy_size - 6, self.enemy_size - 6), 3)
        pygame.draw.line(self.original_image, WHITE, (5, self.enemy_size - 6), (self.enemy_size - 6, 5), 3)

    def shoot(self, all_sprites, enemy_bullets):
        """ Override shoot: Jatuhkan ranjau (jika cukup rendah), bukan peluru """
        now = pygame.time.get_ticks()
        if self.rect.bottom > MINELAYER_DROP_MIN_Y:
            if now - self.last_drop_time > MINELAYER_DROP_DELAY + random.randint(-300, 300):
                self.last_drop_time = now
                print("Mine Layer dropped a mine!")
                new_mine = Mine(self.rect.centerx, self.rect.bottom)
                all_sprites.add(new_mine)
                mines.add(new_mine)

# --- Kelas Mine ---
class Mine(pygame.sprite.Sprite):
    """ Ranjau yang dijatuhkan MineLayerEnemy, melayang turun dan meledak """
    mine_size = 18
    def __init__(self, centerx, bottomy):
        super().__init__()
        self.image = pygame.Surface([self.mine_size, self.mine_size], pygame.SRCALPHA)
        pygame.draw.circle(self.image, MINE_COLOR, (self.mine_size // 2, self.mine_size // 2), self.mine_size // 2 - 1)
        pygame.draw.circle(self.image, WHITE, (self.mine_size // 2, self.mine_size // 2), self.mine_size // 2 - 1, 1)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottomy
        self.spawn_time = pygame.time.get_ticks()
        self.speed_y = MINE_SPEED_Y

    def update(self):
        """ Gerakkan ranjau ke bawah dan cek durasi/batas layar """
        now = pygame.time.get_ticks()

        # Cek efek slow field dari player
        current_speed_factor = 1.0
        if player in player_group and player.slow_field_active:
            dist_x = self.rect.centerx - player.rect.centerx
            dist_y = self.rect.centery - player.rect.centery
            distance = math.hypot(dist_x, dist_y)
            if distance < SLOW_FIELD_RADIUS:
                current_speed_factor = SLOW_FIELD_FACTOR

        self.rect.y += self.speed_y * current_speed_factor # Terapkan faktor perlambatan

        if now - self.spawn_time > MINE_DURATION:
            self.explode(player_group)
        elif self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def explode(self, player_group_ref):
        """ Efek saat ranjau meledak (dipanggil saat kena player atau waktu habis) """
        if self not in all_sprites: return

        print("Mine exploded!")
        expl_center = self.rect.center
        expl = Explosion(expl_center, MINE_EXPLOSION_RADIUS * 2, 'normal')
        all_sprites.add(expl)
        explosions.add(expl)

        for player_obj in player_group_ref:
            dist_x = player_obj.rect.centerx - expl_center[0]
            dist_y = player_obj.rect.centery - expl_center[1]
            distance = math.hypot(dist_x, dist_y)

            if distance < MINE_EXPLOSION_RADIUS:
                print(f"Player hit by mine explosion! Distance: {distance:.1f}")
                if not player_obj.invincible:
                    if player_obj.shield_active:
                        player_obj.deactivate_shield()
                    else:
                        if player_obj.hide():
                             pass
        self.kill()

# --- Kelas CommanderEnemy ---
class CommanderEnemy(Enemy):
    """ Musuh spesial tipe Commander, lebih kuat dan memanggil bantuan """
    enemy_size = 35 # Sedikit lebih besar
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed_y = COMMANDER_SPEED_Y # Lebih lambat
        self.health = COMMANDER_HEALTH
        self.last_reinforcement_time = pygame.time.get_ticks() + random.randint(1000, COMMANDER_REINFORCEMENT_DELAY)
        self.reinforcement_delay = COMMANDER_REINFORCEMENT_DELAY

    def draw_shape(self):
        """ Menggambar bentuk Commander (misal: lebih lebar, warna ungu) """
        self.original_image = pygame.Surface([self.enemy_size, self.enemy_size], pygame.SRCALPHA) # Buat surface baru
        self.original_image.fill((0,0,0,0))
        # Contoh: Bentuk seperti perisai atau emblem
        points = [(self.enemy_size * 0.5, 0), (self.enemy_size, self.enemy_size * 0.4),
                  (self.enemy_size * 0.8, self.enemy_size), (self.enemy_size * 0.2, self.enemy_size),
                  (0, self.enemy_size * 0.4)]
        pygame.draw.polygon(self.original_image, COMMANDER_COLOR, points)
        pygame.draw.circle(self.original_image, YELLOW, (self.enemy_size // 2, self.enemy_size // 2), 5) # Titik tengah

    def update(self, all_sprites_ref, enemies_ref): # Terima grup sprite untuk spawn
        """ Update Commander: Gerak dasar + panggil bantuan """
        # Panggil update dasar dari Enemy (gerak, batas layar, flash, slow field)
        super().update()
        now = pygame.time.get_ticks()

        # Logika memanggil bantuan
        if now - self.last_reinforcement_time > self.reinforcement_delay:
            self.last_reinforcement_time = now
            self.call_reinforcements(all_sprites_ref, enemies_ref)

    def call_reinforcements(self, all_sprites_ref, enemies_ref):
        """ Memunculkan musuh Enemy standar di dekat Commander """
        print(f"Commander ({self.rect.centerx},{self.rect.centery}) calling reinforcements!")
        spawn_count = 0
        for i in range(COMMANDER_REINFORCEMENTS_COUNT):
            # Cek batas musuh di layar sebelum spawn
            if len(enemies_ref) < MAX_ENEMIES_ON_SCREEN:
                # Tentukan posisi spawn di samping Commander
                offset_x = (self.enemy_size // 2 + Enemy.enemy_size // 2 + 10) * (1 if i % 2 == 0 else -1)
                spawn_x = self.rect.centerx + offset_x
                spawn_y = self.rect.centery
                # Pastikan spawn di dalam layar horizontal
                spawn_x = max(Enemy.enemy_size // 2, min(SCREEN_WIDTH - Enemy.enemy_size // 2, spawn_x))

                print(f"- Spawning reinforcement at ({spawn_x},{spawn_y})")
                new_enemy = Enemy(spawn_x - Enemy.enemy_size // 2, spawn_y - Enemy.enemy_size // 2)
                all_sprites_ref.add(new_enemy)
                enemies_ref.add(new_enemy)
                spawn_count += 1
            else:
                print("- Max enemies on screen reached, cannot spawn reinforcement.")
                break # Hentikan spawn jika layar penuh

    def shoot(self, all_sprites, enemy_bullets):
        """ Commander tidak menembak peluru biasa """
        pass

    def take_damage(self, amount):
        """ Mengurangi health Commander, kembalikan True jika mati """
        if self.health > 0:
            self.health -= amount
            print(f"Commander Hit! Health: {self.health}/{COMMANDER_HEALTH}")
            self.flash() # Tampilkan efek flash
            if self.health <= 0:
                print("Commander Defeated!")
                return True # Mati
        return False # Belum mati

# --- Kelas BossEnemy ---
class BossEnemy(pygame.sprite.Sprite):
    """ Merepresentasikan musuh Boss dengan efek hit flash dan drop powerup """
    def __init__(self, level):
        super().__init__(); self.level = level
        self.max_health = BOSS_HEALTH_INITIAL + (level - 1) * BOSS_HEALTH_INCREMENT; self.current_health = self.max_health
        boss_width = 120; boss_height = 80
        self.original_image = pygame.Surface([boss_width, boss_height]); self.original_image.fill(BOSS_COLOR)
        pygame.draw.rect(self.original_image, RED, (boss_width * 0.4, boss_height * 0.2, 10, 10))
        pygame.draw.rect(self.original_image, RED, (boss_width * 0.6 - 10, boss_height * 0.2, 10, 10))
        pygame.draw.rect(self.original_image, YELLOW, (boss_width // 2 - 15, boss_height * 0.7, 30, 15))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(); self.rect.centerx = SCREEN_WIDTH // 2; self.rect.bottom = -20
        self.target_y = 80;
        # PERBARUAN: Logika arah dan kecepatan untuk Boss
        self.direction = 1 # 1 untuk kanan, -1 untuk kiri
        self.base_speed_x = BOSS_SPEED_X_BASE # Simpan magnitudo dasar
        self.last_shot_time = pygame.time.get_ticks()
        self.is_hit = False; self.hit_timer = 0
        self.boss_margin = 20
        self.dropped_at_75 = False
        self.dropped_at_50 = False
        self.dropped_at_25 = False

    def calculate_dynamic_stats(self, player_obj):
        """ Menghitung statistik dinamis boss berdasarkan status player """
        if not player_obj: # Jika player tidak ada (misal baru mati)
            # Kembalikan nilai dasar
            return BOSS_SHOOT_DELAY_BASE, BOSS_BULLET_SPEED_BASE, BOSS_SPEED_X_BASE, BOSS_SPREAD_CHANCE_BASE

        # Hitung skor kekuatan player
        power_level = 0
        power_level += (player_obj.weapon_level - 1) # 0-4
        power_level += len(player_obj.options)      # 0-2
        power_level += min(player_obj.bomb_count, 2) # 0-2 (pengaruh bom dibatasi)
        # PERBARUAN: Naikkan bobot shield
        if player_obj.shield_active: power_level += 2
        if player_obj.spread_active: power_level += 2

        # Skor maksimal teoritis (4 + 2 + 2 + 2 + 2 = 12)
        max_power = 12
        scale_modifier = min(1.0, power_level / max_power) if max_power > 0 else 0
        # print(f"Player Power: {power_level}/{max_power}, Scale: {scale_modifier:.2f}") # Debug

        # Hitung statistik efektif menggunakan interpolasi linear
        eff_delay = BOSS_SHOOT_DELAY_BASE - (BOSS_SHOOT_DELAY_BASE - BOSS_SHOOT_DELAY_MIN) * scale_modifier
        eff_bullet_spd = BOSS_BULLET_SPEED_BASE + (BOSS_BULLET_SPEED_MAX - BOSS_BULLET_SPEED_BASE) * scale_modifier
        eff_move_spd_mag = BOSS_SPEED_X_BASE + (BOSS_SPEED_X_MAX - BOSS_SPEED_X_BASE) * scale_modifier # Hitung magnitudo
        eff_spread = BOSS_SPREAD_CHANCE_BASE + (BOSS_SPREAD_CHANCE_MAX - BOSS_SPREAD_CHANCE_BASE) * scale_modifier

        # Return integer delay, float speeds/chance, dan MAGNITUDO kecepatan gerak
        return int(eff_delay), eff_bullet_spd, eff_move_spd_mag, eff_spread

    def update(self, player_obj): # PERBARUAN: Terima objek player
        """ Memperbarui posisi, menembak (dengan stats dinamis), batas layar, dan cek hit flash """
        now = pygame.time.get_ticks()

        # PERBARUAN: Hitung stats dinamis berdasarkan player
        _, _, effective_move_speed_mag, _ = self.calculate_dynamic_stats(player_obj)

        # Gerak masuk ke layar
        if self.rect.centery < self.target_y:
            self.rect.y += 2
        else:
            # Gerak horizontal setelah masuk
            current_speed = effective_move_speed_mag * self.direction # Terapkan arah
            self.rect.x += current_speed # Gunakan kecepatan efektif dengan arah

            # PERBARUAN: Logika pantulan horizontal Boss menggunakan direction
            if self.rect.right > SCREEN_WIDTH - self.boss_margin:
                self.rect.right = SCREEN_WIDTH - self.boss_margin # Jepit posisi kanan
                self.direction = -1 # Balik arah
            elif self.rect.left < self.boss_margin:
                self.rect.left = self.boss_margin # Jepit posisi kiri
                self.direction = 1 # Balik arah

        # Menembak (logika penentuan waktu ada di dalam shoot)
        self.shoot(all_sprites, boss_bullets, player_obj) # Pass player_obj

        # Hit flash
        if self.is_hit and now - self.hit_timer > HIT_FLASH_DURATION:
            self.is_hit = False; self.image = self.original_image.copy()

    def shoot(self, all_sprites, boss_bullets, player_obj): # PERBARUAN: Terima player_obj
        """ Logika menembak boss dengan statistik dinamis """
        now = pygame.time.get_ticks()
        # PERBARUAN: Hitung stats dinamis untuk menembak
        effective_delay, effective_bullet_speed, _, effective_spread_chance = self.calculate_dynamic_stats(player_obj)

        if now - self.last_shot_time > effective_delay:
            self.last_shot_time = now
            spawn_x = self.rect.centerx; spawn_y = self.rect.bottom - 10

            # BARU: Cek Scrambler sebelum tentukan pola tembak
            use_spread = random.random() < effective_spread_chance
            if player_obj and player_obj.scrambler_active:
                use_spread = False # Scrambler menonaktifkan spread shot
                print("Boss spread shot disabled by Scrambler!")

            if use_spread:
                 print(f"Boss Spread Shot! (Chance: {effective_spread_chance:.2f})")
                 angles = [0, -8, 8, -16, 16, -24, 24]
                 for angle_deg in angles:
                     angle_rad = math.radians(angle_deg)
                     # Gunakan kecepatan peluru efektif
                     vx = effective_bullet_speed * math.sin(angle_rad)
                     vy = effective_bullet_speed * math.cos(angle_rad)
                     b = Bullet(spawn_x, spawn_y, vx, vy, BOSS_BULLET_COLOR); all_sprites.add(b); boss_bullets.add(b)
            else:
                 # Tembakan lurus 3 peluru
                 offset = 20
                 # Gunakan kecepatan peluru efektif
                 b1 = Bullet(spawn_x - offset, spawn_y, 0, effective_bullet_speed, BOSS_BULLET_COLOR);
                 b2 = Bullet(spawn_x, spawn_y, 0, effective_bullet_speed, BOSS_BULLET_COLOR);
                 b3 = Bullet(spawn_x + offset, spawn_y, 0, effective_bullet_speed, BOSS_BULLET_COLOR)
                 all_sprites.add(b1, b2, b3); boss_bullets.add(b1, b2, b3)

    def take_damage(self, amount, all_sprites_ref, powerups_ref):
        """ Mengurangi health boss, memicu flash, dan cek drop powerup """
        if self.current_health <= 0: return False

        self.current_health -= amount
        self.flash()
        print(f"Boss Hit! Health: {self.current_health}/{self.max_health}")

        if self.max_health > 0:
            health_percent = self.current_health / self.max_health

            if not self.dropped_at_75 and health_percent < 0.75:
                self.dropped_at_75 = True
                print("Boss dropped SHIELD powerup!")
                powerup = PowerUp(self.rect.center, 'shield')
                all_sprites_ref.add(powerup)
                powerups_ref.add(powerup)

            elif not self.dropped_at_50 and health_percent < 0.50:
                self.dropped_at_50 = True
                print("Boss dropped BOMB powerup!")
                powerup = PowerUp(self.rect.center, 'bomb')
                all_sprites_ref.add(powerup)
                powerups_ref.add(powerup)

            elif not self.dropped_at_25 and health_percent < 0.25:
                self.dropped_at_25 = True
                print("Boss dropped AMMO powerup!")
                powerup = PowerUp(self.rect.center, 'ammo')
                all_sprites_ref.add(powerup)
                powerups_ref.add(powerup)

        return self.current_health <= 0

    def draw_health_bar(self, surface):
        """ Menggambar health bar boss """
        if self.current_health > 0:
            bar_length = 150; bar_height = 15; fill_percent = self.current_health / self.max_health
            fill_length = int(bar_length * fill_percent)
            outline_rect = pygame.Rect(self.rect.centerx - bar_length // 2, self.rect.top - bar_height - 5, bar_length, bar_height)
            fill_rect = pygame.Rect(outline_rect.left, outline_rect.top, fill_length, bar_height)
            pygame.draw.rect(surface, HEALTH_BAR_BG, outline_rect); pygame.draw.rect(surface, BOSS_HEALTH_COLOR, fill_rect); pygame.draw.rect(surface, WHITE, outline_rect, 2)

    def flash(self):
        """ Aktifkan efek hit flash """
        if not self.is_hit:
            self.is_hit = True; self.hit_timer = pygame.time.get_ticks()
            flash_surf = self.original_image.copy(); flash_surf.fill(WHITE, special_flags=pygame.BLEND_RGB_MAX); self.image = flash_surf

# --- Kelas Bullet ---
class Bullet(pygame.sprite.Sprite):
    """ Merepresentasikan peluru """
    def __init__(self, x, y, speed_x, speed_y, color):
        super().__init__(); self.image = pygame.Surface([4, 10]); self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color # Simpan warna untuk cek slow field
        if speed_y < 0: self.rect.centerx = x; self.rect.bottom = y
        else: self.rect.centerx = x; self.rect.top = y
        self.speed_x = speed_x; self.speed_y = speed_y

    def update(self):
        """ Gerakkan peluru, cek slow field, dan hapus jika keluar layar """
        # Cek efek slow field dari player
        current_speed_factor = 1.0
        # Hanya perlambat peluru musuh (kuning) atau boss (oranye)
        is_enemy_bullet = self.color == YELLOW or self.color == BOSS_BULLET_COLOR
        if is_enemy_bullet and player in player_group and player.slow_field_active:
            dist_x = self.rect.centerx - player.rect.centerx
            dist_y = self.rect.centery - player.rect.centery
            distance = math.hypot(dist_x, dist_y)
            if distance < SLOW_FIELD_RADIUS:
                current_speed_factor = SLOW_FIELD_FACTOR

        # Gerakkan peluru dengan kecepatan efektif
        self.rect.x += self.speed_x * current_speed_factor
        self.rect.y += self.speed_y * current_speed_factor

        # Hapus jika keluar layar
        buffer = 20
        if self.rect.bottom < -buffer or self.rect.top > SCREEN_HEIGHT + buffer or \
           self.rect.right < -buffer or self.rect.left > SCREEN_WIDTH + buffer:
            self.kill()

# --- Kelas PowerUp ---
class PowerUp(pygame.sprite.Sprite):
    """ Merepresentasikan item power-up """
    def __init__(self, center_pos, type):
        super().__init__(); self.type = type; item_size = 22
        self.image = pygame.Surface([item_size, item_size], pygame.SRCALPHA)
        color = WHITE # Default color
        if self.type == 'ammo':
            color = POWERUP_AMMO_COLOR
            pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
            pygame.draw.line(self.image, WHITE, (item_size // 2, item_size * 0.2), (item_size // 2, item_size * 0.8), 3)
            pygame.draw.line(self.image, WHITE, (item_size * 0.2, item_size // 2), (item_size * 0.8, item_size // 2), 3)
        elif self.type == 'spread':
            color = POWERUP_SPREAD_COLOR
            pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
            cx, cy = item_size // 2, item_size // 2
            pygame.draw.line(self.image, WHITE, (cx, cy), (cx, item_size * 0.1), 2)
            pygame.draw.line(self.image, WHITE, (cx, cy), (item_size * 0.2, item_size * 0.2), 2)
            pygame.draw.line(self.image, WHITE, (cx, cy), (item_size * 0.8, item_size * 0.2), 2)
        elif self.type == 'shield':
             color = POWERUP_SHIELD_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             rect_inner = pygame.Rect(item_size*0.3, item_size*0.2, item_size*0.4, item_size*0.6)
             pygame.draw.rect(self.image, WHITE, rect_inner, border_radius=2)
        elif self.type == 'option':
             color = POWERUP_OPTION_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             pygame.draw.circle(self.image, WHITE, (item_size // 2, item_size // 2), item_size // 4)
        elif self.type == 'bomb':
             color = POWERUP_BOMB_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             pygame.draw.circle(self.image, BLACK, (item_size // 2, item_size // 2), item_size // 3)
             pygame.draw.line(self.image, WHITE, (item_size // 2, item_size * 0.1), (item_size * 0.7, item_size * 0.3), 2)
        elif self.type == 'shield_upgrade':
             color = POWERUP_SHIELD_UPGRADE_COLOR
             pygame.draw.rect(self.image, color, (2, 2, item_size-4, item_size-4), border_radius=3) # Kotak emas
             pygame.draw.circle(self.image, WHITE, (item_size // 2, item_size // 2), item_size // 4, 2) # Lingkaran putih di tengah
        elif self.type == 'piercing':
             color = POWERUP_PIERCING_COLOR
             pygame.draw.rect(self.image, color, (item_size*0.1, item_size*0.3, item_size*0.8, item_size*0.4)) # Persegi panjang abu
             pygame.draw.line(self.image, WHITE, (item_size*0.1, item_size*0.5), (item_size*0.9, item_size*0.5), 1) # Garis tengah
             pygame.draw.polygon(self.image, WHITE, [(item_size*0.7, item_size*0.3), (item_size*0.95, item_size*0.5), (item_size*0.7, item_size*0.7)]) # Panah ujung
        elif self.type == 'slow_field':
             color = POWERUP_SLOWFIELD_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             # Gambar ikon jam pasir sederhana
             pygame.draw.polygon(self.image, WHITE, [(item_size*0.3, item_size*0.3), (item_size*0.7, item_size*0.3), (item_size*0.5, item_size*0.5)])
             pygame.draw.polygon(self.image, WHITE, [(item_size*0.3, item_size*0.7), (item_size*0.7, item_size*0.7), (item_size*0.5, item_size*0.5)])
        # BARU: Visual Powerup Baru
        elif self.type == 'emp':
             color = POWERUP_EMP_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             # Gambar ikon petir sederhana
             pygame.draw.polygon(self.image, WHITE, [(item_size*0.5, item_size*0.1), (item_size*0.3, item_size*0.5), (item_size*0.5, item_size*0.5), (item_size*0.4, item_size*0.9), (item_size*0.7, item_size*0.5), (item_size*0.5, item_size*0.5)])
        elif self.type == 'rapid_fire':
             color = POWERUP_RAPIDFIRE_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             # Gambar ikon tiga peluru
             sz = item_size * 0.15
             pygame.draw.rect(self.image, WHITE, (item_size*0.3 - sz/2, item_size*0.3, sz, sz*2))
             pygame.draw.rect(self.image, WHITE, (item_size*0.5 - sz/2, item_size*0.3, sz, sz*2))
             pygame.draw.rect(self.image, WHITE, (item_size*0.7 - sz/2, item_size*0.3, sz, sz*2))
        elif self.type == 'scrambler':
             color = POWERUP_SCRAMBLER_COLOR
             pygame.draw.circle(self.image, color, (item_size // 2, item_size // 2), item_size // 2)
             # Gambar ikon sinyal acak
             pygame.draw.line(self.image, BLACK, (item_size*0.2, item_size*0.7), (item_size*0.4, item_size*0.3), 2)
             pygame.draw.line(self.image, BLACK, (item_size*0.4, item_size*0.3), (item_size*0.6, item_size*0.8), 2)
             pygame.draw.line(self.image, BLACK, (item_size*0.6, item_size*0.8), (item_size*0.8, item_size*0.2), 2)


        self.rect = self.image.get_rect(); self.rect.center = center_pos; self.speed_y = POWERUP_SPEED

    def update(self):
        """ Gerakkan power-up ke bawah """
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT: self.kill()

# --- Kelas Explosion ---
# (Tidak ada perubahan)
class Explosion(pygame.sprite.Sprite):
    """ Animasi ledakan sederhana """
    def __init__(self, center, size, type='normal'):
        super().__init__(); self.size = size
        self.image = pygame.Surface((size, size), pygame.SRCALPHA); self.rect = self.image.get_rect(center=center)
        self.frame = 0; self.frame_rate = 40; self.last_update = pygame.time.get_ticks(); self.type = type
        if self.type == 'shield_break':
            self.colors = [(0, 200, 255), (0, 150, 200)]; self.max_frames = len(self.colors) * 3
        else: self.colors = EXPLOSION_COLORS; self.max_frames = len(self.colors) * 2

    def update(self):
        """ Update frame animasi ledakan """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now; self.frame += 1
            if self.frame >= self.max_frames: self.kill()
            else:
                try:
                    radius = int((self.frame / self.max_frames) * (self.size / 2))
                    color_index_divisor = 3 if self.type == 'shield_break' else 2
                    color_index = self.frame // color_index_divisor; color = self.colors[color_index % len(self.colors)]
                    self.image.fill((0,0,0,0)); pygame.draw.circle(self.image, color, (self.size // 2, self.size // 2), radius)
                except IndexError: self.kill()


# --- Inisialisasi Game ---
pygame.init(); pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)); pygame.display.set_caption("Don-shoot Near")
clock = pygame.time.Clock(); font_name = pygame.font.match_font('arial'); high_score = 0

# Font & Ikon UI
bomb_font = pygame.font.Font(font_name, 16)
charge_font = pygame.font.Font(font_name, 14) # Font untuk charge item
credit_font = pygame.font.Font(font_name, 12) # Font untuk kredit
bomb_icon_surf = pygame.Surface((15, 15), pygame.SRCALPHA)
pygame.draw.circle(bomb_icon_surf, GREY, (8, 8), 7)
pygame.draw.circle(bomb_icon_surf, BLACK, (8, 8), 4)
pygame.draw.line(bomb_icon_surf, WHITE, (8, 1), (11, 4), 2)
# BARU: Ikon untuk EMP dan Rapid Fire
emp_icon_surf = pygame.Surface((15, 15), pygame.SRCALPHA)
pygame.draw.circle(emp_icon_surf, ELECTRIC_BLUE, (8, 8), 7)
pygame.draw.polygon(emp_icon_surf, WHITE, [(7, 2), (5, 8), (7, 8), (6, 13), (10, 7), (8, 7)])
rapid_icon_surf = pygame.Surface((15, 15), pygame.SRCALPHA)
pygame.draw.circle(rapid_icon_surf, BRIGHT_RED, (8, 8), 7)
sz = 2; sp = 4
pygame.draw.rect(rapid_icon_surf, WHITE, (sp-sz/2, 4, sz, sz*2.5))
pygame.draw.rect(rapid_icon_surf, WHITE, (2*sp-sz/2, 4, sz, sz*2.5))
pygame.draw.rect(rapid_icon_surf, WHITE, (3*sp-sz/2, 4, sz, sz*2.5))


def draw_text(surf, text, size, x, y, color=WHITE, align="midtop"):
    """ Fungsi bantuan untuk menggambar teks dengan alignment """
    font = pygame.font.Font(font_name, size); text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "midtop": text_rect.midtop = (x, y)
    elif align == "midbottom": text_rect.midbottom = (x, y)
    elif align == "topleft": text_rect.topleft = (x, y)
    elif align == "bottomleft": text_rect.bottomleft = (x, y)
    elif align == "topright": text_rect.topright = (x, y)
    elif align == "bottomright": text_rect.bottomright = (x, y)
    elif align == "center": text_rect.center = (x, y)
    else: text_rect.midtop = (x, y) # Default
    surf.blit(text_surface, text_rect)


def draw_player_health_bar(surf, x, y, current_hp, max_hp):
    """ Menggambar health bar pemain saat lawan boss """
    if current_hp < 0: current_hp = 0
    bar_length = 100; bar_height = 10; fill_percent = current_hp / max_hp; fill_length = int(bar_length * fill_percent)
    outline_rect = pygame.Rect(x, y, bar_length, bar_height); fill_rect = pygame.Rect(x, y, fill_length, bar_height)
    pygame.draw.rect(surf, HEALTH_BAR_BG, outline_rect); pygame.draw.rect(surf, PLAYER_HEALTH_COLOR, fill_rect); pygame.draw.rect(surf, WHITE, outline_rect, 1)

def draw_player_lives(surf, x, y, lives, img):
    """ Menggambar ikon nyawa pemain """
    icon_spacing = 5
    for i in range(lives):
        img_rect = img.get_rect(); small_img = pygame.transform.scale(img, (img_rect.width // 2, img_rect.height // 2))
        small_rect = small_img.get_rect(); small_rect.x = x + i * (small_rect.width + icon_spacing); small_rect.y = y
        surf.blit(small_img, small_rect)

# BARU: Fungsi generik untuk menggambar charge item
def draw_charge_item(surf, x, y, count, icon):
    """ Menggambar ikon dan jumlah charge item """
    icon_rect = icon.get_rect()
    icon_rect.topleft = (x, y)
    surf.blit(icon, icon_rect)
    count_text = charge_font.render(f"x{count}", True, WHITE)
    count_rect = count_text.get_rect()
    count_rect.midleft = (icon_rect.right + 2, icon_rect.centery+1)
    surf.blit(count_text, count_rect)

# PERBARUAN: Fungsi helper untuk koleksi powerup
def handle_player_powerup_collisions(player_sprite, powerups_group):
    """ Menangani kolisi antara player dan powerup """
    if player_sprite: # Pastikan player ada
        powerups_collected = pygame.sprite.spritecollide(player_sprite, powerups_group, True)
        for powerup_hit in powerups_collected:
            print(f"Player collected {powerup_hit.type} powerup!")
            if powerup_hit.type == 'ammo': player_sprite.increase_weapon_level()
            elif powerup_hit.type == 'spread': player_sprite.activate_spread(SPREAD_DURATION)
            elif powerup_hit.type == 'shield': player_sprite.activate_shield() # Ini akan cek shield_upgrade_ready
            elif powerup_hit.type == 'option': player_sprite.add_option()
            elif powerup_hit.type == 'bomb': player_sprite.add_bomb()
            elif powerup_hit.type == 'shield_upgrade': player_sprite.ready_shield_upgrade()
            elif powerup_hit.type == 'piercing': player_sprite.activate_piercing(PIERCING_DURATION)
            elif powerup_hit.type == 'slow_field': player_sprite.activate_slow_field(SLOWFIELD_DURATION)
            elif powerup_hit.type == 'emp': player_sprite.add_emp_charge() # BARU
            elif powerup_hit.type == 'rapid_fire': player_sprite.add_rapid_fire_charge() # BARU
            elif powerup_hit.type == 'scrambler': player_sprite.activate_scrambler(SCRAMBLER_DURATION) # BARU

# --- Fungsi Definisi Wave ---
# (Definisi wave tidak diubah di sini, hanya tanda tangan)
wave_functions = []

# PERBARUAN: Fungsi wave sekarang menerima wave_index untuk penskalaan jumlah
def spawn_wave_line(all_sprites, enemies, wave_index):
    """ Wave tipe Line: Jumlah musuh bertambah seiring wave """
    base_num = 7
    target_num = base_num + int(wave_index * ENEMY_COUNT_SCALE_PER_WAVE * 0.8) # Skala lebih lambat untuk tipe ini
    num_to_spawn = min(target_num, MAX_ENEMIES_ON_SCREEN - len(enemies)) # Hormati batas maks
    print(f"Wave Line (Index {wave_index}): Spawning {num_to_spawn} enemies")

    if num_to_spawn <= 0: return

    # Sesuaikan spacing agar tidak terlalu lebar/sempit
    spacing = max(50, 80 - wave_index * 2)
    total_width = (num_to_spawn - 1) * spacing
    start_x = (SCREEN_WIDTH - total_width) // 2
    start_y = -Enemy.enemy_size

    for i in range(num_to_spawn):
        e = Enemy(start_x + i * spacing, start_y)
        all_sprites.add(e); enemies.add(e)
wave_functions.append(spawn_wave_line)

def spawn_wave_v(all_sprites, enemies, wave_index):
    """ Wave tipe V: Jumlah musuh bertambah seiring wave """
    base_num = 5
    target_num = base_num + int(wave_index * ENEMY_COUNT_SCALE_PER_WAVE)
    num_to_spawn = min(target_num, MAX_ENEMIES_ON_SCREEN - len(enemies))
    print(f"Wave V (Index {wave_index}): Spawning {num_to_spawn} enemies")

    if num_to_spawn <= 0: return

    start_x = SCREEN_WIDTH // 2; start_y = -Enemy.enemy_size * 2
    spacing_x = 60; spacing_y = 40
    # Posisi V dasar
    positions = [(start_x, start_y),
                 (start_x - spacing_x, start_y - spacing_y), (start_x + spacing_x, start_y - spacing_y),
                 (start_x - spacing_x * 2, start_y - spacing_y * 2), (start_x + spacing_x * 2, start_y - spacing_y * 2)]
    # Tambahkan musuh ekstra jika target > 5
    extra_needed = num_to_spawn - len(positions)
    for i in range(extra_needed):
        # Tambahkan di samping atau belakang V
        side = 1 if i % 2 == 0 else -1
        offset_factor = (i // 2) + 3 # Semakin jauh ke samping/belakang
        extra_x = start_x + side * spacing_x * offset_factor
        extra_y = start_y - spacing_y * offset_factor
        positions.append((extra_x, extra_y))

    # Spawn dari posisi yang dihitung
    count = 0
    for x, y in positions:
        if count >= num_to_spawn: break
        if len(enemies) < MAX_ENEMIES_ON_SCREEN:
            e = Enemy(x, y); all_sprites.add(e); enemies.add(e)
            count += 1
wave_functions.append(spawn_wave_v)

def spawn_wave_dashers(all_sprites, enemies, wave_index):
    """ Wave tipe Dasher: Jumlah musuh bertambah seiring wave """
    base_num = 4
    target_num = base_num + int(wave_index * ENEMY_COUNT_SCALE_PER_WAVE * 0.7) # Skala lebih lambat
    num_to_spawn = min(target_num, MAX_ENEMIES_ON_SCREEN - len(enemies))
    print(f"Wave Dashers (Index {wave_index}): Spawning {num_to_spawn} enemies")

    if num_to_spawn <= 0: return

    # Tambahkan lebih banyak posisi spawn dari samping
    positions = []
    y_start = 60; y_increment = 20
    for i in range(num_to_spawn):
        side_x = -DasherEnemy.enemy_size if i % 2 == 0 else SCREEN_WIDTH
        current_y = y_start + (i // 2) * y_increment
        positions.append((side_x, current_y))

    for x, y in positions:
        if len(enemies) < MAX_ENEMIES_ON_SCREEN:
            d = DasherEnemy(x,y); all_sprites.add(d); enemies.add(d)
wave_functions.append(spawn_wave_dashers)

def spawn_wave_minelayers(all_sprites, enemies, wave_index):
    """ Wave tipe MineLayer: Jumlah musuh bertambah seiring wave """
    base_num = 5
    target_num = base_num + int(wave_index * ENEMY_COUNT_SCALE_PER_WAVE * 0.9)
    num_to_spawn = min(target_num, MAX_ENEMIES_ON_SCREEN - len(enemies))
    print(f"Wave Mine Layers (Index {wave_index}): Spawning {num_to_spawn} enemies")

    if num_to_spawn <= 0: return

    spacing = max(60, 100 - wave_index * 3)
    total_width = (num_to_spawn - 1) * spacing
    start_x = max(MineLayerEnemy.enemy_size, min(SCREEN_WIDTH - MineLayerEnemy.enemy_size - total_width, (SCREEN_WIDTH - total_width) // 2)) # Pastikan tidak mulai terlalu pinggir
    start_y = -MineLayerEnemy.enemy_size - 20

    for i in range(num_to_spawn):
        ml = MineLayerEnemy(start_x + i * spacing, start_y - (i%2 * 20)) # Sedikit variasi Y
        all_sprites.add(ml); enemies.add(ml)
wave_functions.append(spawn_wave_minelayers)

def spawn_wave_mix_sides(all_sprites, enemies, wave_index):
    """ Wave tipe Mix Sides: Jumlah musuh bertambah seiring wave """
    base_pairs = 3
    target_pairs = base_pairs + (wave_index // 2)
    num_to_spawn = min(target_pairs * 2, MAX_ENEMIES_ON_SCREEN - len(enemies))
    print(f"Wave Mix Sides (Index {wave_index}): Spawning {num_to_spawn} enemies")

    if num_to_spawn <= 0: return

    positions = []
    y_start = 50; y_increment = 20
    for i in range(target_pairs): # Buat pasangan posisi
        pos_left = (-Enemy.enemy_size, y_start + i * y_increment * 2)
        pos_right = (SCREEN_WIDTH, y_start + i * y_increment * 2 + y_increment)
        positions.append(pos_left)
        positions.append(pos_right)

    count = 0
    for i, (x, y) in enumerate(positions):
        if count >= num_to_spawn: break
        if len(enemies) < MAX_ENEMIES_ON_SCREEN:
            # Ganti tipe musuh (misal: lebih banyak dasher di wave lanjut)
            dasher_chance = 0.4 + wave_index * 0.05
            enemy_type = DasherEnemy if random.random() < dasher_chance else Enemy
            e = enemy_type(x, y); all_sprites.add(e); enemies.add(e)
            count += 1
wave_functions.append(spawn_wave_mix_sides)

# PERBARUAN: Wave campuran baru yang lebih menantang
def spawn_wave_mixed_challenge(all_sprites, enemies, wave_index):
    """ Wave tipe Mixed Challenge: Jumlah musuh bertambah + Commander """
    print(f"Wave Mixed Challenge (Index {wave_index})")
    spawned_count = 0
    # Target total dikurangi 1 untuk Commander
    max_spawn_this_wave = min(ENEMY_COUNT_BASE + int(wave_index * ENEMY_COUNT_SCALE_PER_WAVE * 1.2) -1, MAX_ENEMIES_ON_SCREEN - len(enemies) -1)

    if max_spawn_this_wave < 0: max_spawn_this_wave = 0

    # Spawn Commander jika wave cukup tinggi (misal index 5 ke atas, yaitu wave 6)
    commander_spawned = False
    if wave_index >= 5 and len(enemies) < MAX_ENEMIES_ON_SCREEN:
         cmd = CommanderEnemy(SCREEN_WIDTH // 2 - CommanderEnemy.enemy_size // 2, -CommanderEnemy.enemy_size - 10)
         all_sprites.add(cmd); enemies.add(cmd)
         commander_spawned = True
         print("- Spawning Commander")

    # Enemy tengah (jumlah berdasarkan wave)
    num_enemy = min(max_spawn_this_wave, 4 + wave_index // 2)
    spacing_enemy = 80
    total_width_enemy = (num_enemy - 1) * spacing_enemy
    start_x_enemy = (SCREEN_WIDTH - total_width_enemy) // 2; start_y_enemy = -Enemy.enemy_size - 40
    for i in range(num_enemy):
        if len(enemies) < MAX_ENEMIES_ON_SCREEN and spawned_count < max_spawn_this_wave:
            e = Enemy(start_x_enemy + i * spacing_enemy, start_y_enemy); all_sprites.add(e); enemies.add(e)
            spawned_count += 1
    # Dasher samping (jumlah berdasarkan wave)
    num_dashers = min(max_spawn_this_wave - spawned_count, 2 + wave_index // 3)
    for i in range(num_dashers):
         if len(enemies) < MAX_ENEMIES_ON_SCREEN and spawned_count < max_spawn_this_wave:
             side_x = -DasherEnemy.enemy_size if i % 2 == 0 else SCREEN_WIDTH
             y_pos = 60 + i * 40
             d = DasherEnemy(side_x, y_pos); all_sprites.add(d); enemies.add(d)
             spawned_count += 1
    # Mine Layer atas (jumlah berdasarkan wave)
    num_minelayers = min(max_spawn_this_wave - spawned_count, 2 + wave_index // 3)
    for i in range(num_minelayers):
         if len(enemies) < MAX_ENEMIES_ON_SCREEN and spawned_count < max_spawn_this_wave:
             x_pos = SCREEN_WIDTH * (0.25 + i*0.5)
             y_pos = -MineLayerEnemy.enemy_size - i * 30
             ml = MineLayerEnemy(x_pos, y_pos); all_sprites.add(ml); enemies.add(ml)
             spawned_count += 1

    total_spawned = spawned_count + (1 if commander_spawned else 0)
    print(f"Spawned {total_spawned} total enemies for Mixed Challenge.")
wave_functions.append(spawn_wave_mixed_challenge)


# --- Variabel Game ---
game_state = TITLE_SCREEN; score = 0
boss_level = 1; next_boss_wave = BOSS_WAVE_INTERVAL
state_before_pause = PLAYING
score_multiplier = 1; consecutive_kills = 0
current_wave_index = 0
wave_transition_timer = 0

# Grup sprite
all_sprites = pygame.sprite.Group(); enemies = pygame.sprite.Group(); bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group(); player_group = pygame.sprite.Group(); powerups = pygame.sprite.Group()
boss_group = pygame.sprite.GroupSingle(); boss_bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()
mines = pygame.sprite.Group()

player = Player()
player_life_icon = player.original_image.copy()

# --- Game Loop ---
running = True
while running:
    dt = clock.tick(60); now = pygame.time.get_ticks()

    # --- Penanganan Event ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state == PLAYING or game_state == BOSS_FIGHT:
                    state_before_pause = game_state; game_state = PAUSED; print("Game Paused")
            elif game_state == PAUSED:
                 if event.key != pygame.K_ESCAPE:
                     game_state = state_before_pause; print("Game Resumed")
            elif game_state == TITLE_SCREEN:
                if event.key == pygame.K_SPACE:
                    # Reset game state
                    all_sprites.empty(); enemies.empty(); bullets.empty()
                    enemy_bullets.empty(); player_group.empty(); powerups.empty()
                    boss_group.empty(); boss_bullets.empty(); explosions.empty(); mines.empty()
                    player = Player(); all_sprites.add(player); player_group.add(player)
                    score = 0; boss_level = 1; next_boss_wave = BOSS_WAVE_INTERVAL
                    score_multiplier = 1; consecutive_kills = 0
                    current_wave_index = 0
                    game_state = WAVE_TRANSITION
                    wave_transition_timer = now
            elif game_state == GAME_OVER:
                if event.key == pygame.K_r: game_state = TITLE_SCREEN
            elif (game_state == PLAYING or game_state == BOSS_FIGHT): # Hanya jika sedang bermain
                if event.key == pygame.K_b: # Gunakan Bom
                    if player in player_group:
                        player.use_bomb(enemies, enemy_bullets)
                elif event.key == pygame.K_f: # BARU: Gunakan EMP
                    if player in player_group:
                        player.use_emp(enemy_bullets, boss_bullets)
                elif event.key == pygame.K_r: # BARU: Aktifkan Rapid Fire
                     if player in player_group:
                         player.activate_rapid_fire()


    # --- Update (Hanya jika tidak sedang PAUSED) ---
    if game_state != PAUSED:
        player_group.update()
        bullets.update()
        enemy_bullets.update()
        powerups.update()
        boss_bullets.update()
        explosions.update()
        mines.update() # Ini akan memanggil Mine.explode jika timer habis

        # PERBARUAN: Pindahkan logika koleksi powerup ke sini agar aktif di semua state relevan
        if player in player_group:
             handle_player_powerup_collisions(player, powerups)

        # Logika spesifik per state
        if game_state == PLAYING:
            # PERBARUAN: Update musuh, termasuk Commander yg perlu grup sprite
            for enemy in enemies:
                 if isinstance(enemy, CommanderEnemy):
                      enemy.update(all_sprites, enemies) # Pass grup ke Commander
                 else:
                      enemy.update() # Update musuh biasa

            # Musuh menembak/drop
            for enemy in enemies:
                if hasattr(enemy, 'shoot'):
                    enemy.shoot(all_sprites, enemy_bullets)

            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                if player in player_group: player.shoot(all_sprites, bullets)

            if not enemies:
                 print(f"Wave {current_wave_index + 1} Cleared!")
                 game_state = WAVE_TRANSITION
                 wave_transition_timer = now
                 current_wave_index += 1

            # --- Collision Detection (PLAYING state) ---
            player_died_this_frame = False
            if player in player_group:
                # Cek kolisi player vs ranjau (hanya untuk trigger explode)
                mines_hit_player_direct = pygame.sprite.spritecollide(player, mines, False)
                if mines_hit_player_direct:
                     for mine_hit in mines_hit_player_direct:
                         if mine_hit in mines:
                              mine_hit.explode(player_group)
                              # Cek jika player mati karena ledakan ranjau
                              if player not in player_group:
                                   player_died_this_frame = True
                                   break # Keluar loop ranjau jika player mati
                # Cek kolisi lain HANYA jika player masih hidup
                if not player_died_this_frame and player in player_group and not player.invincible and not player.hidden:
                    hit_by_bullet = pygame.sprite.groupcollide(player_group, enemy_bullets, False, True)
                    hit_by_enemy = pygame.sprite.groupcollide(player_group, enemies, False, True)

                    # PERBARUAN: Logika refleksi perisai
                    reflected_bullets = []
                    if player.shield_active and player.current_shield_reflects:
                        # Gunakan spritecollide lagi untuk peluru yg mungkin baru muncul
                        bullets_hitting_shield = pygame.sprite.spritecollide(player, enemy_bullets, True) # Hancurkan peluru musuh
                        for bullet_hit in bullets_hitting_shield:
                            # Hanya pantulkan peluru kuning standar
                            if bullet_hit.color == YELLOW:
                                print("Reflecting enemy bullet!")
                                # Buat peluru pantulan
                                reflect_bullet = Bullet(player.rect.centerx, player.rect.top, 0, -BULLET_SPEED, WHITE)
                                reflected_bullets.append(reflect_bullet)
                            # Perisai tetap pecah setelah menahan/memantulkan
                            player.deactivate_shield()
                            # Tidak perlu proses damage lebih lanjut krn perisai aktif
                            hit_by_bullet = {} # Kosongkan agar tidak diproses lagi di bawah
                            hit_by_enemy = {} # Kolisi badan tetap pecahkan perisai tapi tidak dipantul

                    if reflected_bullets:
                        all_sprites.add(reflected_bullets)
                        bullets.add(reflected_bullets) # Tambahkan ke peluru pemain

                    # Proses damage jika TIDAK ada perisai (atau perisai sudah pecah frame ini)
                    if (hit_by_bullet or hit_by_enemy) and not player.shield_active:
                        if not player.invincible: # Cek invincibility
                             expl = Explosion(player.rect.center, 60); all_sprites.add(expl); explosions.add(expl)
                             if player.hide():
                                  player_died_this_frame = True # Tandai mati
                                  if player.lives <= 0: game_state = GAME_OVER
                             # Musuh yg menabrak sudah dihapus oleh groupcollide=True
                             for enemy_hit_list in hit_by_enemy.values():
                                 for e in enemy_hit_list:
                                     expl_e = Explosion(e.rect.center, 40); all_sprites.add(expl_e); explosions.add(expl_e);
                        # Jika invincible, tidak terjadi apa-apa

                    # PERBARUAN: Hapus logika koleksi powerup dari sini (sudah dipindah ke luar)
                    # powerup_hits = pygame.sprite.groupcollide(player_group, powerups, False, True) ...

            # Kolisi Musuh vs Peluru Pemain (di luar cek player hidup)
            # PERBARUAN: Logika piercing rounds
            enemies_hit_by_player = pygame.sprite.groupcollide(enemies, bullets, False, False) # Jangan kill bullet dulu
            for enemy, bullets_that_hit in enemies_hit_by_player.items():
                 if enemy in all_sprites:
                     enemy_center = enemy.rect.center
                     enemy_type = type(enemy)
                     is_commander = isinstance(enemy, CommanderEnemy)
                     is_mine_layer = isinstance(enemy, MineLayerEnemy)
                     is_tough = is_commander or is_mine_layer # Musuh yg menghentikan piercing

                     # Proses damage ke musuh
                     should_kill_enemy = False
                     if is_commander:
                         if enemy.take_damage(len(bullets_that_hit)): # Commander butuh bbrp hit
                             should_kill_enemy = True
                             score += 50 * score_multiplier
                             powerup_type = random.choice(['shield', 'bomb', 'option', 'shield_upgrade']) # Drop bagus
                             powerup = PowerUp(enemy_center, powerup_type); all_sprites.add(powerup); powerups.add(powerup)
                         else:
                             enemy.flash()
                     else: # Musuh biasa
                         if enemy.take_damage(len(bullets_that_hit)): # Tetap panggil take_damage (meski hanya flash)
                             should_kill_enemy = True
                             score += 10 * score_multiplier
                             # Drop powerup biasa
                             if random.random() < POWERUP_DROP_CHANCE:
                                 # Tambahkan powerup baru ke pool drop
                                 powerup_pool = ['ammo', 'ammo', 'spread', 'shield', 'option', 'bomb',
                                                 'shield_upgrade', 'piercing', 'slow_field', 'emp', 'rapid_fire', 'scrambler'] # Tambahkan item baru
                                 powerup_type = random.choice(powerup_pool)
                                 powerup = PowerUp(enemy_center, powerup_type); all_sprites.add(powerup); powerups.add(powerup)

                     # Hancurkan musuh jika perlu
                     if should_kill_enemy:
                         expl_s = Explosion(enemy_center, 30); all_sprites.add(expl_s); explosions.add(expl_s)
                         expl_e = Explosion(enemy_center, 40 if not is_commander else 50); all_sprites.add(expl_e); explosions.add(expl_e)
                         enemy.kill()
                         consecutive_kills += 1

                         # Cek drop ranjau jika MineLayer mati
                         if enemy_type is MineLayerEnemy:
                             print("Mine Layer destroyed, dropping mines!")
                             for _ in range(MINES_ON_DEATH):
                                 death_mine = Mine(enemy_center[0] + random.randint(-10, 10), enemy_center[1])
                                 all_sprites.add(death_mine)
                                 mines.add(death_mine)

                         # Cek multiplier
                         if consecutive_kills >= MULTIPLIER_THRESHOLD:
                              score_multiplier = min(score_multiplier + 1, MAX_MULTIPLIER); consecutive_kills = 0; print(f"Multiplier Up! x{score_multiplier}")

                     # Proses peluru (hancurkan atau biarkan tembus)
                     for bullet in bullets_that_hit:
                         if bullet in bullets: # Pastikan peluru masih ada
                             if player in player_group and player.piercing_rounds_active:
                                 # Peluru tembus kecuali kena musuh kuat
                                 if is_tough:
                                     bullet.kill()
                             else:
                                 # Peluru normal selalu hancur
                                 bullet.kill()

            # Reset multiplier jika pemain mati di frame ini (setelah semua kolisi dicek)
            if player_died_this_frame: score_multiplier = 1; consecutive_kills = 0

        elif game_state == WAVE_TRANSITION:
             # Update penting selama transisi (misal: pergerakan powerup)
             # Logika koleksi powerup sudah dipindah ke luar state check

             # Cek selesai transisi
             if now - wave_transition_timer > WAVE_TRANSITION_DELAY:
                 next_wave_num = current_wave_index + 1
                 if next_wave_num % BOSS_WAVE_INTERVAL == 0:
                      game_state = BOSS_FIGHT
                      current_boss_level = next_wave_num // BOSS_WAVE_INTERVAL
                      print(f"WAVE {next_wave_num}. BOSS FIGHT LEVEL {current_boss_level} START!")
                      for sprite in enemies: sprite.kill()
                      for sprite in enemy_bullets: sprite.kill()
                      for sprite in mines: sprite.kill()
                      boss = BossEnemy(current_boss_level); all_sprites.add(boss); boss_group.add(boss)
                      if player in player_group:
                          player.reset_boss_health()
                          # PERBARUAN: Berikan item otomatis saat boss mulai
                          print("Granting automatic items for boss fight...")
                          possible_items = ['ammo', 'shield', 'bomb', 'option', 'shield_upgrade',
                                            'piercing', 'slow_field', 'emp', 'rapid_fire', 'scrambler'] # Tambahkan item baru
                          items_to_grant = []
                          if AUTO_ITEMS_ON_BOSS_START > 0 and len(possible_items) > 0:
                               items_to_grant = random.sample(possible_items, k=min(AUTO_ITEMS_ON_BOSS_START, len(possible_items)))

                          for item_type in items_to_grant:
                              print(f"- Granting {item_type}")
                              if item_type == 'ammo': player.increase_weapon_level()
                              elif item_type == 'shield': player.activate_shield() # Akan cek upgrade
                              elif item_type == 'bomb': player.add_bomb()
                              elif item_type == 'option': player.add_option()
                              elif item_type == 'shield_upgrade': player.ready_shield_upgrade()
                              elif item_type == 'piercing': player.activate_piercing(PIERCING_DURATION)
                              elif item_type == 'slow_field': player.activate_slow_field(SLOWFIELD_DURATION)
                              elif item_type == 'emp': player.add_emp_charge()
                              elif item_type == 'rapid_fire': player.add_rapid_fire_charge()
                              elif item_type == 'scrambler': player.activate_scrambler(SCRAMBLER_DURATION)


                 else:
                      game_state = PLAYING
                      wave_func_index = current_wave_index % len(wave_functions)
                      print(f"Starting Wave {next_wave_num} (Function Index: {wave_func_index})")
                      for sprite in mines: sprite.kill()
                      # PERBARUAN: Pass wave_index ke fungsi spawn
                      wave_functions[wave_func_index](all_sprites, enemies, current_wave_index)


        elif game_state == BOSS_FIGHT:
            # PERBARUAN: Pass objek player ke update boss
            boss_group.update(player if player in player_group else None)

            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                if player in player_group: player.shoot(all_sprites, bullets)

            boss = boss_group.sprite
            if boss:
                 # PERBARUAN: Logika piercing rounds vs boss
                 bullets_hitting_boss = pygame.sprite.spritecollide(boss, bullets, False) # Jangan kill bullet dulu
                 if bullets_hitting_boss:
                     damage_dealt = len(bullets_hitting_boss)
                     # PERBARUAN: Pass grup sprite ke take_damage
                     if boss.take_damage(damage_dealt, all_sprites, powerups):
                         current_boss_level = boss.level
                         print(f"BOSS LEVEL {current_boss_level} DEFEATED!");
                         score += current_boss_level * 100 * score_multiplier
                         expl_b = Explosion(boss.rect.center, 100); all_sprites.add(expl_b); explosions.add(expl_b)
                         boss.kill()
                         for bullet in boss_bullets: bullet.kill()
                         current_wave_index += 1
                         print(f"Wave index incremented to: {current_wave_index}")
                         game_state = WAVE_TRANSITION
                         wave_transition_timer = now
                         score_multiplier = 1; consecutive_kills = 0
                     # Hancurkan peluru pemain setelah mengenai boss
                     for bullet in bullets_hitting_boss:
                         bullet.kill()

            # Kolisi Pemain vs Peluru Boss & Ranjau
            player_died_this_frame = False # Lacak kematian di state ini juga
            if player in player_group:
                # Cek kolisi ranjau dulu
                mines_hit_player_direct = pygame.sprite.spritecollide(player, mines, False)
                if mines_hit_player_direct:
                    for mine_hit in mines_hit_player_direct:
                        if mine_hit in mines:
                            mine_hit.explode(player_group)
                            # Cek jika player mati karena ledakan ranjau
                            if player not in player_group:
                                player_died_this_frame = True
                                break # Keluar loop ranjau jika player mati
                # Jika player masih hidup, cek kolisi peluru boss
                if not player_died_this_frame and player in player_group and not player.invincible and not player.hidden:
                    # PERBARUAN: Logika refleksi perisai vs peluru boss
                    reflected_bullets = []
                    if player.shield_active and player.current_shield_reflects:
                        bullets_hitting_shield = pygame.sprite.spritecollide(player, boss_bullets, True) # Hancurkan peluru boss
                        for bullet_hit in bullets_hitting_shield:
                            # Pantulkan semua peluru boss
                            print("Reflecting boss bullet!")
                            reflect_bullet = Bullet(player.rect.centerx, player.rect.top, 0, -BULLET_SPEED, WHITE) # Peluru pantulan = peluru player
                            reflected_bullets.append(reflect_bullet)
                        if bullets_hitting_shield: # Jika ada yg kena perisai reflektif
                            player.deactivate_shield() # Perisai pecah
                    else: # Perisai normal atau tidak ada perisai
                        hits_on_player = pygame.sprite.spritecollide(player, boss_bullets, True) # Hancurkan peluru boss
                        if hits_on_player:
                             if not player.shield_active: # Tidak ada perisai
                                 expl_p = Explosion(player.rect.center, 60); all_sprites.add(expl_p); explosions.add(expl_p)
                                 player.take_boss_damage(len(hits_on_player))
                                 if player.current_boss_health <= 0:
                                     player_died_this_frame = True # Tandai mati karena HP habis
                                     game_state = GAME_OVER
                             else: # Perisai normal aktif
                                 player.deactivate_shield()

                    if reflected_bullets:
                        all_sprites.add(reflected_bullets)
                        bullets.add(reflected_bullets)

                    # PERBARUAN: Hapus logika koleksi powerup dari sini (sudah dipindah ke luar)
                    # powerup_hits = pygame.sprite.groupcollide(player_group, powerups, False, True) ...

            # Reset multiplier jika pemain mati di frame ini
            if player_died_this_frame: score_multiplier = 1; consecutive_kills = 0


    # --- Draw / Render ---
    screen.fill(BLACK)

    if game_state != TITLE_SCREEN and game_state != GAME_OVER:
        all_sprites.draw(screen);
        draw_text(screen, f"Skor: {score}", 18, SCREEN_WIDTH / 2, 10)
        draw_text(screen, f"High Score: {high_score}", 18, SCREEN_WIDTH - 80, 10)
        if score_multiplier > 1: draw_text(screen, f"x{score_multiplier}", 24, SCREEN_WIDTH / 2 + 80, 8, YELLOW)

        if player in player_group:
             player.draw_shield(screen) # Gambar perisai (bisa reflektif)
             player.draw_slow_field(screen) # Gambar visual slow field jika aktif
             player.draw_active_effects(screen) # Gambar visual EMP & Rapid Fire glow

             # Tampilkan status efek aktif
             status_texts = []
             # Urutkan berdasarkan prioritas atau sisa waktu?
             if player.rapid_fire_active:
                 remaining_time = max(0, (player.rapid_fire_end_time - now) // 1000)
                 status_texts.append(f"Rapid: {remaining_time}s")
             if player.piercing_rounds_active:
                 remaining_time = max(0, (player.piercing_rounds_end_time - now) // 1000)
                 status_texts.append(f"Pierce: {remaining_time}s")
             if player.slow_field_active:
                 remaining_time = max(0, (player.slow_field_end_time - now) // 1000)
                 status_texts.append(f"Slow: {remaining_time}s")
             if player.scrambler_active:
                 remaining_time = max(0, (player.scrambler_end_time - now) // 1000)
                 status_texts.append(f"Scramble: {remaining_time}s")
             if player.shield_upgrade_ready:
                 status_texts.append("Reflect Ready!")

             level_text = f"Level: {player.weapon_level}"
             if player.spread_active:
                 remaining_spread_time = max(0, (player.spread_end_time - now) // 1000)
                 level_text = f"Spread: {remaining_spread_time}s"

             draw_text(screen, level_text, 18, 70, 10)
             # Tampilkan status efek lain di bawah level
             for i, status in enumerate(status_texts):
                  draw_text(screen, status, 14, 70, 30 + i * 15, YELLOW)


             ui_y_pos = SCREEN_HEIGHT - 30
             # BARU: Atur posisi X untuk item charges agar lebih rapi
             charge_x_start = SCREEN_WIDTH - 180
             charge_spacing = 60
             if game_state == PLAYING or (game_state == PAUSED and state_before_pause == PLAYING) or game_state == WAVE_TRANSITION:
                 draw_player_lives(screen, SCREEN_WIDTH - 100, ui_y_pos, player.lives, player_life_icon)
                 draw_charge_item(screen, charge_x_start, ui_y_pos + 2, player.bomb_count, bomb_icon_surf)
                 draw_charge_item(screen, charge_x_start - charge_spacing, ui_y_pos + 2, player.emp_charges, emp_icon_surf)
                 draw_charge_item(screen, charge_x_start - charge_spacing*2, ui_y_pos + 2, player.rapid_fire_charges, rapid_icon_surf)
             elif game_state == BOSS_FIGHT or (game_state == PAUSED and state_before_pause == BOSS_FIGHT):
                 if boss in boss_group: boss.draw_health_bar(screen)
                 draw_player_health_bar(screen, 10, SCREEN_HEIGHT - 20, player.current_boss_health, PLAYER_BOSS_HEALTH)
                 draw_text(screen, "HP:", 14, 120, SCREEN_HEIGHT - 22)
                 # BARU: Atur posisi X untuk item charges saat boss
                 charge_x_start_boss = SCREEN_WIDTH - 100
                 draw_charge_item(screen, charge_x_start_boss, ui_y_pos + 2, player.bomb_count, bomb_icon_surf)
                 draw_charge_item(screen, charge_x_start_boss - charge_spacing, ui_y_pos + 2, player.emp_charges, emp_icon_surf)
                 draw_charge_item(screen, charge_x_start_boss - charge_spacing*2, ui_y_pos + 2, player.rapid_fire_charges, rapid_icon_surf)

        if game_state == WAVE_TRANSITION:
             time_since_transition = now - wave_transition_timer
             alpha = 255
             fade_start_time = WAVE_TRANSITION_DELAY * 0.7
             fade_duration = WAVE_TRANSITION_DELAY * 0.3
             if time_since_transition > fade_start_time and fade_duration > 0:
                  alpha = max(0, 255 - int(((time_since_transition - fade_start_time) / fade_duration) * 255))

             next_wave_display_num = current_wave_index + 1
             text_to_display = f"WAVE {next_wave_display_num}"
             text_color = WHITE
             if next_wave_display_num % BOSS_WAVE_INTERVAL == 0:
                 text_to_display = f"BOSS INCOMING!"
                 text_color = RED

             font = pygame.font.Font(font_name, 48)
             text_surface = font.render(text_to_display, True, text_color)
             text_surface.set_alpha(alpha)
             text_rect = text_surface.get_rect()
             text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30)
             screen.blit(text_surface, text_rect)

        if player in player_group and player.bomb_flash_active:
            flash_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            flash_surface.fill(WHITE)
            flash_surface.set_alpha(180)
            screen.blit(flash_surface, (0, 0))

    # PERBARUAN: Logika Tampilan Beranda (Title Screen)
    if game_state == TITLE_SCREEN:
        # Judul Besar
        draw_text(screen, "Don-shoot Near", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 - 40)

        # Gambar Sprite Player di Tengah
        player_icon_large = pygame.transform.scale(player_life_icon, (60, 60)) # Perbesar ikon
        player_icon_rect = player_icon_large.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
        screen.blit(player_icon_large, player_icon_rect)

        # Instruksi Dasar
        draw_text(screen, "Gunakan Panah/AD untuk Bergerak, Spasi untuk Menembak", 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 10)
        # Instruksi Item Aktif
        draw_text(screen, "Tekan B: Bom, F: EMP, R: Rapid Fire", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40, YELLOW) # Warna beda

        # High Score
        draw_text(screen, f"High Score: {high_score}", 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 75)

        # Prompt Mulai (Berkedip)
        if (pygame.time.get_ticks() // TITLE_BLINK_INTERVAL) % 2 == 0:
             draw_text(screen, "Tekan SPASI untuk Mulai", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)

        # Kredit Developer (BARU)
        draw_text(screen, "Dibuat oleh @HikiNarou", 14, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 45)
        draw_text(screen, "Github: https://github.com/HikiNarou", 14, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 25)

    elif game_state == GAME_OVER:
        if score > high_score: high_score = score
        draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        draw_text(screen, f"Skor Akhir: {score}", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20)
        draw_text(screen, f"High Score: {high_score}", 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20)
        final_wave = current_wave_index
        draw_text(screen, f"Mencapai Wave: {final_wave + 1}", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60)
        draw_text(screen, "Tekan R untuk Kembali ke Layar Judul", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
    elif game_state == PAUSED:
        pause_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        pause_surface.fill(PAUSE_OVERLAY_COLOR); screen.blit(pause_surface, (0,0))
        draw_text(screen, "PAUSED", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50)
        draw_text(screen, "Tekan tombol apa saja (selain ESC) untuk melanjutkan", 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20)

    pygame.display.flip()

# --- Keluar dari Pygame ---
pygame.quit()
