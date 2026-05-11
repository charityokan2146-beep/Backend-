signals(id, signal_id, created_at, account_id, symbol,
        direction, entry, sl, tp1, tp2, confidence,
        regime, playbook, action, reasons_json,
        tp_first_prob, consumed)

heartbeats(account_id UNIQUE, received_at, symbol,
           equity, balance, free_margin,
           spread_points, open_positions)

events(id, occurred_at, account_id, signal_id,
       event_type, symbol, direction, volume,
       open_price, close_price, profit, detail_json)

daily_stats(stat_date, account_id UNIQUE per day,
            realized_pnl, trade_count,
            consecutive_losses, cooldown_until)
